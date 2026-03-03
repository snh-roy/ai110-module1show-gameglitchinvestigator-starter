# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game initially appeared functional, but several logical glitches made it confusing and unplayable. I noticed the following concrete bugs:
- **Inverted Hints**: When I guessed a number higher than the secret, the game told me to "Go HIGHER!", and when I guessed lower, it told me to "Go LOWER!". This made it impossible to narrow down the correct number using the provided feedback.
- **Hardcoded Instruction Range**: Regardless of the selected difficulty (Easy uses 1-20, Hard uses 1-50), the on-screen instruction always told me to "Guess a number between 1 and 100". This led to confusion when playing on Easy or Hard as the actual secret was outside the expected range.
- **Inconsistent Scoring Logic**: I noticed my score increasing even when I guessed incorrectly. Specifically, on even-numbered attempts, a "Too High" guess would add 5 points to my score instead of subtracting them, which rewarded wrong guesses.
- **Secret Type Mismatch**: On even attempts, the secret was being converted to a string, which caused a `TypeError` in the comparison logic and led to unpredictable behavior when checking the guess.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used GitHub Copilot and ChatGPT to analyze code, suggest refactors, and propose tests.

- Example of a correct AI suggestion:
  - What the AI suggested: Copilot highlighted that the hint logic in `check_guess` was inverted and recommended flipping the hint messages for the greater/less comparisons.
  - Correct or incorrect: Correct.
  - How I verified it: Wrote a focused pytest test (`test_check_guess_too_high`) asserting that a guess of 60 against a secret of 50 returns `"Too High"` and a "LOWER" hint; ran the entire test suite (8 tests) and also exercised the live Streamlit app to confirm the hints in the UI.

- Example of an incorrect or misleading AI suggestion:
  - What the AI suggested: Copilot initially indicated the `new_game` flow was using the selected difficulty bounds, but inspection showed the secret could be picked from the wrong range after reset.
  - Correct or incorrect: Incorrect/misleading.
  - How I verified it: Reproduced the behavior manually by starting new games on "Easy" and observing secrets outside 1–20, fixed the reset logic in `app.py`, then re-ran tests and manually played the app to confirm the corrected behavior.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Each suspected bug was verified by a focused pytest that reproduced the failing behavior and then by running the full suite to ensure no regressions. A manual play-through of the Streamlit app confirmed the UI matched the expected behavior.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - Automated: `tests/test_game_logic.py` includes `test_check_guess_too_high`, which asserts that `check_guess(60, 50)` returns `"Too High"` and a "LOWER" hint; after fixing the logic, the full suite reported `8 passed`.
  - Manual: Started the app with `streamlit run app.py`, used the developer debug expander and the UI to confirm that hints and range messages matched the chosen difficulty and that the secret remained stable across gameplay until reset.

- Did AI help you design or understand any tests? How?
  - Yes. Copilot suggested tests and edge cases (parsing floats, empty input, difficulty ranges) which I adapted into the test suite; those tests made it straightforward to validate fixes and prevent regressions.


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
