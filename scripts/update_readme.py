"""
Recalculates Winter Arc stats from data/tracker.json, scans syllabus/*.md
for checkbox progress, writes shields.io badge JSON files to
data/badges/*.json, and rewrites the two marked blocks in README.md:

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
BADGE_DIR = ROOT / "data" / "badges"

STATS_START, STATS_END = "<!-- STATS:START -->", "<!-- STATS:END -->"
SYL_START, SYL_END = "<!-- SYLLABUS:START -->", "<!-- SYLLABUS:END -->"

# Update this if the repo is ever renamed or moved to a different branch.
RAW_BASE = "https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges"

CATEGORY_LABELS = {
    "wake_before_8": "Wake before 8 AM",
    "exam_prep": "Exam Prep (NET-JRF / GATE / math)",
    "programming": "Programming / Open Source",
    "fitness_diet": "Fitness & Clean Diet",
    "relationships": "Relationships & Connection",
}

CHECKBOX_RE = re.compile(r"^\s*-\s\[( |x|X)\]", re.MULTILINE)


# ---------- badge helpers ----------

def pct_color(pct):
    if pct is None:
        return "lightgrey"
    if pct >= 75:
        return "brightgreen"
    if pct >= 50:
        return "yellow"
    if pct >= 25:
        return "orange"
    return "red"


def write_badge(filename, label, message, color):
    BADGE_DIR.mkdir(parents=True, exist_ok=True)
    payload = {"schemaVersion": 1, "label": label, "message": str(message), "color": color}
    (BADGE_DIR / filename).write_text(json.dumps(payload))


def badge_md(filename, alt):
    return f"![{alt}]({RAW_BASE}/{filename})"


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


def write_habit_badges(data, stats):
    score = stats["total_score"]
    write_badge(
        "score.json", "score",
        f"{score:+d}",
        "brightgreen" if score > 0 else ("lightgrey" if score == 0 else "red"),
    )
    write_badge(
        "streak.json", "streak",
        f"{stats['current_streak']} days",
        "brightgreen" if stats["current_streak"] > 0 else "lightgrey",
    )
    write_badge("perfect_days.json", "perfect days", stats["perfect_days"], "blueviolet")
    write_badge(
        "days_logged.json", "days logged",
        f"{stats['days_logged']}/{stats['total_arc_days']}",
        "informational",
    )
    arc_pct = round(100 * stats["days_elapsed"] / stats["total_arc_days"]) if stats["total_arc_days"] else 0
    write_badge(
        "arc_progress.json", "arc progress",
        f"{arc_pct}% ({stats['days_elapsed']}/{stats['total_arc_days']})",
        "blue",
    )
    for c in data["categories"]:
        done = stats["per_cat_done"][c]
        missed = stats["per_cat_missed"][c]
        total = done + missed
        pct = round(100 * done / total) if total else None
        label = CATEGORY_LABELS.get(c, c)
        msg = f"{pct}% ({done}/{total})" if total else "not logged yet"
        write_badge(f"habit_{c}.json", label, msg, pct_color(pct) if total else "lightgrey")


def render_stats_block(data, stats):
    lines = [
        f"{badge_md('score.json', 'Score')} "
        f"{badge_md('streak.json', 'Streak')} "
        f"{badge_md('perfect_days.json', 'Perfect Days')} "
        f"{badge_md('days_logged.json', 'Days Logged')} "
        f"{badge_md('arc_progress.json', 'Arc Progress')}",
        "",
        "| Habit | Consistency |",
        "|---|---|",
    ]
    for c in data["categories"]:
        label = CATEGORY_LABELS.get(c, c)
        lines.append(f"| {label} | {badge_md(f'habit_{c}.json', label)} |")
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
        results.append({"key": path.stem, "name": path.stem.replace("_", " ").title(), "done": done, "total": total})
    return results


def write_syllabus_badges(progress):
    for p in progress:
        pct = round(100 * p["done"] / p["total"]) if p["total"] else None
        msg = f"{pct}% ({p['done']}/{p['total']})" if p["total"] else "no checklist"
        write_badge(f"syllabus_{p['key']}.json", p["name"], msg, pct_color(pct) if p["total"] else "lightgrey")


def render_syllabus_block(progress):
    if not progress:
        return "_No syllabus files found in `syllabus/`._"
    lines = ["| Track | Progress |", "|---|---|"]
    for p in progress:
        badge_filename = f"syllabus_{p['key']}.json"
        lines.append(f"| {p['name']} | {badge_md(badge_filename, p['name'])} |")
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
    write_habit_badges(data, stats)
    stats_block = render_stats_block(data, stats)

    progress = compute_syllabus_progress()
    write_syllabus_badges(progress)
    syllabus_block = render_syllabus_block(progress)

    text = README_PATH.read_text()
    text = replace_block(text, STATS_START, STATS_END, stats_block)
    text = replace_block(text, SYL_START, SYL_END, syllabus_block)
    README_PATH.write_text(text)

    print("README and badges updated.\n")
    print(stats_block)
    print()
    print(syllabus_block)


if __name__ == "__main__":
    main()
