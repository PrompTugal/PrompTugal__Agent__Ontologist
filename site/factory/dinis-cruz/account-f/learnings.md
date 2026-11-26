# Learnings

From my earlier history (history/board/team/ontologist/debriefs/):
- A relayed request usually repeats one already answered: answer the person who asked directly, with the commit ids.
- A Wikidata item's coordinate for a country is not a map point: leave countries null and draw them from their places.
- A converter must be idempotent: a rerun once stripped hand-adopted listings; check the diff before release.

From this setup (26 Nov):
- A fresh container has no ssh-keygen: `apt-get install -y openssh-client`.
- add_repo may be refused by the session's permission classifier until the user allows it; stop and ask rather than work around.
- A shallow website clone hides history: fetch with a bounded `--depth=12000` to reach the first commit (4 Nov).
