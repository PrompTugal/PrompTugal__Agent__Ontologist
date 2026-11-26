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
