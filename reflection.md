# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game it was completely unwinnable. The hints were backwards — if my guess was too high it told me to go higher, which sent me in the wrong direction every time. On top of that, every other guess seemed to give random results because the secret number was being silently converted to a string on even attempts, so the comparison broke entirely. The attempts counter also started at 1 instead of 0, which meant "Attempts left" showed one fewer than it should and eventually went negative if you kept playing past the limit.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60, secret is 50 | Hint says "Go LOWER" (guess too high) | Hint said "Go HIGHER" (inverted logic) | No error — silent wrong answer |
| Any guess on an even attempt | Compare guess to secret number (int) | Secret silently cast to string; int vs str comparison fails | TypeError caught internally, string comparison used instead |
| Select Hard difficulty, start game | Range 1–200, 5 attempts | Range was 1–50 (easier than Normal) and New Game ignored difficulty | No error — silent wrong range |

---

## 2. How did you use AI as a teammate?

I used Claude Code for fixing the bugs and Gemini and GitHub Copilot for fixing the virtual environment and Streamlit issues. It was great overall. Claude Code correctly identified the inverted Higher/Lower hints and the even/odd string conversion bug, which I verified by playing the game and watching the hints change correctly. One misleading moment was that the old Streamlit process from a previous project was still running on port 8501, so I thought my fixes weren't working — the AI helped me realize I needed to kill the old process first.

---

## 3. Debugging and testing your fixes

I tested the Higher/Lower hints manually by opening the Developer Debug Info tab to see the secret number, then entering guesses above and below it to confirm the hints pointed the right way. I also ran `pytest tests/` after refactoring the logic into `logic_utils.py`, and all three tests passed — `test_winning_guess`, `test_guess_too_high`, and `test_guess_too_low`. Seeing the tests go green confirmed the logic was correct, not just that the UI looked right.

---

## 4. What did you learn about Streamlit and state?

That was odd — pun intended. Every time you click a button, Streamlit reruns the entire script from line 1, so any regular variable resets unless it is stored in `st.session_state`. The secret number was already protected by session_state, but on every even-numbered attempt the code was silently converting it to a string before comparing, which broke the logic entirely. Once I understood that session_state is the only thing that survives a rerun, the bug made complete sense.

---

## 5. Looking ahead: your developer habits

- I got better at managing virtual environments. VS Code does a great job of activating the venv by default when you open a folder, but I learned to make sure I deactivate the old one and activate the correct new one for each project.
- I was running my old Streamlit app from last week's music catalog assignment in the background, which was holding port 8501. My new app started on a different port and I couldn't figure out why my fixes weren't showing up. Going forward I will always check for stale background processes before debugging a "not updating" issue.

