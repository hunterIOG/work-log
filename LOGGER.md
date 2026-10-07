# Work log

Daily summary of NomBot and GrantRadar work, written each night from Claude Code chats and git commits.

## 2026-10-07 (Wednesday)

*Hours worked: 2h · 8 commits · 38 messages*

**Summary:** NomBot search hit the 90% relevance goal (91%), Research Buddy dropped to 1 unsupported claim in 401, and several UI changes shipped.

**Done**
- **Search eval** reached 91% relevant (was 81%, 50% and 35% at first baseline). 38 of 50 questions meet the goal, up from 32.
- **Embeddings** finished: 50,971 filings embedded. 47,595 orgs now have filing text, about 4× before.
- **City filter, cause boost and 4× filing text** raised relevance from 50% to 81% before the Appalachia work.
- **Appalachia filter** built on a new `zip_regions` table (ZIP → county, ARC flag; 420 ARC counties matched) in `generosity-data`. Louisville and Richmond VA come out 0% Appalachian, and Knoxville and Pikeville 100%.
- **Weaker matches** scoring under 50 now fold behind "Show N weaker matches". One combined notice replaces two, and no-strong-match questions list the closest orgs.
- **Research Buddy eval** built (30 questions, claims checked against cited filings). The first run had 12 problems in 406 claims (97% supported). After the prompt fix, 1 problem in 401 claims, and 29 of 30 answers were clean.
- **Filter changes** now show new results in about 0.4s instead of about 6s. Scores re-sort when they arrive.
- **Loading card** is centered over a frosted veil. Sources now open beside the org inside its popover as a split view.
- **Research Buddy history** is saved per search in the browser, with a History button and New chat.
- **Popover close** now works with one × (source half first, then the popover). A bug that left closed popovers and panels on screen is fixed.
- **Smaller fixes:** tooltip overlapping the next row's score, the duplicate React key error, and the NomBot logo as the tab icon.
- **Docs** updated: both READMEs, with the progress checklist, web app map and both evals (`82273f7`).
- **Work log:** private `work-log` repo with a nightly launchd job. The dry run worked, and backfill of 10/06 and 10/07 was in progress.

**Decisions**
- **Appalachia** is filtered at county level via the ARC list, since the 13-state expansion was right but too broad.
- **Typo handling** is left unchanged. The parser already reads misspellings correctly, and the low score was a few-true-matches problem.
- **Weaker matches** are hidden but counted, and the eval reports questions with no strong match so hiding can't inflate the score.
- **Work log** goes to a private repo rather than the org repo, to avoid publishing chat summaries.

**Next**
- **Research Buddy eval:** the goal is zero unsupported claims, and 1 remains.
- **Search speed:** median search is about 14s against the under-2s goal.
- **Cloud launch:** switch to OpenAI embeddings and deploy by Oct 19–25.

## 2026-10-06 (Tuesday)

*Hours worked: 4h · 37 commits · 44 messages*

**Summary:** Built filters, votes, eval, relevance scores, SOI viewer, side panels and Research Buddy; the eval baseline of 35% rose to 50%.

**Done**
- **Eval baseline:** 50-question harness scored 35% relevant against the 90% goal, with only 5 of 50 questions reaching 90%. After relevance ranking, the city filter and the SOI work, the report showed 50%.
- **Votes:** 👍/👎 on each result, saved to a new `feedback` table (migration `004`).
- **Filter chips:** place, budget and cause are editable without retyping.
- **Relevance score:** each result gets a 0–100 Claude score with a hover reason, sorted highest first, and the CSV export includes the same columns.
- **City filter:** "Homeless shelters in Louisville" went from 5 weak results to 341 Louisville orgs.
- **Streaming:** results appear at 2.0s instead of 8.5s, then re-sort once the scores arrive.
- **Filing text:** coverage rose from 12,354 to 50,971 filings. The embeddings are still running, about 70 more minutes.
- **SOI viewer:** keeps 54,590 full records and 499 field definitions (migration `005`). Negative amounts now display as −$5K instead of "$-234171".
- **Side panel:** source viewers open in a right panel, in a compact field and value layout.
- **Research Buddy:** v0 gives cited answers in a docked chat panel opened from a floating button. Citations open the org in a modal.
- **UI:** the left sidebar has Starred and Recents with a current-page highlight, plus an Apple-style restyle and a centered home composer. Fixes cover the hydration error, the Recents order, the back-to-results flash, the loading overlap and the search suggestions.
- **Commits:** eight pushes to `NomBot`, plus two to `generosity-data`.

**Decisions**
- **Priorities:** build search quality and speed features ahead of more UI polish.
- **Guessed causes** now boost ranking instead of filtering, because the hard filter hid Louisville's best homeless-services org.
- **Buddy placement:** a docked panel replaced the inline search bar, which competed with the main one.
- **Back to results** uses browser history, so results restore instantly.

**Next**
- **Re-run the eval** after the embeddings finish and report the new score.
- **Commit the NomBot favicon**, which is built but not yet pushed.
- **Cloud deploy** is scheduled for Oct 19–25.

