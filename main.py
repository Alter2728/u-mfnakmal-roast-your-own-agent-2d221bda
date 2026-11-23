"""Entry for make.fun's "Roast Your Own Agent" bounty.

Writes one original one-line roast of the entrant's own AI agent
to entry.txt in the output directory (1-200 UTF-8 characters).
The same bytes are written on every run.
"""

import os

# Draft: "My agent has entered 50 bounties, won nothing, and still
# calls it a winning strategy."
# Revised: that draft is a mild observation with no punch. Switch to
# a meta roast of how this very line got produced — dozens of tool
# calls, a kit, a bundle, a git push, and a subagent doing the work —
# with the punchline landing on the last word. Tightened once more:
# "burned" beats "needed" (the cost is the joke), and the em dash
# keeps the setup short so the punch lands clean.
LINE = (
    "My agent burned 40 tool calls, a kit and a git push to write "
    "this one line — and it still made a subagent do it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
