# Work log

Daily summary of NomBot, GrantRadar and imnet work, written each night from Claude Code chats and git commits.

## 2026-10-27 (Tuesday)

*Hours worked: 4.75h (9:21am–6:59pm, 290 min inactive removed) · 20 commits · 66 messages*

**Summary:** NomBot got a goal popover, article-style reports with photos and its own cause icons; imnet's Discover became a Pinterest-style board; and the user-testing blurb went out.

**Done**
- **[NomBot] Research redesign** is live. Answers show a big number, headline and one chart, with details folded away. The count appears in 2–4 s (was 7–10 s). Words above the fold are down 27–52% (Search −52%, Browse −47%, Org −36%, Home −27%).
- **[NomBot] Goal popover** replaces the table the user rejected. Step 1 picks a topic and step 2 shows up to 5 questions. It opens below the tile and stays put, and step 2 keeps the cause header and breadcrumb. Questions are short, and "‹ Back to chat" returns from Browse with the popover reopened.
- **[NomBot] Research split into Ask and Reports.** Reports are article pages with a hero photo, credit line, large headline and a pulled-out key number. The 39 reports sit at `/research/reports`.
- **[NomBot] Every report now has a relevant photo:** 22 match the headline exactly and 17 use the closest scene. No photo is used on more than 2 reports. A rubber-chicken photo on a donor-advised fund report was caught and swapped.
- **[NomBot] Cause icons** are now our own line icons in soft tinted circles, replacing the UN artwork. Along the way, cause grids got no truncated names (5/4/3/2 columns, names wrap to two lines) and a shared layering scale fixed popover z-fighting.
- **[NomBot] Deploy safety:** a safe deploy script builds first, swaps only on success and rolls back on failure. A half-built Reports page had crashed :4000 at 12:14. It was restored from the last good build (ab80f30) and the :3001 test server was restarted.
- **[NomBot] Environment label** reached 53,913 of 66,912 orgs (81%) by 18:24.
- **[NomBot] Workforce and health care label pilots** (p3) passed. Workforce was 100% primary and 96% partial. Health care was 96% and 100% (raw).
- **[imnet] Discover rebuilt as a Pinterest-style board:** topic chips, a masonry layout of tall photos, and ways-to-help as pins. Pins show friends going or supporting the org. "People you may know" is a card on the board and an Edit causes chip replaced the old sections.
- **[imnet] Consistency and bug fixes:** one button each, friends instead of followers, and Sign up/Donate buttons in lists. Two bugs were fixed: events across the Nov 1 clock change keep their time (B-052), and share previews embed photos after the Next 16.4.3 upgrade (B-053). PR #20 was merged to `main` with 31 commits after all 4 checks passed.
- **[Admin] User-testing setup:** the booking link was checked, and Julia's blurb was revised to her voice (AI Fellow, AI tools, calls with Hunter) and sent. The Oct 26 log was updated to 4.75 h by adding 1.5 h of meetings.

**Decisions**
- **Popover over table:** progressive disclosure (topic, then questions) is easier to scan than a table.
- **Own icons over UN icons:** the UN rules bar recoloring or cropping, so 17 bright icons could not be made harmonious. The "By cause" wording replaces "By goal".
- **Corrected categories becomes a switch,** not a follow-up prompt, since it is a setting that re-runs the answer in place.
- **Friends are one-way:** no acceptance step for now.

**Next**
- **[NomBot]** Ship the speed and wording batch: known questions under 1 s and typed questions under 4 s. Remove "(SDG 13)" from answers, remove horizontal scroll in the popover and fix the environmental-education category. Then add hover preview cards for orgs and foundations.
- **[NomBot]** Finish the environment label run, then grade it before loading anything.
- **[Admin]** Reboot the Linux box (GPU error) and draft the 30-minute user-test script.

## 2026-10-26 (Monday)

*Hours worked: 4.75h (9:33am–10:29pm, 537 min inactive removed) · 16 commits · 102 messages*

**Summary:** Fixed NomBot's place search for the Inglewood test (coverage 30–57% → 7/7, 9/10, 8/8), built Browse by cause on the 17 UN goals, and began a minimal-UI redesign. Also patched Next.js in NomBot and iMNet.

**Done**
- [NomBot] **Inglewood place search** now finds 7 of 7 health/dental, 9 of 10 girls' leadership and 8 of 8 youth sports orgs, up from 4/7, 3/10 and 3/8.
  - Results come in tiers: in the city, serving it, nearby, county.
  - Orgs named for Inglewood count even if they mail from elsewhere.
  - Search stays about 1 s.
- [NomBot] **Girls' leadership top 10** rose from 6/10 to 9/10 relevant, and all 3 phrasings pass.
  - "Girls" now ranks higher instead of filtering. "Girls only" still filters.
  - Whole-word "must mention" matching added.
  - API tests 276/276, routing tests 114/114.
- [NomBot] **Research Report city filter** now answers city-level questions. The false "no city data" caveat is removed.
- [NomBot] **Download report** added: a printable report with method, orgs by tier, funders, caveats and leads to verify, plus a richer CSV. 3 PDFs, 3 CSVs and a summary prepared for Keith.
- [NomBot] **Browse by cause and Research Report restructured around the 17 UN goals**, with one shared taxonomy mapped to labels and IRS cause codes.
  - 70 questions: the 54 earlier ones plus 16 new goal questions.
  - Pages load in about 0.4 s or less.
  - "SDG 4" and "life below water" phrasing works.
  - 8 goals have strong coverage, 7 are marked limited, and 9 subcategories are not in the data yet.
- [NomBot] **Youth development label** wired into research answers, org pages, API and MCP.
- [NomBot] **Search summary under the search bar** (count line from results, short description checked against returned orgs), with the old overview demoted to "Did you know".
  - Description switched to start early for speed.
- [NomBot] **First UI redesign live on :4000**: minimal search page, big count with tier icons, Insights toggle, softer colors, an ask box on Research Report, and consistent numbers across panels.
  - Words above the fold: search −34%, home −27% (target −50%).
  - A UX audit found 90 issues: 1 critical, 36 task-hurting, 53 polish.
- [NomBot] **Next.js 16.4.3** security upgrade, closing 2 critical and 1 high advisory. Public link left open. The half-finished rating work is saved on `wip-rating-merge`.
- [imnet] **Next.js 16.4.3** upgrade pushed (it was on 16.3.8). Typecheck, lint, 209 unit tests and build pass. Funders in the public record now link to their records.
- [imnet] **Demo data seeded locally** for ASPCA: 10 comments and 7 volunteer shifts, gitignored. NomBot's :3001 test server was restarted after the upgrade broke the trust signals panel.
- [Admin] **Follow-ups:** drafted the write-up for Keith and a WhatsApp blurb for Julia.

**Decisions**
- **Speed over exactness** for the search summary: the description starts from the closest matches and may differ slightly from the final list.
- **Minimal UI:** one focal point per page, with text cut and icons used instead of words.
- **Next.js patch** applied immediately rather than waiting for the demo to end.

**Next**
- **Redesign:** org page, research answers, Browse and reports, plus more trimming. Sidebar treatment is undecided.
- **Labels:** environment, workforce and healthcare still need pilots and review.
- **Keith:** send the Inglewood reports and write-up. Legal update due after Thursday.

## 2026-10-22 (Thursday)

*Active in Claude Code: ~0h 24m (estimate) · 0 commits · 17 messages*

**Summary:** Mostly admin and outreach day: checked API key usage for two testers, set up remote access for a Chicago trip, and drafted outreach messages.

**Done**
- [NomBot] **API key usage** verified for Muneeb (3 calls) and Tyler (1 call). Both were successful `/api/v1/search` calls on Oct 19, with no errors and no calls since.
- [NomBot] **Failed-auth log** checked: 34 keyless rejections, all from our own test suite. No outside failed attempts.
- [NomBot] **Public API availability** confirmed. The Tailscale Funnel link is up and rejects keyless calls. The API stays reachable only while the Mac is awake, online, running Tailscale and running NomBot on :4000.
- [Admin] **Remote access** set up for Chicago. Screen Sharing is on and reachable over Tailscale. The travel Mac answered in 11 ms on home Wi-Fi and 105 ms on a phone hotspot, with a direct path and no relay.
- [Admin] **Follow-up draft to Kate** written as a WhatsApp message. It covers NomBot progress and four requested items: past diligence reports, advisor-group questions, contact names and a Salesforce example.
- [Admin] **Intro request to Stephanie** drafted, asking for 2–3 advisor or researcher introductions.
- [Admin] **IoG team ask** edited for grammar and clarity. It now asks for researchers and advisors for NomBot, and for foundations, nonprofits and donors for iMNet onboarding.
- [Admin] **Background agents** stopped. The grant matching round 8 agent had finished and pushed its work. The data quality and nightly benchmark agent also finished.

**Decisions**
- [Admin] **Screen Sharing over Tailscale** chosen for Mac-to-Mac access from Chicago. It reaches the live terminal session, and Remote Control and SSH stay as lighter fallbacks.
- [NomBot] **Rebuild deferred.** Rebuilding now would cause downtime and ship the half-finished rating change.

**Next**
- [Admin] **Screen Sharing login** still to be tested from the travel Mac before leaving.
- [Admin] **Mac sleep** must be prevented while away, by staying plugged in with the lid open or running `caffeinate`.
- [Admin] **Subscriptions question** for Keith about Inside Philanthropy, Chronicle of Philanthropy and Giving USA access.

## 2026-10-20 (Tuesday)

*Hours worked: 7.75h (12:06am–6:08pm, 624 min inactive removed) · 0 commits · 187 messages*

**Summary:** Shipped go-to-market features, a decluttered imnet UI, six NomBot data upgrades and the 10/20 invoice.

**Done**
- [imnet] **Go-to-market features** built and pushed to `dev` in 7 commits: invite links with invite-only mode (F-131), "Go together" event invites (F-132), claim-your-profile (F-133), weekly "Ways to help" email (F-134), giving-day page (F-135), launch readiness (F-136) and a **landing page** (F-137). 185 unit/RLS and 101 e2e tests passed.
- [imnet] **Decluttering pass** cut privacy notes, subtitles, the thank-you feature and the share button. The Home filters merged into one row, and post headers became icon-based.
- [imnet] **Post header** now reads cause | place | time, with stacked friend faces on a second line. The logo is sized to the header height, and the **site font** is now the system font. 102 e2e tests passed.
- [imnet] **Giving shares** show each gift or hour as a percentage of an org's recorded total, hidden when fewer than 5 people contributed. **Commenter bios** show hours and dollars for opted-in people, and post text is auto-formatted into short paragraphs with bold figures.
- [NomBot] **Transfer fix** removed **$23.3B** of non-cash transfers from grant totals. 2021 went from $149.7B to $141.5B.
- [NomBot] **Evidence chain** ("Show the steps") is live on every research answer, in the API and MCP. It adds a spike check on the 2020 food bank figures.
- [NomBot] **Four labels loaded:** racial equity, immigrants and refugees and mental health (all graded 90%+), then health equity (98% main, 100% partial, recall ~54%). Routing tests reached 93/93 and research 91/91.
- [NomBot] **Education label** is live with a 3-question Research block ($46.2B, 24% of foundation dollars). **Token logging** with an /admin section went live at 6:32 PM.
- [NomBot] **Grant matching round 6** raised foundation grant links from 65.6% to **67.4%** (+$9.8B linked across both rounds). It also added 9,487 orgs missing from the IRS file. **Board-name merges** are now used in NomBot.
- [NomBot] **IRS category corrections** found 4,049 miscoded orgs (94% on a fresh hand check). They now appear on org pages and in the API, plus an optional "corrected categories" answer mode.
- [NomBot] **Service areas** were built (573K orgs) but fell below the accuracy bar, so they are not used yet. A guard fixed the dev-server error.
- [Admin] **Invoice 10_20_26** was produced: **60 h × $60 = $3,600** for Oct 8–20, 3 pages with the imnet screenshot and a single LOGGER.md link. A Gmail draft was made, and nothing was sent.
- [Admin] **Saturday rule** (only time after 4:30 PM counts) added to the clock-out script. Oct 17 dropped from 6.25 h to 0.75 h. Oct 19 was corrected to 9 h with 120 min of meetings.

**Decisions**
- **Immigrants label split:** immigration-policy groups of any stance get their own sub-type so they don't skew the funder rankings.
- **Label runs:** all four remaining label runs (animal welfare, youth, arts, health equity) were queued one at a time to spread weekly subscription use.
- **work-log repo:** it stays public so the LOGGER.md link works for the invoice recipient.
- **Go-to-market plan:** launch in the South Bay, invite-only, with nonprofits signing up first and GivingTuesday (Dec 1) as the first test.

**Next**
- **Label full runs:** animal welfare is running, then youth and arts. Each needs approval before loading.
- **Service areas:** re-run on Linux, aiming for 90% accuracy on national and international scope.
- **Invoice:** attach the PDF to the Gmail draft and send. Confirm whether imnet hours are billable.

## 2026-10-19 (Monday)

*Hours worked: 9h (11:37am–11:39pm, 298 min inactive removed) · 54 commits · 156 messages*

**Meetings:** 120 min in 2 meetings, the second with Josh (Joshua Elder, Siegel Family Endowment) at the AI Fellows session with Helen, Tyler, Rafael and Julia

**Summary:** Built the Linux GPU helper, shipped new APIs and labels, and ran Year-in-giving, backups and nightly monitoring.

**Done**
- [NomBot] **Housing and homelessness label** loaded: 32,755 orgs (19,110 main, 13,645 partial), graded 98% and 94%. It adds $2.89B of foundation grants (2022–24) for main-focus orgs. Routing 75/75, research 70/70.
- [NomBot] **Two-cause answers** now rank both causes with overlap (7 of the top 50 climate funders also top 50 for women and girls) and readable foundation names. Routing 73/73, research 69/69.
- [NomBot] **Partner API** gained 10 data endpoints, news, IoG Giving Guides (13 guides, 168 sections, behind `iog_internal`) and MCP tools. API tests 169/169 at first, then 209/209.
- [NomBot] **Semantic search** (`semantic=true`) is live for news, bills and Federal Register. 48,776 items were embedded on the Linux GPU in 4 min, and keyword search had found nothing for 9 of 10 test questions.
- [NomBot] **News dedupe** found 883 duplicate copies (23%), so 3,819 headlines become 2,936 stories. The API returns one row per story with `also_reported_by`.
- [NomBot] **Grant linking round 5** raised foundation grants linked from 64.2% to 65.6% (+209,533 grants, +$7.82B). Seven new rules each scored 58–60 of 60 on hand-graded samples.
- [NomBot] **IRS tax status** went live: 1.43M Pub 78 orgs and 1.25M revocations. 201 revoked orgs still received $12.0M in foundation grants. Added the `/orgs/{ein}/status` endpoint.
- [NomBot] **Nightly checks** on `/admin`: the first data-quality run gave 21 pass, 3 warn, 0 fail. The benchmark answered 84 of 150 with 0 misleading, at about $0.52 per night.
- [NomBot] **Local-model pre-screen test** (Qwen 2.5 7B) saves 34% of Claude work on climate and 35% on tech and AI skills, at under 1% loss. It saves only 3% on education.
- [NomBot] **Tech and AI skills label** loaded (307 primary, 834 partial).
- [imnet] **Year in giving** shipped: a private, story-style donor Wrapped with an opt-in share card, a Home card for Dec 1–Jan 31, a pilot admin dashboard and the first sign-in flow. 173 unit and 93 e2e tests pass.
- [Admin] **Linux helper** is set up: its GPU embeds 4x faster than the Mac and its vectors match (0.999998+). It holds a verified 106 GB raw-data copy. The nightly backup copy runs unattended, and the first restore test passed (18 min, 13/13 tables). Weekly Parquet snapshots (13 files, 686 MB) and an IRS batch watcher are live.
- [Admin] **Muneeb and Tyler** received read-only API keys with `iog_internal`. The generosity-data README was rewritten from 680 to 131 lines and the repo was made private. The day was clocked at 8 h, with the 60-min meeting with Joshua Elder added.

**Decisions**
- **Linux as helper, not server:** it has 15 GB RAM against the Mac's 24 GB, so the database stays on the Mac.
- **Access by API key only:** no local runs, and the repo is private because a public README could not enforce that.
- **Pre-filter for narrow labels only:** it is skipped for education, where it saves about 3% for 12 GPU-hours.
- **Related-party transfers** (such as the $7.63B UL to ULSE line) will be excluded from grant totals but kept visible as transfers.

**Next**
- **Overnight jobs:** the transfer fix, the "Show the steps" evidence chain, service areas, narrow-label pilots and the education run (about 13 h left).
- **Approvals needed:** education and the narrow labels load only after Hunter approves them.
- **Mac sleep:** `disablesleep` is still off, so a closed lid would stop the overnight work.

## 2026-10-18 (Sunday)

*Hours worked: 0.25h (2:52am–5:48am, 162 min inactive removed) · 2 commits · 3 messages*

**Summary:** Overnight agents finished, so the 2012–2025 history, foundation payout and nonprofit finance panels, and a substance use label were tested, committed and pushed live.

**Done**
- [NomBot] **Benchmark** rose from 79 to 83 of 150. Routing is 71/71, research 66/66, and answer checks show 0 mismatches.
- [NomBot] **History** now reaches back to 2012. Foundation grants grew from 5.7M to 14.8M ($838B, 64% linked). Charity grants grew from 3.4M to 8.5M ($1.52T, 81% linked).
- [NomBot] **Foundation payout** answers are live: in 2024 the median private foundation paid out 5.2% of its investment assets, and 55% paid out 5% or more.
- [NomBot] **Nonprofit finance** answers are live: deficits by year, months of cash and multi-year streaks.
- [NomBot] **Substance use label** is loaded and passed both grading bars: main focus 98%, partial 91%. It has 9,275 main focus and 4,191 partial. Opioid questions now use it instead of keywords, and the stale C24 benchmark entry was fixed.
- [NomBot] **Label fix:** Sonnet can keep or drop a partial but never promote it to main focus. That rule removed the errors.
- [NomBot] **Housing and homelessness label** finished its full run and passed both bars: main focus 98%, partial 94%. It has 19,110 main focus and 13,645 partial. It is not loaded yet.
- [NomBot] **Theme pilots** failed on partials: racial equity 91% main focus and 87% partial, immigrants and refugees 84% partial, mental health 77% partial. They need definition fixes.
- [Admin] **Commits** pushed: generosity-data `8a79030` and NomBot `c7c7f5b`. The live site was rebuilt. Labeling used 22% of the weekly subscription limit.

**Decisions**
- [NomBot] **Same-funder growth:** for trends reaching before 2020, growth should use the same funders in both years. E-filing wasn't required before 2020, so early years miss smaller foundations (48K in 2015 vs 93K in 2022). This is a recommendation, not yet approved.

**Next**
- [NomBot] **Fix pre-2020 growth.** The food bank trend currently shows a misleading 456% for 2015–2024.
- [NomBot] **Load housing and homelessness**, a 9-minute refresh, then add it to NomBot.
- [NomBot] **Re-pilot** racial equity, immigrants and refugees, and mental health after definition fixes.

## 2026-10-17 (Saturday)

*Hours worked: 0.75h (4:30pm–10:58pm, 349 min inactive removed) · 29 commits · 87 messages*

**Summary:** Research answers got much better and the database grew, with the benchmark rising from 73 to 79 of 150 and misleading answers falling from 13 to 0.

**Done**
- [NomBot] **IRS recovery:** 156,971 missing returns restored, including Fidelity's 2023 return, because the IRS split May 2025 and 2026 into 05A and 05B files. Foundation grants rose to 5.72M ($413B) and charity grants to 3.41M ($673B). Fidelity 2023 now matches its own return at 99.2%.
- [NomBot] **Research benchmark:** built 150 researcher questions (`npm run eval:benchmark`). The first scorecard was 73/150. After fixes it was **79/150**, with misleading answers down from 13 to 0 and wrong routings from 10 to 0.
- [NomBot] **Question reader:** about 80% cheaper per question with a warm cache (~$0.016 → ~$0.003). Routing accuracy went from 104 to 112 of 112, and there is a 30 s timeout fallback.
- [NomBot] **Fast medians:** about 3x faster (typical 633 ms → 282 ms), using about 1.1 GB of precomputed tables.
- [NomBot] **Answer quality:** the open-ended question test went from 19/42 to 49/49. Largest-1% questions, wrong-premise corrections, the opioid answer and the school district vs public college split were fixed.
- [NomBot] **Cause labels everywhere:** climate and women and girls now appear in search chips, org pages, the API, MCP and weekly snapshots. `test:labels` passes 24/24. Answers for unlabeled themes now carry a trust note.
- [NomBot] **Org pages:** they now show Grants received (foundations, charities, federal) and Grants given. Big-giver pages are faster (Fidelity ~1.1 s → ~20 ms).
- [NomBot] **Inflation and benchmarks:** trend answers show real growth (for example 9.0% nominal, 1.7% after inflation). National answers state completeness: 65% of IRS SOI foundation grants and 71% of Giving USA.
- [NomBot] **Household giving:** loaded IRS SOI charitable deductions by county (2013–2023) and ZIP (2013–2022), 1.96M rows. 2 of 12 household questions now pass.
- [NomBot] **Finance panels:** foundation finances (458K foundation-years) and a nonprofit finance panel (1.23M org-years). The median foundation payout fell from 5.7% (2022) to 5.2% (2024). Not yet committed.
- [NomBot] **Schedule I placeholders:** "SEE ATTACHED" and "VARIOUS" rows ($14.9B) were split out of recipient, place and cause answers. Totals now add "plus $41.7B reported but not itemized". The SVCF 2022 gap is in the filer's own return, not a bug.
- [NomBot] **Linking and company foundations:** foundation grants linked rose 63.2% → 66.5% (58.7% of $) over two rounds. Federal awards linked rose 80.6% → 85.5%. Company foundations went from 1,446 to 1,757, with 102/102 recall and 48/50 precision.
- [NomBot] **Substance use label:** screened 22,713 orgs on the subscription at $0 API cost. Main focus was 99% correct and partial focus 89%, so it is **not loaded**. The subscription labeler with `--new-only` top-ups and `after_load.sh` is built.

**Decisions**
- **Subscription first:** labeling runs on the Claude subscription, and switching to the API key needs confirmation.
- **Placeholder split:** exclude placeholder rows from recipient, place and cause answers, but keep them as "reported but not itemized".
- **Led-by labels:** use only self-described tags, with no name-based inference of race or gender.
- **Raw federal audit file:** keep it locally for now (git-ignored).

**Next**
- [NomBot] **Overnight runs:** history back to about 2012 and the label work (substance use partial check, theme pilots) were still running.
- [NomBot] **Substance use:** run a Sonnet check of the 4,715 partials, re-grade, then load if it passes.
- [NomBot] **Commit and rebuild:** commit the finance panels and overnight work after a full test run, then rebuild the live site.

## 2026-10-16 (Friday)

*Hours worked: 7.75h (8:49am–11:00pm, 437 min inactive removed) · 0 commits · 127 messages*

**Summary:** Shipped NomBot's research pages, ChatGPT-style answer chat, Google-style results and 10–60× faster search, set up Mac hosting with a partner API, and added three imnet features.

**Done**
- [NomBot] **Loading-screen bug** fixed: the rotating headline removed the clicked chip and the overlay went with it. Rotation now stops after a click.
- [NomBot] **Rural-Appalachia search** cut from 15–20 s to 4.7 s by fixing a ZIP type mismatch. The same fix went into GrantRadar. A 17-hour stray query was cancelled.
- [NomBot] **Insights became Research**, with a dedicated page per finding: key numbers, chart, data table, org side panel, scoped chat. All 32 findings now have short headlines and 2–3 bullets. Old links redirect.
- [NomBot] **Research answers** cover 15 question types, using fixed queries (the AI never writes SQL). 30 of 32 test questions now get an on-target answer, up from 19. Answers open at `/research/ask` as a ChatGPT-style thread with follow-ups.
- [NomBot] **Follow-up suggestions** now go through topic rules plus an AI picker. `npm run test:followups` passes on 8 threads.
- [NomBot] **Search results** redesigned Google-style, with the diagram first in the knowledge panel. "Report" and "Ask about this finding" now open as right-side panels.
- [NomBot] **Search speed:** database time went from 12–14 s to 0.2–3.4 s. Full page went from 8.3–14.6 s to 5.3–8.1 s. Benchmark relevance held at 69%. Postgres now has 4 GB `shared_buffers`, and the old 1.4 GB vector index is dropped.
- [NomBot] **Database research layer:** a pre-summarized grants table (about 950K rows), 681 category codes with plain-English names, a data dictionary and a nightly refresh.
- [NomBot] **Hosting and partner API:** the Mac runs always-on production apps behind a password gate, via Tailscale Funnel. Partner API with per-partner keys, remote MCP and public docs. Weekly Parquet snapshot of 378 MB. The architecture diagram was redrawn.
- [imnet] **Three features** built, 165 unit and 85 e2e tests passing: friends' experiences, a "ways to get involved" path, and Notable givers with fictional demo figures.
- [imnet] **Friends tab** merged (PR #15). Then message controls, a first-week welcome flow, person reports, a "What Verified means" page and an AI-assisted media label merged (PR #16).
- [Admin] **Una Osili meeting** logged (45 min). Her feedback led to the climate and women-and-girls labels.

**Decisions**
- **Host on the MacBook** instead of Supabase at about $129/month.
- **Partner access via APIs and snapshots only**, with no direct SQL on the personal Mac.
- **Faster Claude models rejected** for scoring and question parsing. Each cost 2–7 benchmark points.
- **Notable givers are opt-in and fictional in the demo.** Real people need their consent.

**Next**
- **Tailscale:** the install was still pending at last check; the later live check shows the address working.
- **Data expansion:** Schedule I, Census ACS and USAspending are still running and not committed.
- **Open questions:** restore spending, staff and volunteers in result lines. Add the state-answer headquarters caveat and DC handling.

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

