"""
Recalculates Winter Arc stats from data/tracker.json, scans syllabus/*.md
for checkbox progress, and rewrites the two marked blocks in README.md:

  <!-- STATS:START -->    ... <!-- STATS:END -->
  <!-- SYLLABUS:START --> ... <!-- SYLLABUS:END -->

Run from anywhere inside the repo:
    python scripts/update_readme.py
"""

import json
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "tracker.json"
README_PATH = ROOT / "README.md"
SYLLABUS_DIR = ROOT / "syllabus"

STATS_START, STATS_END = "<!-- STATS:START -->", "<!-- STATS:END -->"
SYL_START, SYL_END = "<!-- SYLLABUS:START -->", "<!-- SYLLABUS:END -->"

CATEGORY_LABELS = {
    "wake_before_8": "Wake before 8 AM",
    "exam_prep": "Exam Prep (NET-JRF / GATE / math)",
    "programming": "Programming / Open Source",
    "fitness_diet": "Fitness & Clean Diet",
    "relationships": "Relationships & Connection",
}

CHECKBOX_RE = re.compile(r"^\s*-\s\[( |x|X)\]", re.MULTILINE)


# ---------- habit stats ----------

def load_data():
    with open(DATA_PATH) as f:
        return json.load(f)


def compute_stats(data):
    days = data["days"]
    categories = data["categories"]
    start = datetime.date.fromisoformat(data["start_date"])
    end = datetime.date.fromisoformat(data["end_date"])
    total_arc_days = (end - start).days + 1

    total_score = 0
    per_cat_done = {c: 0 for c in categories}
    per_cat_missed = {c: 0 for c in categories}
    perfect_days = 0
    logged_dates = sorted(days.keys())

    for date_str in logged_dates:
        entry = days[date_str]
        scheduled = [c for c in categories if c in entry]
        all_done = bool(scheduled)
        for c in categories:
            val = entry.get(c)
            if val is True:
                total_score += 1
                per_cat_done[c] += 1
            elif val is False:
                total_score -= 1
                per_cat_missed[c] += 1
                all_done = False
        if all_done:
            perfect_days += 1

    streak = 0
    for date_str in reversed(logged_dates):
        entry = days[date_str]
        net = sum(
            1 if entry.get(c) is True else (-1 if entry.get(c) is False else 0)
            for c in categories
        )
        if net > 0:
            streak += 1
        else:
            break

    days_elapsed = (datetime.date.today() - start).days + 1
    days_elapsed = max(0, min(days_elapsed, total_arc_days))

    return {
        "total_score": total_score,
        "days_logged": len(logged_dates),
        "total_arc_days": total_arc_days,
        "days_elapsed": days_elapsed,
        "perfect_days": perfect_days,
        "current_streak": streak,
        "per_cat_done": per_cat_done,
        "per_cat_missed": per_cat_missed,
    }


def render_bar(done, missed, width=20):
    total = done + missed
    if total == 0:
        return "`" + ("░" * width) + "` 0%"
    pct = done / total
    filled = round(pct * width)
    bar = "█" * filled + "░" * (width - filled)
    return f"`{bar}` {pct * 100:.0f}%"


def render_stats_block(data, stats):
    lines = [
        f"**Score: {stats['total_score']:+d}**  |  "
        f"Days logged: {stats['days_logged']}/{stats['total_arc_days']}  |  "
        f"Perfect days: {stats['perfect_days']}  |  "
        f"Current streak: {stats['current_streak']} 🔥",
        "",
        f"Arc progress: "
        f"{render_bar(stats['days_elapsed'], stats['total_arc_days'] - stats['days_elapsed'])} "
        f"({stats['days_elapsed']}/{stats['total_arc_days']} days elapsed)",
        "",
        "| Habit | Done | Missed | Consistency |",
        "|---|---|---|---|",
    ]
    for c in data["categories"]:
        label = CATEGORY_LABELS.get(c, c)
        done = stats["per_cat_done"][c]
        missed = stats["per_cat_missed"][c]
        lines.append(f"| {label} | {done} | {missed} | {render_bar(done, missed, 12)} |")
    lines.append("")
    lines.append(f"_Last updated: {datetime.date.today().isoformat()}_")
    return "\n".join(lines)


# ---------- syllabus progress ----------

def compute_syllabus_progress():
    results = []
    if not SYLLABUS_DIR.exists():
        return results
    for path in sorted(SYLLABUS_DIR.glob("*.md")):
        text = path.read_text()
        boxes = CHECKBOX_RE.findall(text)
        total = len(boxes)
        done = sum(1 for b in boxes if b.lower() == "x")
        results.append({"name": path.stem.replace("_", " ").title(), "done": done, "total": total})
    return results


def render_syllabus_block(progress):
    if not progress:
        return "_No syllabus files found in `syllabus/`._"
    lines = ["| Track | Topics done | Total | Progress |", "|---|---|---|---|"]
    for p in progress:
        remaining = p["total"] - p["done"]
        lines.append(
            f"| {p['name']} | {p['done']} | {p['total']} | {render_bar(p['done'], remaining, 12)} |"
        )
    lines.append("")
    lines.append(
        "_Check off topics directly in the `syllabus/*.md` files "
        "(`- [ ]` -> `- [x]`) as you cover them._"
    )
    return "\n".join(lines)


# ---------- README writing ----------

def replace_block(text, start_mark, end_mark, new_content):
    if start_mark not in text or end_mark not in text:
        raise RuntimeError(f"README markers not found: {start_mark} / {end_mark}")
    before = text.split(start_mark)[0]
    after = text.split(end_mark)[1]
    return before + start_mark + "\n" + new_content + "\n" + end_mark + after


def main():
    data = load_data()
    stats = compute_stats(data)
    stats_block = render_stats_block(data, stats)

    progress = compute_syllabus_progress()
    syllabus_block = render_syllabus_block(progress)

    text = README_PATH.read_text()
    text = replace_block(text, STATS_START, STATS_END, stats_block)
    text = replace_block(text, SYL_START, SYL_END, syllabus_block)
    README_PATH.write_text(text)

    print("README updated.\n")
    print(stats_block)
    print()
    print(syllabus_block)


if __name__ == "__main__":
    main()
