<div align="center">

# 🌑 Winter Arc 2026

### *"I refuse to be bitter; don't be bitter towards life."*

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)
![Built in Public](https://img.shields.io/badge/built-in%20public-orange)
![Sept 1 → Dec 31](https://img.shields.io/badge/Sept%201%20→%20Dec%2031%2C%202026-122%20days-8A2BE2)

</div>

Repo: [github.com/Sohamnaik/Winter-Arc-2026](https://github.com/Sohamnaik/Winter-Arc-2026)

---

## 📋 The Arc

Five daily habits. Do it, +1. Miss it, −1. Not a "today" habit? Skip it — no score change.

| # | Habit | What it means |
|---|---|---|
| 1 | **Wake before 8 AM** | No exceptions, no snoozing past it |
| 2 | **Exam prep** | UGC-CSIR-NET-JRF (Dec 2026), GATE 2027 Biotech & Life Sciences (Feb 2027), DBT-BET (2026-27) — math study folds in here too |
| 3 | **Programming** | Deliberate practice + open-source contributions, not just tutorials |
| 4 | **Fitness & clean diet** | Train regularly, no junk, no added sugar |
| 5 | **Relationships** | Actively build and maintain the connections that matter |

Math isn't a forced daily checkbox — it's real study, tracked as a topic checklist in `syllabus/mathematics.md` instead. Same for the exam syllabus itself and the programming roadmap — see **Syllabus Progress** below.

This isn't a vibe, it's a system — the habit stack James Clear talks about in *Atomic Habits*: small daily reps, tracked honestly, compounding for 122 days.

---

## 📊 Player Status

<!-- STATS:START -->
![Score](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/score.json) ![Streak](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/streak.json) ![Perfect Days](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/perfect_days.json) ![Days Logged](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/days_logged.json) ![Arc Progress](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/arc_progress.json)

| Habit | Consistency |
|---|---|
| Wake before 8 AM | ![Wake before 8 AM](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/habit_wake_before_8.json) |
| Exam Prep (NET-JRF / GATE / math) | ![Exam Prep (NET-JRF / GATE / math)](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/habit_exam_prep.json) |
| Programming / Open Source | ![Programming / Open Source](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/habit_programming.json) |
| Fitness & Clean Diet | ![Fitness & Clean Diet](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/habit_fitness_diet.json) |
| Relationships & Connection | ![Relationships & Connection](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/habit_relationships.json) |

_Last updated: 2026-09-01_
<!-- STATS:END -->

---

## 🧬 Syllabus Progress

<!-- SYLLABUS:START -->
| Track | Progress |
|---|---|
| Exam Prep | ![Exam Prep](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/syllabus_exam_prep.json) |
| Mathematics | ![Mathematics](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/syllabus_mathematics.json) |
| Programming | ![Programming](https://raw.githubusercontent.com/Sohamnaik/Winter-Arc-2026/main/data/badges/syllabus_programming.json) |

_Check off topics directly in the `syllabus/*.md` files (`- [ ]` -> `- [x]`) as you cover them._
<!-- SYLLABUS:END -->

Checklists live in `syllabus/`:
- `syllabus/exam_prep.md` — CSIR-NET Life Sciences, GATE BT/XL, DBT-BET
- `syllabus/programming.md` — roadmap + open-source contribution log
- `syllabus/mathematics.md` — the math rebuild, topic by topic

---

## ⚙️ How This Works

1. **Log the day.** Run:
   ```bash
   python scripts/log_day.py
   ```
   It asks y/n/skip for each of the 5 habits and saves it to `data/tracker.json` under today's date. Skip a habit that isn't relevant today (e.g. Relationships) and it simply doesn't count for or against you.

2. **Check off syllabus topics as you actually cover them** in the `syllabus/*.md` files (`- [ ]` → `- [x]`).

3. **Update the README.** Run:
   ```bash
   python scripts/update_readme.py
   ```
   This recalculates your habit score, streak, perfect days, per-habit consistency, and syllabus completion, regenerates the colored badges in `data/badges/`, and rewrites the marked blocks above.

4. **Automate it.** `.github/workflows/update-readme.yml` runs step 3 automatically and commits the refreshed README + badges whenever you push a change to `data/tracker.json` or any `syllabus/*.md` file.

5. **Commit daily.** The commit history *is* the "built in public" part — every green square is a day you showed up.

> Badges pull live from `data/badges/*.json` on GitHub's `main` branch via shields.io, so they update automatically after every push — no need to touch them by hand. They may lag a minute behind a fresh push while GitHub's CDN catches up.

---

## 🎯 Scoring Rules

- Each of the 5 daily habits is worth **+1** if done, **−1** if missed, **0** (not counted) if skipped as not applicable that day.
- **Perfect day** = every habit you logged that day (i.e. didn't skip) was a +1.
- **Current streak** = consecutive most recent logged days where you completed more than you missed.
- Score can go negative — that's intentional. It's supposed to sting a little.
- Syllabus progress is separate and cumulative — it only ever goes up as you check off topics.

---

<div align="center">

### 122 days. No bitterness. Just the reps.

</div>
