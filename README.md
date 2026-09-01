# Winter Arc 2026 🔥

> "I refuse to be bitter; don't be bitter towards life."

**September 1, 2026 → December 31, 2026** · 122 days · built and tracked in public.

---

## The Arc

Five daily habits. Do it, +1. Miss it, −1. Not a "today" habit? Skip it — no score change.

| # | Habit | What it means |
|---|---|---|
| 1 | **Wake before 8 AM** | No exceptions, no snoozing past it |
| 2 | **Exam prep** | UGC-CSIR-NET-JRF (Dec 2026), GATE 2027 Biotech & Life Sciences (Feb 2027), DBT-BET (2026-27) — math study folds in here too |
| 3 | **Programming** | Deliberate practice + open-source contributions, not just tutorials |
| 4 | **Fitness & clean diet** | Train regularly, no junk, no added sugar |
| 5 | **Relationships** | Maintain the connections that matter |

---

## Player status 

<!-- STATS:START -->
**Score: -1**  |  Days logged: 1/122  |  Perfect days: 0  |  Current streak: 0 🔥

Arc progress: `░░░░░░░░░░░░░░░░░░░░` 1% (1/122 days elapsed)

| Habit | Done | Missed | Consistency |
|---|---|---|---|
| Wake before 8 AM | 0 | 1 | `░░░░░░░░░░░░` 0% |
| Exam Prep (NET-JRF / GATE / math) | 0 | 0 | `░░░░░░░░░░░░` 0% |
| Programming / Open Source | 0 | 0 | `░░░░░░░░░░░░` 0% |
| Fitness & Clean Diet | 0 | 0 | `░░░░░░░░░░░░` 0% |
| Relationships & Connection | 0 | 0 | `░░░░░░░░░░░░` 0% |

<!-- STATS:END -->

---

## Syllabus Progress

<!-- SYLLABUS:START -->
| Track | Topics done | Total | Progress |
|---|---|---|---|
| Exam Prep | 0 | 36 | `░░░░░░░░░░░░` 0% |
| Mathematics | 0 | 22 | `░░░░░░░░░░░░` 0% |
| Programming | 0 | 15 | `░░░░░░░░░░░░` 0% |

<!-- SYLLABUS:END -->

Checklists live in `syllabus/`:
- `syllabus/exam_prep.md` — CSIR-NET Life Sciences, GATE BT/XL, DBT-BET
- `syllabus/programming.md` — roadmap + open-source contribution log
- `syllabus/mathematics.md` — the math rebuild, topic by topic

---

## How this works

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
   This recalculates your habit score, streak, perfect days, per-habit consistency, and syllabus completion, then rewrites the marked blocks above.

4. **Automate it.** `.github/workflows/update-readme.yml` runs step 3 automatically and commits the refreshed README whenever you push a change to `data/tracker.json` or any `syllabus/*.md` file.

5. **Commit daily.** The commit history *is* the "built in public" part — every green square is a day you showed up.

---

## Scoring rules

- Each of the 5 daily habits is worth **+1** if done, **−1** if missed, **0** (not counted) if skipped as not applicable that day.
- **Perfect day** = every habit you logged that day (i.e. didn't skip) was a +1.
- **Current streak** = consecutive most recent logged days where you completed more than you missed.
- Score can go negative — that's intentional. It's supposed to sting a little.
- Syllabus progress is separate and cumulative — it only ever goes up as you check off topics.

---

## Why

I read this quote on Instagram that said, "Somewhere in your 20s, you'll get the opportunity to rebuild your life after a negative loop, heal from what broke you, live in your own space, reconnect with your discipline, and learn to love yourself again. It is very important that you see that journey through". This repo represents that journey of mine.
