# Work log

Daily summary of NomBot and GrantRadar work, written each night from Claude Code chats and git commits.

## 2026-10-08 (Thursday)

*Hours worked: 5.25h (3:00pm–8:16pm) · 24 commits · 113 messages*

**Summary:** Shipped NomBot's 990-based diligence and Census gap map and GrantRadar's landscape panel and funder-view check, and set up the Figma, Supabase and PostHog workspaces for Keith.

**Done**
- [NomBot] **Source panel** now has one panel with a tab per source, so it closes in one click. Before, each source added a history step and needed two closes.
- [NomBot] **Result rows** were cut to name, one grey facts line, a one-line "Mission:" and finance tags. Source links show only on hover. Funders and "Not yet funded" lists are one line each, with details on hover.
- [NomBot] **FLAG diligence data:** new `filing_flag` table loaded from 990 XML (50,971 filings in 53 s). It covers prior-year figures, board independence, audit, insider flags, leadership and pay. It found 3,686 boards under half independent and 651 filers reporting insider loans.
- [NomBot] **Org page** now has year-over-year figures, a leadership and governance section, and colored financial-health signals. Government grants are split out (Manna Meal: 41% government) and the spending split is shown (87% programs, 7% admin, 6% fundraising). Officer titles are cleaned, so "CHIEF EXEC O" reads "Chief Executive Officer".
- [NomBot] **Finances tab** has Growing, Shrinking, Deficit, Thin reserves and Donor-reliant rows (e.g. Donor-reliant 77 of 150). Click a row to list the organizations behind it. Result tags, the tab and the AI overview share one rule set, now based on the 990 XML.
- [NomBot] **Gaps map** uses Census county poverty for 3,144 counties (migrations 010 and 011). The map shows orange for high poverty with no match and green for a match. The county list highlights on hover, and the "% poverty" popover shows people count and the U.S. rate. Clicking a county in the Organizations view lists its orgs.
- [NomBot] **Gap cutoff** is now relative to the map, so Ohio uses 15.4% and shows 8 of 22 counties as gaps. Gaps are limited to the 5 loaded states, which changed the headline from 68 of 83 to 50 of 65.
- [GrantRadar] **Landscape panel** beside the matches has Overview, Breakdown, Peers, Ask (grant ranges by budget) and Calendar (deadline months). Funder names in the overview are now full names.
- [GrantRadar] **"How funders will see you"** at `/grants/check` runs the shared `lib/flag.ts` rules on your own 990. It lists concerns with what to prepare. Foundations such as Kroger get an explanation, since they file a 990-PF.
- [GrantRadar] **Standalone cleanup:** no NomBot toggle, pages titled GrantRadar, `/` redirects to `/grants`, sidebar header fixed on one row, radar tab icon, and a quieter funder-row right column. The architecture diagram was redrawn and the README updated.
- [Admin] **Invoice and software setup:** invoice re-billed to Protocol Z, Inc. (17.75 hrs × $60 = $1,065, with 10/07 at 8.75 hrs). I created the Figma team, Supabase org and PostHog org and invited Keith. I rewrote the instructions doc for Vercel, Figma, Supabase and PostHog and added a cost summary. Progress trackers were updated (NomBot Issue #1, new GrantRadar Issue #2).

**Decisions**
- [Admin] **Vercel:** Keith creates the team on paid Pro, not the trial. A trial allows only one Owner, so Hunter could not be made Owner until after the trial.
- [NomBot] **Diligence statuses** come from fixed, visible rules with no AI verdict, because the slides showed two AI tools rating the same filing differently.
- [NomBot] **Weak/Medium/Strong label** and the "How this is rated" section were removed to cut clutter. The colored signals stay.

**Next**
- [Admin] **Invites:** Keith accepts the Supabase invite by Oct 9, PostHog by Oct 11, and Figma, then Hunter makes him Admin. Keith creates the Vercel team.
- [NomBot] **FLAG items not built:** questions to ask, pay benchmark, big-donor concentration (Schedule A), revocation check.
- [GrantRadar] **Recipient linking** is at 51%, against a 70% goal.

## 2026-10-07 (Wednesday)

*Hours worked: 8.75h (8:20am–4:58pm) · 43 commits · 95 messages*

**Summary:** Search hit 91% relevant and Research Buddy cut to 1 unsupported claim in 401. GrantRadar was built from scratch, and NomBot got the landscape analysis panel and a results-page redesign.

**Done**
- [NomBot] **Search relevance** rose from 81% to 91% (goal 90%), with 38 of 50 questions at goal. The Appalachia county filter (ZIP→county table, 420 ARC counties) and folded weaker matches drove it.
- [NomBot] **Research Buddy eval** went from 12 problems in 406 claims to 1 in 401. 29 of 30 answers are fully supported after a prompt tightening.
- [NomBot] **Results page** redesigned: full-width fixed search and filters, results on the left (~60%) and a tabbed analysis panel on the right (~40%). Each side scrolls on its own, and macOS scrollbar clipping is fixed.
- [NomBot] **Analysis panel** combines AI overview, breakdown, county map, themes and funders into one hover-only tabbed card. Citations show an instant hover card.
- [NomBot] **Staff and volunteer counts** from Form 990 Part I are on org pages for 50,971 filings. 33,331 orgs report staff and 7,057 are all-volunteer.
- [NomBot] **Compare** page (2–4 orgs side by side) has a back link and an "Add one more" placeholder. **Starred folders** and a "← Back to Starred" link were added.
- [NomBot] **UI**: centered loading card over a frosted veil, sources opening beside the org in its popover, and Research Buddy history. Filter changes now show results in ~0.4s instead of ~6s, and a stuck-overlay bug is fixed.
- [GrantRadar] **Built end to end** on `/grants`: mission → ranked foundations → funder sheet with a streamed, cited "Why this funder?". Data is 8,030 foundations and 102,725 grants (5 states, 2025 990-PFs), with 51% of in-state grants linked to recipients.
- [GrantRadar] **"Groups like yours" matching**: Claude scores each candidate grantee ≥70 on similarity of work, so unrelated funders (e.g. a health foundation for animal rescue) drop out. Closeness dots show match strength.
- [GrantRadar] **Feedback features built**: grant-type labels (unrestricted / project / policy; 72% labelled, 34 of 36 spot-checked correct) and Research Buddy on `/grants`.
- [GrantRadar] **UI polish**: shorter copy, SF-style icons, clearer row hierarchy, Starred funders and Recent missions, and a "Gives in" menu listing all states.
- [Admin] **Work-log and docs**: private work-log repo with a nightly job and a start/end hours clock, covering NomBot and GrantRadar. The NomBot README, architecture diagram and real screenshots were updated, and a CLAUDE.md rule keeps the README in sync with every commit. The IoG demo feedback was added to both READMEs. An invoice including the fellowship sessions was drafted.

**Decisions**
- [NomBot] **Strong matches only** are scored in the eval, so folding weaker results can't inflate the 91%.
- [GrantRadar] **Precision over coverage** for grantee linking, since a wrong link credits the wrong charity.
- [Admin] **README updated by Claude per commit** rather than by an autonomous git hook, which the safety check blocked.
- [Admin] **Private repo** for the work log, so chat summaries aren't visible to the org.

**Next**
- [NomBot] **Cloud launch** (Oct 19–25): Supabase + Vercel, all 50 states.
- [GrantRadar] **Merge NomBot into GrantRadar** and resolve the Buddy component conflicts.
- [Admin] **Competitor scan and user testing** with the two audiences, per the demo feedback.

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

