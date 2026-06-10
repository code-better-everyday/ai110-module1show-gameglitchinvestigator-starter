# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Fixed inverted hints in `check_guess`: "Too High" now correctly says "Go LOWER" and "Too Low" says "Go HIGHER".
2. Fixed secret-as-string bug in `app.py`: removed the even/odd attempt block that converted the secret number to a string, causing comparisons to fail and hints to be wrong on every other guess.
3. Fixed wrong Hard difficulty range in `get_range_for_difficulty`: Hard was 1–50 (easier than Normal), corrected to 1–200. Also fixed hardcoded "1 to 100" info text to use the actual `low`/`high` values.
4. Fixed New Game button ignoring difficulty in `app.py`: was always generating a secret with `randint(1, 100)`, now uses the correct `low`/`high` range for the selected difficulty.
5. Fixed attempts counter initializing to 1 instead of 0 in `app.py`: caused "Attempts left" to show one fewer than correct and go negative past the limit.

**Screenshot** *(optional)*: ![alt text](image.png)

## 🧪 Test Results

```
pytest tests/ -v
============================= test session starts =============================
platform win32 -- Python 3.13.13, pytest-9.0.3
collected 3 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 33%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 66%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [100%]

============================== 3 passed in 0.10s ==============================
```

## 🚀 Stretch Features

- [x] Enhanced UI implemented:
  - Fixed misleading caption ("Something is off." → "Debugged and playable.")
  - Added score, attempts-left, and difficulty metrics row at the top
  - Added progress bar that fills as attempts are used; warns with ⚠️ in the last 2 attempts
  - Color-coded hints: green (win), yellow (too high), blue (too low)
  - Guess history table shown below the game, listing every guess and its result
  - Win triggers balloons animation; game-end state shows colored success/error banner
