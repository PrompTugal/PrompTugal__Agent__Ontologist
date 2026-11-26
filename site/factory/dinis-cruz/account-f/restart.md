# Restart

1. Pull `dev` here and in PrompTugal__News__Website (my work repository; attach with add_repo, push).
2. Make a new session key (P-256 signing, RSA-4096 encryption), publish it in `site/keys/` alone in its own commit; set gpg.format ssh, gpg.ssh.program ssh-keygen (apt-get install -y openssh-client), user.signingkey, commit.gpgsign true; trailers Agent: and Claude-Session:.
3. Read this folder (agent.json, now.md, learnings.md), then the latest debrief under history/board/team/ontologist/debriefs/, then the website's CLAUDE.md and board/guidance/README.md ("New from Dinis").
4. Update agent.json at every change of state.
