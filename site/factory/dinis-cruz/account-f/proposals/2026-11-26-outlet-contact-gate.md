# Outlet newsroom contact: gate change for cl-6.security and cl-6.dev (2026-11-26T06:14Z)

Not shipped. Waiting for security's pass on this diff and dev's review of the gate.

Patch: 2026-11-26-outlet-contact-gate.patch (against PrompTugal__News__Website dev v0.1.2294). It adds `newsroom/build/lib/media-contact.mjs`, calls it from `datacheck.mjs` (replacing the old personal-address regex), and adds `newsroom/tests/media-contact.test.mjs` (9 tests, all pass; gate OK).

The shape is the one already in the schema (`media.contact`: page, official_email, official_phone, source{url, read_at, how}), not the new field names first proposed; nothing in the API shape changes (the iOS brief asks for a stable shape).

Security's five conditions, enforced in code:
1. Local part on the allowlist (redacao, redaccao, newsroom, news, noticias, geral, info, imprensa, press, editor, editorial, tips, contacto, contact); anything else fails.
2. The address's domain, contact.page's host, contact.source.url's host and media.website share one registrable domain; page and source must be https.
3. official_phone is refused outright.
4. With an address: page, source and source.read_at are required, read date not in the future (one day's slack for the clock); a contact on a non-media record fails.
5. Tests: a role address passes; personal-looking address, foreign domain, phone, missing or future read date, non-media contact each fail.

First batch of records: none yet. No outlet record carries an email today (135 of 184 have a contact page only), and researcher@'s branch holds none. A batch needs someone to read each outlet's own contact page; I will not guess or copy addresses from elsewhere. Run on the current 510 organisations the new check reports 0 problems.

## Follow-ups from security (2026-11-26T06:19Z)
Done in the patch: phone-like numbers refused in any text of the contact (how, email); com.pt, org.pt, gov.pt, edu.pt treated as second levels, with tests (11 pass). Security: ship after cl-6.dev reviews the gate. Waiting for dev (asked the conductor, no link to that session).

## Shipped (2026-11-26T06:26Z)
Gate live: website commit 0000dfbbc (v0.1.2296), with cl-6.dev's three follow-ups (ISO date not a phone, page-only contacts checked for https and read date, shared hosts never an outlet's own domain); 14 tests. rtp-noticias lost its contact block (page 404 on http and https; commit 8896de773). No outlet record carries an address yet: the batch waits for Dinis's own word (conductor, via researcher@).
