#!/usr/bin/env python3
"""Write one day's entry in LOGGER.md from that day's NomBot, GrantRadar and imnet Claude Code chats and git commits.

  python3 daily_log.py                 # today (local time), commit and push
  python3 daily_log.py 2026-10-06      # a given day
  python3 daily_log.py --dry-run       # print the entry, change nothing
  python3 daily_log.py --end           # end today: hours = first message today -> now; log and push
  python3 daily_log.py --end --break=30   # same, minus a 30-minute break

Runs nightly via launchd (com.hunterzhang.worklog.plist). Re-running a day replaces its entry.
"""
import datetime as dt
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "LOGGER.md")
HOURS = os.path.join(HERE, "hours.json")  # {"2026-10-06": 4}: hours you report; shown instead of the estimate
CLOCK = os.path.join(HERE, "clock.json")  # {"2026-10-08": {"start": "09:12", "end": "12:40"}}: written by --end
# Chats in any NomBot, GrantRadar or imnet folder (imnet lives under ~/Desktop/IOG)
PROJECTS = os.path.expanduser("~/.claude/projects")
MATCH = re.compile(r"nombot|grantradar|imnet|-IOG(-|$)", re.I)
REPOS = [os.path.expanduser(p) for p in ("~/Desktop/NomBot", "~/Desktop/generosity-data", "~/Desktop/IOG/imnet")]
IDLE = 15 * 60          # gaps longer than this don't count as active time
MSG_CAP, TOTAL_CAP = 1500, 120_000
HEADER = "# Work log\n\nDaily summary of NomBot, GrantRadar and imnet work, written each night from Claude Code chats and git commits.\n"

PROMPT = """Below are one day's Claude Code chat messages (user and assistant) and git commits for the NomBot, GrantRadar and imnet projects (Institute on Generosity AI Fellowship).
Write a work-log entry in Markdown for {day}. Output ONLY these sections, no title, no preamble:

**Summary:** one sentence.

**Done**
- 3-12 bullets of concrete things built, fixed, measured or decided (lead with the result, include numbers such as eval scores). Start each bullet with its project in brackets: [NomBot], [GrantRadar], [imnet] (Impact Network, "LinkedIn for generosity") or [Admin] (invoices, fellowship sessions, tooling).

**Decisions**
- 0-4 bullets: choices made and why. Omit the section if none.

**Next**
- 0-3 bullets: open items. Omit the section if none.

Rules: short declarative bullets, bold the key noun of each bullet. Use only what the messages show.
Never include secrets, API keys, tokens, passwords, home addresses, phone numbers or email addresses.

Commits:
{commits}

Messages:
{messages}"""


def local_day(ts: str) -> tuple[dt.date, dt.datetime]:
    t = dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone()
    return t.date(), t


def text_of(content) -> str:
    if isinstance(content, str):
        return content
    return "\n".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text")


def clean(s: str) -> str:
    s = re.sub(r"<system-reminder>.*?</system-reminder>", "", s, flags=re.S)
    s = re.sub(r"<(local-command-[a-z]+|command-[a-z]+)>.*?</\1>", "", s, flags=re.S)
    return s.strip()


def collect(day: dt.date):
    msgs, times = [], []
    for path in (p for p in glob.glob(f"{PROJECTS}/*/*.jsonl") if MATCH.search(os.path.basename(os.path.dirname(p)))):
        with open(path) as f:
            for line in f:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("type") not in ("user", "assistant") or not e.get("timestamp"):
                    continue
                d, t = local_day(e["timestamp"])
                if d != day:
                    continue
                times.append(t)
                if e.get("isMeta") or e.get("isCompactSummary"):
                    continue
                txt = clean(text_of((e.get("message") or {}).get("content", "")))
                if txt:
                    msgs.append((t, e["type"], txt[:MSG_CAP]))
    msgs.sort(key=lambda m: m[0])
    times.sort()
    active = sum(min((b - a).total_seconds(), IDLE) for a, b in zip(times, times[1:]) if (b - a).total_seconds() <= IDLE)
    return msgs, active


def commits(day: dt.date) -> list[str]:
    out = []
    for repo in REPOS:
        if not os.path.isdir(repo):
            continue
        r = subprocess.run(["git", "-C", repo, "log", "--all", "--no-merges", f"--since={day} 00:00", f"--until={day + dt.timedelta(days=1)} 00:00",
                            "--format=%h %s"], capture_output=True, text=True)
        out += [f"{os.path.basename(repo)} {l}" for l in r.stdout.splitlines()]
    return out


def summarize(day: dt.date, msgs, cms) -> str:
    body = "\n\n".join(f"[{t:%H:%M}] {role.upper()}: {txt}" for t, role, txt in msgs)
    if len(body) > TOTAL_CAP:  # keep the start and the end of the day
        body = body[: TOTAL_CAP // 2] + "\n\n[…middle of the day omitted…]\n\n" + body[-TOTAL_CAP // 2:]
    prompt = PROMPT.format(day=day, commits="\n".join(cms) or "(none)", messages=body)
    r = subprocess.run(["claude", "-p", "--model", "sonnet"], input=prompt, capture_output=True, text=True, cwd=HERE, timeout=600)
    if r.returncode != 0 or not r.stdout.strip():
        raise SystemExit(f"claude -p failed: {r.stderr.strip()[:500]}")
    return r.stdout.strip()


def write_entry(day: dt.date, entry: str):
    text = open(LOG).read() if os.path.exists(LOG) else HEADER
    sections = re.split(r"(?m)^(?=## \d{4}-\d{2}-\d{2})", text)
    head, days = sections[0], {s[3:13]: s for s in sections[1:]}
    days[str(day)] = entry.rstrip() + "\n\n"
    with open(LOG, "w") as f:
        f.write(head.rstrip() + "\n\n" + "".join(days[k] for k in sorted(days, reverse=True)))


def git(*args):
    return subprocess.run(["git", "-C", HERE, *args], capture_output=True, text=True)


def load(path) -> dict:
    return json.load(open(path)) if os.path.exists(path) else {}


def save(path, data: dict):
    with open(path, "w") as f:
        json.dump(dict(sorted(data.items())), f, indent=2)
        f.write("\n")


# Hours = first message of the day -> the moment you end the day, rounded to the nearest quarter hour.
def clock_out(day: dt.date, msgs):
    if day != dt.date.today():
        raise SystemExit("--end only works for today")
    starts = [t for t, role, _ in msgs if role == "user"]
    if not starts:
        raise SystemExit("No messages today: nothing to clock")
    start, end = starts[0], dt.datetime.now().astimezone()
    brk = next((int(a.split("=")[1]) for a in sys.argv if a.startswith("--break=")), 0)  # minutes off the clock
    hours = round(((end - start).total_seconds() - brk * 60) / 900) / 4
    save(CLOCK, {**load(CLOCK), str(day): {"start": f"{start:%-I:%M%p}".lower(), "end": f"{end:%-I:%M%p}".lower()}})
    save(HOURS, {**load(HOURS), str(day): hours})
    print(f"{day}: {start:%-I:%M%p} -> {end:%-I:%M%p}" + (f" minus {brk} min break" if brk else "") + f" = {hours:g}h")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    day = dt.date.fromisoformat(args[0]) if args else dt.date.today()
    msgs, active = collect(day)
    cms = commits(day)
    if not msgs and not cms:
        print(f"{day}: no NomBot, GrantRadar or imnet activity; nothing logged")
        return
    if "--end" in sys.argv:
        clock_out(day, msgs)
    reported = load(HOURS).get(str(day))
    span = load(CLOCK).get(str(day))
    h, m = divmod(round(active / 60), 60)
    time = (f"Hours worked: {reported:g}h" + (f" ({span['start']}–{span['end']})" if span else "")) if reported is not None \
        else f"Active in Claude Code: ~{h}h {m:02d}m (estimate)"
    meta = f"*{time} · {len(cms)} commits · {sum(1 for _, r, _ in msgs if r == 'user')} messages*"
    entry = f"## {day} ({day:%A})\n\n{meta}\n\n{summarize(day, msgs, cms)}\n"
    if dry:
        print(entry)
        return
    write_entry(day, entry)
    git("pull", "--rebase", "-q")
    git("add", "LOGGER.md", "hours.json", "clock.json")
    if git("diff", "--cached", "--quiet").returncode == 0:
        print(f"{day}: no change")
        return
    git("commit", "-q", "-m", f"Log {day}")
    r = git("push", "-q", "origin", "HEAD:main")
    print(f"{day}: logged" + ("" if r.returncode == 0 else f"; push failed: {r.stderr.strip()}"))


if __name__ == "__main__":
    main()
