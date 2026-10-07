# work-log

Private daily log of NomBot and GrantRadar work: [`LOGGER.md`](LOGGER.md).

Every night at 11:55pm, launchd runs `daily_log.py`. It reads that day's Claude Code chats from any NomBot or GrantRadar folder (`~/.claude/projects/*nombot*`, `*grantradar*`) and commits in `NomBot` and `generosity-data`. It asks `claude -p` for a summary, writes the day's entry (newest first) and pushes.

```bash
python3 daily_log.py                # today
python3 daily_log.py 2026-10-06     # backfill or redo a day (replaces its entry)
python3 daily_log.py --dry-run      # print only
launchctl start com.hunterzhang.worklog   # run the nightly job now
tail ~/Library/Logs/worklog.log
```

Install: `cp com.hunterzhang.worklog.plist ~/Library/LaunchAgents/ && launchctl load ~/Library/LaunchAgents/com.hunterzhang.worklog.plist`

## Hours

- **Start:** your first message to Claude in a NomBot chat that day.
- **End:** when you tell Claude you're done for the day, it runs `python3 daily_log.py --end` (add `--break=30` to take a break off).
- **Hours** = start → end, rounded to the nearest 15 min. Saved in `clock.json` and `hours.json`; the entry shows e.g. `Hours worked: 3.5h (8:20am–11:50am)`.
- **Manual:** add `"2026-10-08": 3` to `hours.json`. No hours → the entry shows an estimate of active Claude Code time.
