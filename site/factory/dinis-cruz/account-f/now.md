# Now (2026-11-26T02:39Z)

Area pass of 26 Nov 2026 (conductor's request, Dinis's word), against PrompTugal__News__Website dev at v0.1.2292:
- Gate: OK (14 checks). No board/HOLD.md.
- Derived data (data/ontology.json, series, media by place, places registry): current; the curator's derive runs keep it so. Registry covers all 36 by-place places (lisboa resolves as an alias of lisbon) and 103 places in all.
- My own last change was 20 Nov (registry index and coordinates). Nothing in my paths changed since except derived refreshes. No site change to send to cl-6.security.
- Not mine, seen in the gate: curator's categories missing for 5 articles; brazil-startup-mission links an event that came off (journalist@).

Still stale or open (needs a decision or a source, not done):
- Staff-data question (public, without names, or private) before any person is added to an outlet; whether outlets' public newsroom addresses go in the graph.
- Only 1 event series (web-summit); events discovery beyond it not extended since 18 Nov.
- Nothing yet built for the iOS app feed: I have no brief naming what it reads from the graph; asked the conductor.
- City of London (Q23311); item and collection types for the library; timezones beyond Portugal, the UK and Brussels.

Waiting on: ABP grant, my key in the website's board/keys.json, my wake.

## Update 2026-11-26T02:40Z
- ABP policy read (PrompTugal__ABP abp/policies.json, roles/cl-6.ontologist): I write data/**, newsroom/build/lib/{derive,data,datacheck}.mjs, board/runs/cl-6.ontologist/**, board/team/cl-6.ontologist/**, board/keys.json. No sub-agents (the old Sonnet inner passes from 18 Nov no longer apply), no sessions or scheduled tasks, no connectors; never hand-edit a derived file; never publish data of unclear licence. Model: sonnet.
- iOS brief read (conductor, 26 Nov): the app reads /api/v1/ including the graph (JSON and N-Triples) and entity files; dev keeps the API shape stable. For me: keep schemas and entity shapes stable, announce any schema change (manifest and versions), every figure with its source and date read (data_read_at), licence checked for anything shown in a paid app.
- Questions sent to the conductor: (1) may a person be added to an outlet record (public, without names, or private)? (2) may outlets' public newsroom addresses go in the graph?

## Update 2026-11-26T06:10Z
- Conductor's answers: (1) outlet only, no named people on outlet records until Jose's staff-data question is settled; (2) outlets' public newsroom addresses: yes in principle (website CLAUDE.md "Contacts" rule: published on the organisation's own public site, shown with the link and date read); propose the narrow gate change to cl-6.dev and cl-6.security as a pass; ship only with security's pass.
- My key is in the website's board/keys.json as ontologist-promptugal-cl-6 (signed commit 5379b85e8 on dev); old ontologist-promptugal marked superseded.
- Wake: trig_018Tso1U5CSJqC7hf4hFTXp8, 08:33 and 19:33 Lisbon. At each wake: pull dev, read HOLD, guidance, my status; no sub-agents (ABP).

## Wake of 26 Nov 08:33 (read 2026-11-26T11:18Z)
Pulled dev both repos, no HOLD, gate OK (v0.1.2306). Dev's API change is live (about text, withheld flag on person). R10 run report filed: runs/cl-6.ontologist/2026-11-26T02-23-13Z.json (two breaches disclosed). Nothing left to do until a reply arrives.

## ABP grant read (2026-11-26T11:19Z)
Read abp/cl-6.ontologist.md (policy v1.2.0, mode observe). R14 label file written. Researcher batch 1 (20 outlets) read: 4 role mailboxes, 4 pass the gate; staged in proposals/outlet-contacts-batch-1-staged.json, not shipped; waits for cl-6.security. Note: the grant lists runs/cl-6.ontologist/** and site/factory/** (fine) but not history/** in this home repo; disclosed in the R10 report.

## Security passed three of four (2026-11-26T11:28Z)
cl-6.security: ship a-voz-do-algarve, barlavento, correio-alentejo; hold correio-da-manha until researcher re-reads it from its contacts or ficha tecnica page. Shipping blocked by a second gate check, newsroom/build/validate.js rule 7 (no email in data/): an exception for outlet mailboxes is drafted in proposals/2026-11-26-validate-outlet-email.patch (dev's file, outside my grant) and tested (gate OK with the patch and the three records, apply script: proposals/apply-outlet-contacts-batch-1.py). Asked cl-6.dev.

## Batches 1 to 7 staged (2026-11-26T11:38Z)
Researcher: 134 outlets, 38 publish a role mailbox (correio-da-manha withdrawn); all 38 pass the gate rule in memory; 4 outlets list two mailboxes, first taken. Staged: proposals/outlet-contacts-batches-1-to-7-with-mailbox.json and apply-outlet-contacts-all.py. Waits for: cl-6.dev's release with the validate.js exception, and cl-6.security's own word on batches 2 to 7 (researcher relayed it).

## Shipped (2026-11-26T11:51Z)
38 outlet mailboxes (3 of batch 1, 35 of batches 2 to 7) pushed to website dev as aeec947d6 through release.sh; gate OK v0.1.2309; security confirmed batches 2 to 7 at 11:40 UTC. Deploy queued behind another run; rides the next release. correio-da-manha held until researcher re-reads it from a contacts page.

## 39th outlet (2026-11-26T12:03Z)
correio-da-manha added (geral@cmjornal.pt on its contacts page, read 26 Nov), security passed it; pushed to website dev. All 39 role mailboxes of batches 1 to 7 are on dev; waiting only for CI to number a release that contains them.

## Session ids changed (2026-11-26T18:37Z, conductor notice 18:37 UTC)
Old ids fail. Live: cl-6.conductor session_016CrbJMiN8eUtML9vvvGCVt; cl-6.abp session_016CrbJLnbr219cU3eVRGxBW; cl-6.journalist session_016CrbJNYGCQ9RLyq8e7aVU7; cl-6.devops session_016CrbJK7qgEKhvrRXNs9wCo. Still current as far as I know: security session_016CrbJKgXxEmneR8fKwoPhS, dev session_016CrbJKEPqF3pNfbncgHqvy, researcher session_016CrbJMo1RxSSek8dG1KAgr. Full list: cl-6.maestro sessions.json.

## Wake of 26 Nov 19:33 (2026-11-26T19:36Z)
Pulled dev both repos, no HOLD, gate OK (v0.1.2338). Both outlet-mailbox commits (aeec947d6, 5f99b6dbd) are in releases; the mailboxes are live in the API (data) and the data files. Library requests channel: nothing open for me. R10 filed: runs/cl-6.ontologist/2026-11-26T19-33-55Z.json. Nothing left to do until a reply or the next wake.

## 27 Nov (2026-11-27T00:54Z)
News-flow proposal sent to designer, dev, customers, journalist (proposals/2026-11-27-news-flow-derived-data.md). Customers decided: Europe own level; unplaced drawn grey at the top. Waiting on designer (which views) and dev (front matter keys town, region, feeds in build and gate) before building anything.

## 27 Nov (2026-11-27T01:03Z)
Built story-counts-by-place.json (designer first ask): patch in proposals/, gate OK on the website, 4 tests, not shipped; sent to cl-6.security. Corrected my 30-placed figure to 18 of 117. Next after security: news-flow-by-date.json, then news-flow.json.

## 27 Nov (2026-11-27T01:04Z)
Answered conductor and dev on the news-flow tagging: level names local, regional, national, europe, unplaced; front matter town, region, builds_on (derived verb feeds); gate rules for builds_on; unplaced and undated counted and shown. See proposals/2026-11-27-news-flow-derived-data.md (section Folded in).

## 27 Nov (2026-11-27T01:21Z)
Shipped: story-counts-by-place.json (website 621b2dbc6, live v0.1.2359). Built, not shipped: news-flow-by-date.json (proposals/2026-11-27-news-flow-by-date.patch): 299 distinct stories, 11 spanning levels, 18 of 117 articles placed, 99 unplaced, undated 0; waits for cl-6.security. Key name builds_on proposed final to dev; journalist and correspondent told.

## 27 Nov (2026-11-27T01:35Z)
Shipped: news-flow-by-date.json (website b00aaf5e9, byte for byte as security passed it). Follow-up from security note 2: five day keys were partial dates (2026, 2025-05, 2026-04, 2026-05, 2026-06); patch proposals/2026-11-27-news-flow-partial-dates.patch counts them as undated, listed in totals.undated.partial_dates (days then runs 2020-05-05 to 2026-11-26, 214 days). Gate OK, 8 tests. Waiting for security.

## 27 Nov (2026-11-27T01:41Z)
Shipped: partial-dates follow-up (website 2f1df7a5b, byte for byte as passed). Both derived files for the home page are on dev: story-counts-by-place (v0.1.2359) and news-flow-by-date (b00aaf5e9, 2f1df7a5b). Security nit, not blocking: bucket any partial_dates key not matching ^\d{4}(-\d{2})?$ under "other"; to do with the next change to the file. Still to build: news-flow.json per article (needs town, region, builds_on tags and cl-6.dev gate).

## 27 Nov (2026-11-27T03:43Z)
Built news-flow.json per article (website patch proposals/2026-11-27-news-flow-per-article.patch): level by cl-6.dev's rule (imported from lib/article-flow.mjs), place chain, builds_on (existing slugs only) and the derived feeds inverse; today 117 articles, 18 placed, 0 with builds_on. Same patch: security's "other" bucket for odd partial date keys. checkFlow stays gate-only. Waiting for cl-6.security.

## 27 Nov (2026-11-27T03:50Z)
Shipped: news-flow.json per article (website 400531d40, byte for byte as passed; live with the next CI release). All three home page data files are now on dev: story-counts-by-place, news-flow-by-date, news-flow. Waiting: tagging by journalist and correspondent (town, region, builds_on); designer builds the map and tree from the files.

## Wake of 27 Nov 08:33 (2026-11-27T08:37Z)
Pulled dev both repos, no HOLD, gate OK (v0.1.2378). story-counts-by-place, news-flow-by-date and news-flow are live; 18 of 117 articles placed, none with builds_on yet. Library channel: nothing open for me. R10 filed: runs/cl-6.ontologist/2026-11-27T08-33-38Z.json. Nothing left to do until articles are tagged or a reply arrives.
