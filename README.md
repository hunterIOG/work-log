# work-log

Private daily log of NomBot work: [`LOGGER.md`](LOGGER.md).

Every night at 11:55pm, launchd runs `daily_log.py`. It reads that day's NomBot Claude Code chats (`~/.claude/projects/-Users-hunterzhang-Desktop-NomBot*`) and commits in `NomBot` and `generosity-data`. It asks `claude -p` for a summary, writes the day's entry (newest first) and pushes.

```bash
python3 daily_log.py                # today
python3 daily_log.py 2026-10-06     # backfill or redo a day (replaces its entry)
python3 daily_log.py --dry-run      # print only
launchctl start com.hunterzhang.worklog   # run the nightly job now
tail ~/Library/Logs/worklog.log
```

Install: `cp com.hunterzhang.worklog.plist ~/Library/LaunchAgents/ && launchctl load ~/Library/LaunchAgents/com.hunterzhang.worklog.plist`

Hours: add the day to `hours.json` (e.g. `"2026-10-08": 3`) and the entry shows them. Without it, the entry shows an estimate of active Claude Code time (gaps of 15 min or less between messages).
