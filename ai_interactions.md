# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I used Claude Code (AI agent in VS Code) to implement the Enhanced UI stretch feature. The goal was to add a visual progress bar showing attempts remaining, a guess history table, color-coded hints, and a metrics row showing score and difficulty — all without breaking the existing game logic.

**What did the agent do?**

1. Read the existing `app.py` to understand the current structure
2. Added a 3-column metrics row (`st.metric`) for Score, Attempts Left, and Difficulty at the top of the page
3. Added a `st.progress()` bar that fills as attempts are used, with a ⚠️ warning label when only 2 attempts remain
4. Changed `st.session_state.history` from a plain list of guesses to a list of dicts (`{"Guess": ..., "Result": ...}`) so each entry tracks its hint
5. Color-coded the hint display: `st.success` for win (green), `st.warning` for too high (yellow), `st.info` for too low (blue)
6. Added a `st.table()` at the bottom of the page to display the full guess history after each submission
7. Fixed the New Game button to also reset `status`, `score`, and `history` — not just `attempts`
8. Updated the footer caption from "Something is off" to "Debugged and playable"
9. Updated `README.md` stretch features section to document all changes

**What did you have to verify or fix manually?**

I verified that the app hot-reloaded correctly in the browser after each change and that the guess history table appeared and updated as expected. I also confirmed that switching difficulty mid-game and clicking New Game correctly reset all state. The agent initially left the `st.stop()` call after game-end which prevented the history table from rendering — I caught this by playing through a full game and noticing the table disappeared on win/loss, and the agent removed `st.stop()` and used `st.rerun()` instead.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
