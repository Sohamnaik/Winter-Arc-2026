"""
Interactive daily logger for Winter Arc 2026.

Run:
    python scripts/log_day.py

Each habit can be logged as:
  y - done            (+1)
  n - missed           (-1)
  s - skip / not a "today" habit (no score change, e.g. Relationships
      on a day you're not actively working on it)

Then run scripts/update_readme.py (or push - the GitHub Action does
this for you) to refresh the stats in README.md.
"""

import json
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "tracker.json"

CATEGORY_LABELS = {
    "wake_before_8": "Wake before 8 AM",
    "exam_prep": "Exam Prep (NET-JRF / GATE / math)",
    "programming": "Programming / Open Source",
    "fitness_diet": "Fitness & Clean Diet",
    "relationships": "Relationships & Connection",
}


def ask_tri(prompt):
    while True:
        ans = input(f"{prompt} (y/n/s=skip): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        if ans in ("s", "skip"):
            return None
        print("  please answer y, n, or s")


def main():
    with open(DATA_PATH) as f:
        data = json.load(f)

    today = datetime.date.today().isoformat()
    date_str = input(f"Date [{today}]: ").strip() or today

    existing = data["days"].get(date_str, {})
    if existing:
        overwrite = input(
            f"{date_str} already has an entry. Merge new answers into it? (y/n): "
        ).strip().lower()
        if overwrite not in ("y", "yes"):
            print("Cancelled.")
            return

    entry = dict(existing)
    for c in data["categories"]:
        result = ask_tri(CATEGORY_LABELS.get(c, c))
        if result is None:
            entry.pop(c, None)  # skipped -> no key -> neutral, not scored
        else:
            entry[c] = result

    note = input("Note (optional, press enter to skip): ").strip()
    if note:
        entry["note"] = note
    else:
        entry.pop("note", None)

    data["days"][date_str] = entry

    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"\nLogged {date_str}.")
    print("Now run: python scripts/update_readme.py")


if __name__ == "__main__":
    main()
