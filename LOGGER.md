# Work log

Daily summary of NomBot, GrantRadar and imnet work, written each night from Claude Code chats and git commits.

## 2026-10-16 (Friday)

*Hours worked: 7.75h (8:49am–11:00pm, 437 min inactive removed) · 38 commits · 126 messages*

**Meeting:** 45 min with Una Osili (11:45–12:30)

**Summary:** Research answers became a ChatGPT-style chat on a faster, Google-style NomBot that is self-hosted behind a partner API, and imnet gained friends, notable-giver and trust features.

**Done**
- **[NomBot] Search speed:** full page dropped from 14–25 s to 5.3–8.1 s, with benchmark relevance unchanged at 69%.
  - Candidates are capped at 3,000, a half-precision HNSW index replaces the full-size one, and one cached search feeds the page.
  - A 15–20 s Appalachia slowdown was a ZIP type mismatch, now about 5 s.
  - Postgres `shared_buffers` went from 128 MB to 4 GB.
- **[NomBot] Research answers:** a question router and answer engine give a direct card with fixed, tested queries.
  - Questions open in `/research/ask`, with follow-up threads and on-topic suggestions (`npm run test:followups`, 8 of 8 pass).
  - The page was redesigned ChatGPT-style.
  - Answers are exposed as `/v1/answer` and an MCP tool.
- **[NomBot] Research layer:** the database gained a pre-summarized grants table (about 950K rows instead of 4.9M).
  - It also gained plain-English names for 681 category codes and a data dictionary.
  - 30 of 32 test questions now get an on-target answer, up from 19.
  - Typical database time is 116 ms, down from 173 ms.
- **[NomBot] Search UI:** results and side panel were redesigned in Google style, with the diagram first in the overview.
  - A visual AI overview and first-slide export (PNG and PPTX) were added.
  - Report and "Ask about this finding" became right-side panels.
  - Insights was renamed Research, with a dedicated page per finding and short headlines with bullets for all 32 findings.
- **[NomBot] Partner API:** per-key Bearer auth, `/api/v1` search, org and research endpoints, remote MCP at `/mcp`, and public docs and OpenAPI.
  - Keys are hashed, rate-limited at 60/min and revocable.
  - No endpoint calls Claude.
- **[NomBot] Self-hosting:** NomBot runs on the MacBook as always-on services with an optional `SITE_PASSWORD` gate, nightly backups and a fixed Tailscale Funnel address.
  - Postgres restart briefly took the live site down (about 1 minute), then recovered.
- **[NomBot] Fixed:** the home prompt loading screen vanished because the flipping headline remounted the clicked chip.
- **[GrantRadar] Fixed:** the same ZIP `char(5)` compare skipped the index in `lib/search.ts` (`072a102`).
- **[imnet] Friends and notable givers:** added a Friends tab, friends' experiences (hours and dollars), ways to get involved, and opt-in notable givers.
  - Demo public figures are fictional.
  - Cover photos were added for South Bay orgs.
  - Tests passed (166 unit, 86 e2e).
- **[imnet] Trust and onboarding (PR #16):** added "Who can message me", a three-step first-week path, Report a person, a "What Verified means" page and an AI-assisted media label.
  - 90 of 90 e2e tests pass.
- **[generosity-data] Cause labels:** climate and women and girls labels graded at 95%+, with method docs.
  - Migrations 031–040 added API keys, a weekly Parquet snapshot (378 MB, about 23 s) and the research layer.
- **[Admin] Una meeting:** 45-minute meeting with Una logged. Her feedback shaped the cause labels, the first-slide export, the visual overview and imnet's personal-discovery features.

**Decisions**
- **[NomBot] MacBook hosting** instead of Supabase Large (about $129/month), at $0–5 per month.
- **[NomBot] Partner access** is API plus MCP and weekly exports, with no direct database sharing, so the personal Mac stays private.
- **[NomBot] Scoring models:** kept Sonnet for relevance scoring and Opus for question reading, because Haiku cost 5–7 points of relevance.
- **[imnet] Public figures** are fictional demos, opt-in and admin-badged, since real people can't be shown without consent.

**Next**
- **[NomBot]** Review and commit the background agent's data expansion (Schedule I, Census ACS, USAspending) and the redrawn architecture diagram.
- **[NomBot]** Decide whether to bring spending, staff and volunteers back into the result lines.
- **[Admin]** Create per-partner API keys and revoke the keys pasted in chat.

## 2026-10-15 (Thursday)

*Hours worked: 5.75h (9:12am–11:36pm, 558 min inactive removed) · 0 commits · 98 messages*

**Summary:** Raised the grant link rate from 57.6% to about 64% in NomBot/GrantRadar, and shipped donations, communities, messaging and maps plus an IRS-verification feature in imnet.

**Done**
- [GrantRadar] **Grant link rate** rose from 57.6% to 64.0% of all grants (65.2% of those that can link). Dollars linked rose from about 47% to 57.4%.
- [GrantRadar] **"Doing business as" names** scored 97% and were applied (+62.6K grants). Claude's suggested legal names scored 100% (+20K grants).
- [GrantRadar] **Claude-picked matches** for the top 20K recipients scored 94.9% and were applied (+155K grants). A second round scored 93% (+104K grants).
- [GrantRadar] **Fuzzy-link re-checks** removed about 100K wrong links. "Keep" decisions graded 100% right, "switch" 94%.
- [GrantRadar] **National charities** (95%, +54K grants) and **school districts and colleges** (100%, +39K grants) were linked. 98K grants were labeled as never linkable.
- [GrantRadar] **Funder pages** now show school-district and college recipients.
- [NomBot] **Exact-name cleanup** removed 24K wrong links. Board-interlock low-confidence matches rose from 53% to 88% correct.
- [NomBot] **Funding by theme** (median per organization) and **track record** were added to the Overview and Breakdown tabs.
- [NomBot] **Insights tab** went live with 32 verified, chart-backed patterns for researchers and advisors. Each card has method, sources, CSV and chart export.
- [NomBot] **Donor-advised fund sponsors** (99% graded), 47 top names and 39 public universities were linked. A "latest filing" random-pick bug was fixed (migration 028).
- [imnet] **Test-mode donations** shipped, with no card numbers stored, a donations card for org staff, and Donate buttons in three places.
- [imnet] **Communities, DMs and the Near you map** shipped (nonprofit, foundation, community and volunteer pin types, plus a legend). **IRS-verified claims** and a **Public filings** panel on org profiles were also built. 163 unit and 83 e2e tests pass.
- [Admin] **Kate meeting** (12:00–12:40) logged. Day clocked out at 5.75 hours.

**Decisions**
- [GrantRadar] **Applied picks at 94.9% accuracy**, within error of the 95% bar, because a second Claude check rejected only about 1%.
- [NomBot] **Tab named "Insights"** instead of "Discover", since the audience is researchers and advisors.
- [NomBot] **Launch plan:** bring in researchers and advisors first through NomBot, then grow imnet from them.

**Next**
- [GrantRadar] **Re-check the remaining 118K small fuzzy links**, which grade about 91% right.
- [Admin] **Revoke the pasted API keys**, and put the working key into `.env.local`.
- [imnet] **Commit the NomBot lookup endpoint**, which is still uncommitted.

## 2026-10-14 (Wednesday)

*Hours worked: 9h (7:13am–10:16pm, 421 min inactive removed) · 0 commits · 122 messages*

**Summary:** Loaded the 2026 IRS filings, added Federal Register and Congress.gov data, rebuilt the Tyler brief with cloud and insights plans, and shipped a donor and nonprofit profile, hierarchy and speed overhaul in imnet.

**Done**
- [GrantRadar] **2026 IRS load** finished: 271,959 nonprofit filings added and grants reloaded across 4 IRS years (2023–2026). 225K orgs now have 2+ years of filings.
- [GrantRadar] **Grant linking** rose from 55.9% to 58% (3.08M grants). The ZIP rule (95% correct) and IRS alternate names (99%) added 88,266 grants and $3.8B.
- [GrantRadar] **Rejected matching rules** that missed the 95% bar: name containment (78–83% on a fresh sample), nationally unique names, and Splink (73% at best, 64 min training). Nothing from them was linked.
- [GrantRadar] **Federal Register and Congress.gov** loaded: 24,945 documents (78 funding notices) and 19,611 bills, all of the 119th Congress. Migration 019 added a `source_updates` freshness log. GDELT is built but blocked by rate limits, so it has no data yet.
- [NomBot] **Search benchmark** results: hybrid 69% relevant in top 10, vector 68%, Postgres keyword 57%, OpenSearch BM25 54%. BM25 is 40–70x faster (25 ms) and a third the size.
- [Admin] **Tyler brief** rebuilt into 4 tabs (Database, Data sources, Cloud plan, Insights), cut from 1,152 to about 650 words. It covers 11 GB database sizing, popovers, 12 data-source categories, a cloud diagram and a tools list. A copy is in GitHub at `docs/shared-database-brief.html`.
- [imnet] **Speed work**: caching, streaming header and skeletons, and prefetch brought clicks to 25–39 ms in a production build.
- [imnet] **Profiles and Ways to help**: demo covers and details for orgs and donors, donor Edit profile, Volunteer/Donate "Calls to help" toggle, volunteer hours confirmed by orgs, and LinkedIn-style Following and notifications.
- [imnet] **Four visual hierarchy passes** (type scale, text tones, layout, page leads) plus an optical-alignment audit that brought every button within 1px.
- [imnet] **Audit fixes** B-036 to B-040, including a medium security bug where users could date posts 2099 to pin them on top. Tests now run on their own Supabase stack, in about 1 min instead of 3. 144 unit and 78 e2e tests pass.
- [imnet] **Moved and comment counts** added: comment count is public and Moved count is private to the author and org team. PRs #4 to #8 merged to `main`.

**Decisions**
- [NomBot] **Keep vectors** for search and keep OpenSearch only as a benchmark baseline, since vectors win on quality.
- [GrantRadar] **95% accuracy bar** on a fresh, untuned sample before applying any match rule.
- [Admin] **Production embeddings via API** (OpenAI or Voyage) on Supabase with pgvector, because a Mac cannot serve live search.
- [imnet] **Moved count is private** to the post's author and org team (decision 0015).

**Next**
- [GrantRadar] **Free matching options**: reuse trusted links across years and funders, and add "doing business as" names. Decide whether to commit the rejected Splink script.
- [GrantRadar] **GDELT** retry once the block clears.
- [Admin] **Share** the Tyler brief with Tyler.

## 2026-10-13 (Tuesday)

*Hours worked: 9h (11:37am–8:44pm) · 0 commits · 113 messages*

**Summary:** Loaded every US nonprofit and three years of foundation grants into NomBot and GrantRadar, shipped the NomBot/GrantRadar Oct 12 meeting actionables, and built a LinkedIn-style imnet with about 20 new features.

**Done**
- [NomBot] **Deficit nuance** implemented: a one-year deficit is amber, red only when it repeats and is over 10%. A new "Questions to ask" box was added on org pages. GrantRadar's "How funders will see you" got the same advice.
- [NomBot] **Org website link** added from each 990 (28,843 of 50,971 filings had one, before the national load). **Print memo** fits 2 pages. **Plain-language pass** done.
- [NomBot] **"$1M or more" size filter** added for gift-size fit. Ohio food banks drop from 31 to 26 strong matches. The 50-question search eval was not re-run.
- [NomBot] **Optical alignment audit** across every page in both apps: health dots, buttons, icons and logos now within 0.5px. Pushed.
- [GrantRadar] **Giving circles** tab added, IRS-only: 145 circles in 38 states (was 15 in 5). Example: Impact 100 Owensboro, $258K in grants.
- [NomBot] **National data load:** 1.97M nonprofits, 513,813 filings with new embeddings, and 4.84M grants across 3 years (135,408 foundations), 57% linked to a nonprofit. Both limits (5 states, one year) are gone.
- [NomBot] **Speed fixes:** fuzzy grant matching cut from about 2 days to 97 minutes. Search table refresh cut from 40+ minutes to 2.5 minutes. A GrantRadar query cut from 15s to 32ms. NomBot search takes about 0.5s with a state and 3–6s nationwide.
- [Admin] **Tyler briefing page** published with diagrams, source links and a vector-search section. **Work-log** extended to imnet, with the Sept 30 backfill and a stale bullet removed.
- [imnet] **CONTEXT.md ledger** of dated features and fixes (F-/B- IDs) added. **RLS tests** moved into the repo and run in CI (all pass; each deliberately broken rule failed only its own test). shadcn moved to dev dependencies.
- [imnet] **Brand layer and LinkedIn-style structure** built, with a 3-column home, boxed posts and org tabs. **Local Supabase** runs on Docker at port 3100. 16/16 end-to-end checks passed.
- [imnet] **Multimedia feed:** 7 openly licensed Wikimedia photos plus 3 more videos, photo upload in the composer, and original logos for all orgs.
- [imnet] **Features shipped:**
  - team invites, notifications, impact-stats editor, edit/delete posts, logo upload, saved posts and share previews
  - current needs, giving journal, thank-you notes, events with RSVPs and "I'm interested"
  - LinkedIn-style comments with a comment preview in the feed, and an opt-in self-reported **Donor** badge
  - analytics, search, profile tabs and avatars
- [imnet] **Demo network** grown to 45 orgs and 1,000 people with about 2,570 comments. Final state: 116 unit and 56 e2e tests pass.
- [imnet] **Security review** found one medium open redirect in sign-in. It is fixed with four lower-risk fixes, all tested.

**Decisions**
- [imnet] **Donor badge is opt-in and "self-reported"** because gifts are typed in by donors and the journal promises privacy.
- [imnet] **Illustrated avatars instead of photos,** and original logos instead of real orgs' trademarks, to avoid impersonation and consent problems.
- [imnet] **Copied LinkedIn's structure but not its like counts, comment counts or ranked feed,** to keep the no-public-counts rule.

**Next**
- [Admin] **Wednesday 3–4pm session:** write down architecture and technical questions.
- [imnet] **Open product calls:** comment moderation ("Report comment"), a verified Donor badge via Every.org, and a Donate link for demo orgs.
- [Admin] **Tyler brief** still carries the old 5-state and one-year limits and needs updating.

## 2026-10-12 (Monday)

*Hours worked: 2h · 0 commits · 8 messages*

**Summary:** Set up a Claude API wallet guide for Keith in the fellowship doc, then logged 2h for bug fixes and Keith's meeting demo, plus 3h of presentation prep for Oct 11.

**Done**
- [Admin] **Claude API wallet guide** added to the fellowship software doc. It has 5 steps for Keith: sign in, buy $150 of credits ($100 Hunter, $50 Muneeb), optional auto-reload, invite Hunter as Admin and Muneeb as Developer.
- [Admin] **Wallet section formatting** now matches the PostHog section: same heading style and size, with purpose line, Status, steps and Cost.
- [Admin] **Oct 12 hours** corrected to 2h, covering bug fixes and Keith's meeting, where the project was demoed. The earlier 8.25h clock span was removed.
- [NomBot] **Bug fixes** logged for the day. The tag is unconfirmed and may belong to GrantRadar.

**Decisions**
- **Hours entry:** the 2h manual entry replaced the clock-based total, since it reflects the actual work.
- **Auto-reload:** left optional in the guide, so Keith can approve top-ups himself if he prefers.

**Next**
- **Tyler's amount:** the doc lists no amount for Tyler, and the guide doesn't invite them.
- **Token estimate:** the "TOKEN ESTIMATE" section in the doc is still empty.

## 2026-10-11 (Sunday)

*Hours worked: 3.5h · 0 commits · 11 messages*

**Summary:** Switched NomBot's scoring and overview to Sonnet 5.5 (median 14.0s → 7.2s, relevance still 91%), added clickable funder and peer lists, and ran an optical-alignment audit across both apps.

**Done**
- [Admin] **Presentation preparation:** 3h.
- [NomBot] **Model switch:** relevance scoring and AI overview now use Sonnet 5.5. Eval median per question fell 14.0s → 7.2s. Relevance held at 91% on the 50-question eval. Overview on fresh searches: ~8–9s (was ~11s).
- [NomBot] **Source panel push:** panel now pushes the org page left on screens wider than 900px instead of covering it. Panel is 340–440px on mid-size screens. Verified in a 1000px frame.
- [NomBot] **Narrow-column layout:** financial health signals, Cash/Programs/Liabilities cards and money bars stack into one column while the panel is open.
- [NomBot] **Gaps map hover:** hovering a county highlights its row in the list.
- [NomBot] **Clickable Funders tab:** click a foundation to see city, application status, a green "Foundation profile →" link and the grantees in your results. Verified with Kroger Co Foundation (7 grantees).
- [GrantRadar] **Clickable Peers tab:** click a group to see which funders paid it, largest first, each linking to its funder page. Verified with The First Step Home (12 funders). Funder names are black, green on hover.
- [NomBot] **Optical alignment audit:** measured every page, then fixed the real offsets.
  - Segmented-tab pill is now centred.
  - Page titles share the left edge with the text below.
  - Pill and button text is raised 0.75px.
  - Source-panel labels share one edge.
  - YoY table numbers reach the right edge.
  - Sources list descriptions share a column.
- [GrantRadar] **Optical alignment audit:** funder-card star centred (0.00px offset, was 2.75px high). "How to apply" labels sit on their first line. Shared fixes applied.
- [Admin] **Commits pushed:** NomBot `9a7caef`, `5f395dc`, `8570dff`, `74aee2b`, `bdfb5c8`. GrantRadar `bbf79f5`, `16fd4c4`. Eval report saved at `eval/results/2026-10-11-23-55.md`.

**Decisions**
- [NomBot] **Sonnet only for scoring and overview:** parsing and Research Buddy stay on Opus. This keeps quality while cutting latency.
- [NomBot] **Subpixel nudges skipped:** only offsets that were consistently ~0.9px were corrected. Two nudges that overshot were removed.

**Next**
- [NomBot] **Search speed:** dropping written reasons from scoring and pre-warming common searches are still open options.
- [Admin] **Unchecked in Chrome:** the black/green link colour changes were not visually verified.

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

## 2026-09-30 (Wednesday)

*Active in Claude Code: ~0h 48m (estimate) · 3 commits · 13 messages*

**Summary:** Created the imnet repo, pivoted its scope, and scaffolded Phase I (the network) on `dev` with CI passing.

**Done**
- [imnet] **GitHub repo** `institute-on-generosity/imnet` created (private) after switching `gh` to the `hunterIOG` account. `main` holds the brief, and `dev` is pushed.
- [imnet] **Workflow scope** added to the `hunterIOG` token, so GitHub Actions CI can be pushed.
- [imnet] **Architecture proposal** written: one Next.js + Supabase app, Postgres row-level security by org, and Claude for the AI assists.
- [imnet] **Scope pivot** worked through after the Iteration 1 update. It moved the product from a story engine for nonprofits to a consumer discovery network.
- [imnet] **Phase I scaffold** pushed to `dev` (commit "Scaffold Phase I: the network"):
  - Explore and Following feeds with cause filters.
  - Org profiles, post pages and donor profiles.
  - Magic-link sign-in.
  - Org claim flow, post composer and profile editor.
  - Admin queue and 30-day org stats.
  - Private "this moved me" signal.
- [imnet] **AI assists** added: "Draft from website" fills the profile form, and staff must edit and save. It is limited to that org's staff so other users can't spend Claude credits.
- [imnet] **Security rules** checked in PGlite (Postgres in WebAssembly) with stand-ins for Supabase auth and storage. They held in every case tried: signed-out users can't post, users can't make themselves admin, staff can't post for another org, and images without consent are rejected.
- [imnet] **CI** passes (lint, typecheck, tests, build). 14 tests on video-link parsing pass.
- [imnet] **Docs** added: the vision doc (Iteration 1 text) and a rewritten README.

**Decisions**
- [imnet] **Phase split:** Phase I builds the network and Phase II builds the media tools, so the place exists before the tools that fill it.
- [imnet] **Repo name** is `imnet` (impact-network). It was chosen over `impact-ledger` and `gratnet`. GratNet could be misread as gratification, which clashes with the no-dopamine-loops principle.
- [imnet] **Reactions and comments:** a single private "this moved me" signal, with comments off in Phase I. This follows the no-dopamine rule, and moderation costs a solo builder a lot.
- [imnet] **Fabrication rule:** Phase I posts are written by people. The principle becomes verified orgs plus impact claims linked to a source.

**Next**
- [imnet] **Supabase project:** create one so the app can run against a real database. It hasn't been tested on one yet.
- [imnet] **Phase II questions:** decide Inngest vs. Supabase queues, and whether to delete original files after redaction.

