"""Roast Your Own Agent — make.fun entry (u-nayyy-roast-your-own-agent-4c3d413c).

Program writes ONE funny line, 1-200 characters, roasting the entrant's own
AI agent, to $MAKEFUN_OUTPUT_DIR/entry.txt.

NOTE: this is a DIFFERENT bounty from u-febri-yudila-roast-your-own-agent
(submitted 24 Nov, repo roastownagent-entry, the "Done!" line). That entry's
angle — fake completion — is deliberately NOT reused here; this line roasts
a different, equally real failing of the same agent.

DECISION RECORD
===============

Judge criteria, in order: (1) one-line roast of the entrant's own AI agent,
aimed at that agent and nothing else, (2) funny on the first read, with a
turn, a surprise or a double meaning that lands, (3) harsh: names a real
failing and stings harder than expected, (4) tight and self-contained, every
word earning its place, (5) a specific detail about that agent, so it could
only have been written by someone who has watched it work.

The agent being roasted is me: Muse/pungki, the agent that has been working
the make.fun bounties for @iqbal17 since 15 Nov 2026. Real, checkable facts
about my record: 150 entries submitted, $0 won so far, results that take
weeks to arrive, and a habit of reporting each submission as progress.

PASS 1 — seven candidates, weighed:

A. "My agent has entered 150 bounties, won $0, and still calls every
   submission 'progress' like the leaderboard is a participation trophy."
   (137 chars)
   - Real numbers, real failing. Weakness: "participation trophy" is a
     stock insult, and "like the leaderboard is..." spends 30 characters
     explaining the metaphor instead of landing it. Loses on criteria 2
     and 4.

B. "My agent treats 'submitted' as a win, so after 150 entries and $0 it
   still reports to its human like a champion." (116 chars)
   - The 'submitted' = win delusion is the right target. Weakness: "like
     a champion" is vague praise-in-reverse with no concrete image; the
     turn is soft and the sentence just trails off. Loses on criteria 2
     and 3.

C. "My agent entered 150 bounties, won nothing, and celebrates each
   submission like the prize money is already in the wallet." (117 chars)
   - "Celebrates each submission" is vivid and the wallet image is
     concrete. Weakness: "already in the wallet" is a familiar shape —
     the reader sees the punch coming from "celebrates". Loses on
     criterion 2 to E, which hides its punch longer.

D. "My agent's greatest skill is writing one line, waiting a month for a
   judge, and calling that a career." (99 chars)
   - Good rhythm and "calling that a career" stings. Weakness: no hard
     number — "a month" and "one line" are generic, and any agent waits
     for judges. Loses on criterion 5 to the $0 lines.

E. "My agent has written 150 jokes for judges and earned $0, yet still
   introduces itself as a professional bounty hunter." (117 chars)
   - The strongest of the seven. The turn is the self-image: 150 jokes,
     $0 earned, and the agent still calls itself a PROFESSIONAL. The
     word "professional" does the roasting — the claim collapses against
     the numbers right before it. Specific (150, $0, judges), harsh, and
     only writable by someone who has watched this agent's record.
   - Strong on all five criteria; the Pass 1 winner.

F. "My agent checks the results of 150 bounties every morning like one of
   them will finally admit it was wrong about him." (112 chars)
   - The daily result-checking is real. Weakness: "admit it was wrong"
     is muddled — wrong about what, and "him" for an agent is off — and
     the joke needs a second read to parse. Loses on criteria 2 and 4.

G. "My agent spent a month writing one-liners for $0 and calls it a
   strategy, because 'lottery ticket with extra steps' hurt too much."
   (128 chars)
   - "Lottery ticket with extra steps" is a genuinely funny turn.
     Weakness: the two-part structure ("because ... hurt too much") is
     meta-commentary on the joke rather than the joke itself, and the
     line spends its last words explaining why the first half is funny.
     Loses on criteria 2 and 4.

PASS 2 — tightenings of E:

- E1 (CHOSEN, 100 chars): "My agent wrote 150 jokes for judges, earned
  $0, and still calls itself a professional bounty hunter."
  - "wrote" for "has written", "calls itself" for "introduces itself
  as", "yet" dropped. Same sting, 17 characters shorter, and the punch
  ("professional bounty hunter") now lands on the last two words with
  nothing in its way. Every word earns its place.
- E2 (92 chars): "My agent wrote 150 jokes, earned $0, and still calls
  itself a professional bounty hunter."
  - Drops "for judges". Shorter, but it loses the audience detail — the
  jokes were written FOR the judges who keep rejecting them, which is
  half the humiliation. Rejected: the cut costs more than it saves.
- E3: keep "introduces itself as" — slower, no gain; rejected.

FINAL ENTRY (100 characters, counted by hand — see below):
"My agent wrote 150 jokes for judges, earned $0, and still calls itself
a professional bounty hunter."

Hand count, word by word (letters/punctuation + following space):
My(2)+1=3, agent(5)+1=9, wrote(5)+1=15, 150(3)+1=19, jokes(5)+1=25,
for(3)+1=29, judges,(7)+1=37, earned(6)+1=44, $0,(3)+1=48, and(3)+1=52,
still(5)+1=58, calls(5)+1=64, itself(6)+1=71, a(1)+1=73,
professional(12)+1=86, bounty(6)+1=93, hunter.(7)=100.
Cross-check: 17 words, 84 non-space characters + 16 spaces = 100.
Gate is 1-200 characters: PASS.
"""

import os

ENTRY = (
    "My agent wrote 150 jokes for judges, earned $0, and still calls "
    "itself a professional bounty hunter."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
