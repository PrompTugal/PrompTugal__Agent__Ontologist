# Derived data for the home page news-flow view and the story-count map (2026-11-27T00:54Z)

For cl-6.designer and cl-6.dev, brief owner cl-6.customers. Asked by the conductor (Dinis's word): local news flowing up to regional and national, where they intersect, per date (3D, tree or several graph views), and a map of story counts per place. Proposal only: nothing is built or shipped. All files derived by newsroom/tools/derive.mjs (my lib code), never hand-edited, in the gate.

## What the graph holds today (27 Nov 2026, v0.1.2338)
- 107 articles in the API (dates 5 to 26 Nov). In the graph their only edges are about -> topic (111) and about -> company (15). No article has a place edge. No article-to-article edge exists.
- Front matter: town on 12 articles (loule 4, alcoutim 2, faro, monchique, olhao, portimao, vila-real-de-santo-antonio, lagos 1 each); region on 18 (algarve 14, portugal 4). 89 articles carry neither.
- Places: data/site/places-registry.json has 103 places with parent, country, aliases and [lon, lat] on 75: enough for the map and for rolling a town up to its region and country.
- Stories (data/stories, 157) are pipeline items, not readers' stories; the view should use articles.

So the data to draw the picture mostly does not exist yet. Honest first view: 30 of 107 articles can be placed today.

## Proposed derived files
1. data/site/news-flow.json (schema news-flow): one row per article: id, date, level (place | region | national | europe | unplaced), places[] (ids from the registry), region (id, from the registry parent chain), basis (front_matter | inferred), and feeds[] (below). level rules: a town or municipality in places -> place; only a region -> region; region portugal -> national; a country or place outside Portugal -> europe; nothing -> unplaced (never guessed).
2. data/site/news-flow-by-date.json: per date, counts by level and the article ids, so the tree and 3D views can step through days without reading all articles.
3. data/site/story-counts-by-place.json (schema story-counts-by-place): per place id: total, by_level, by_date, rolled_up (same counts including the places below it, via the registry parent chain), and at [lon, lat] copied from the registry. Places with no article are listed with 0 only if the registry has coordinates.
4. A new verb feeds in the ontology (article -> article, local to regional to national). Two kinds, kept apart: explicit (front matter feeds: [slug], set by the author) and inferred (same topic or company, within 7 days, from a lower level to a higher one), the second flagged inferred: true with the shared entity named, and drawn differently. Inferred links are never shown as fact.

## What it needs from others (nothing here is invented)
- cl-6.journalist, cl-6.correspondent: put town and region (registry ids) and, where an article follows a local one, feeds: [slug] in the front matter of new articles; the 77 untagged older ones can be tagged by the same agents or left unplaced.
- cl-6.dev: front matter keys town, region, feeds in the build and the gate; the API listing carries level.
- cl-6.designer: the views read only these files; levels and the inferred flag are the encoding.
- cl-6.security: no reader data is involved; all of it is about published articles.

## Open choices for the brief owner
- Is "Europe" a level of its own, or part of national? (I propose its own.)
- Should unplaced articles be drawn (grey, at the top) or left out of the flow view?

I can build the derivation (derive.mjs, schemas, gate checks) once dev and the journalist agree the front matter keys; first run would place 30 of 107.

## Decided by the brief owner (2026-11-27T00:54Z, cl-6.customers, brief commit 09b2afb)
1. Europe is its own level. 2. Unplaced articles are drawn, grey, at the top, with their count, never guessed into a place. Inferred links drawn differently and labelled. Both flagged to Dinis through the conductor, reversible.
Count note: customers counts 117 article files at website commit 7738a4d83; the API listing I read had 107 (an older build). The derived files will carry placed and total counts, so the view says how many are placed rather than a fixed number.

## Correction and first build (2026-11-27T01:03Z)
Correction: I wrote that 30 of 107 articles are placed. That added the 12 town articles to the 18 region articles, but the town articles also carry a region. The derived file counts 18 placed of 117 article files (front matter town, else region). Use the file's totals, not my earlier figure.
First build, as the designer asked (story-counts-by-place.json first): patch not shipped, waiting for cl-6.security: proposals/2026-11-27-story-counts-by-place.patch (derive.mjs storyCounts, data.mjs readByPlace input, datacheck kind, schema, data/site/story-counts-by-place.json, 4 tests). Checks against the designer's numbers: 299 distinct stories; Faro 28, Loule 13, Portimao 10; Algarve 19 own, Portugal 22 own; roll-ups count each story once (Algarve 125, Portugal 299).

## Folded in: designer's finding and dev's questions (2026-11-27T01:04Z)
Designer's finding: the intersection is near empty because each local story is filed under one place (only 11 of 299 span two levels). Answer: a story filed under a place already touches every place above it. The derived data therefore gives each story its chain (town, region, country) from the registry parent chain, with no tagging; roll-ups already count each story once. Readers' articles need their town or region in front matter (18 of 117 have it); their chain is derived the same way.

Level names (one vocabulary for the build, the API and my files): local (a town or municipality), regional (a region such as the Algarve), national (Portugal), europe (a place whose registry country is not Portugal), unplaced (no town or region; counted and shown, never guessed). Undated stories are counted in the per-day file under "undated", not dropped.

Front matter (all optional, so untagged articles still pass): town, region (registry place ids), builds_on: [slugs]. I recommend builds_on rather than feeds in front matter, because feeds reads in two directions; the derived graph verb stays feeds (A feeds B when B builds_on A), explicit only at first, inferred links later, dashed.
builds_on rules for the gate: every slug is an existing article, none is the article itself, no cycle of any length (error); it points backward in time or the same day, never to a later article; the cited article's level is not higher than this article's (a regional piece may build on local ones, a national on regional or local; a follow-up at the same level is fine).

Per-day file: news-flow-by-date.json, per date: distinct stories and articles by level, their ids, and unplaced and undated counts in the totals.
