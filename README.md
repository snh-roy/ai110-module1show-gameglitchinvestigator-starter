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

This project is a simple number-guessing game built with Streamlit where the player chooses a difficulty and attempts to guess a secret number within a constrained range.

Bugs found: inverted hint logic (hints told players to go higher when their guess was already higher), instruction text not reflecting the selected difficulty range, scoring that sometimes increased on wrong guesses, and a type mismatch that could break comparisons.

Fixes applied: corrected the hint comparisons and messages in `logic_utils.check_guess`, fixed scoring to consistently deduct points for incorrect guesses, ensured the new game reset uses the selected difficulty range, removed any secret-type flipping, and added focused pytest tests in `tests/test_game_logic.py` to prevent regressions.

Verification: ran `pytest` (8 passed) and manually played the app with `streamlit run app.py` to confirm stable secret numbers, correct hints, and expected scoring. See `reflection.md` for a detailed account of AI-assisted debugging.

## 📸 Demo

- Run the app locally: `pip install -r requirements.txt && streamlit run app.py`
- Automated tests: run `pytest` (the suite reports `8 passed`).
- Screenshot: Add a screenshot of the fixed game UI here (or view the app at http://localhost:8501 when running locally).

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
