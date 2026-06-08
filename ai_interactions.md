# ai_interactions.md: documentation of ai agent workflows, test generation, and model comparisons.
# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Identify and fix remaining bugs in the game logic and UI, specifically targeting the difficulty range inconsistencies, negative scoring, and state desync when changing difficulty levels.

**What did the agent do?**

1.  Researched the codebase using `grep_search` and `read_file`.
2.  Modified `tests/test_game_logic.py` to add reproduction cases for the bugs.
3.  Updated `logic_utils.py` to fix the "Hard" range (1-200) and prevent negative scores in `update_score`.
4.  Updated `app.py` to add a difficulty change listener that resets the game state.
5.  Ran `pytest` to verify all fixes.

**What did you have to verify or fix manually?**

I manually verified that the `st.rerun()` logic in `app.py` correctly handles the first-time initialization of the difficulty state to avoid unnecessary reruns on page load.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative Scoring | "How do I test that the score never drops below zero?" | `test_update_score_no_negative` | Yes | Scores should be non-negative for better user experience. |
| Hard Range | "Ensure Hard difficulty is actually harder than Normal." | Updated `test_difficulty_ranges` | Yes | The Hard range should be significantly larger (1-200) than Normal (1-100). |
| Empty Input | "Test parsing an empty string for the guess." | `test_parse_guess_invalid` (with empty) | Yes | Graceful error handling for empty inputs prevents crashes. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Refactor get_range_for_difficulty to be more concise.
```

**Linting output before:**

```
No errors, but repetitive if statements.
```

**Changes applied:**

Simplified the lookup logic and added a default return value to make the function more robust.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

"Refactor the score update logic to handle multiple win conditions."

| | Model A | Model B |
|-|---------|---------|
| **Model name** | Claude Sonnet 4.6 | GPT-4o |
| **Response summary** | Used a dictionary lookup for outcomes. | Used a large switch/case-like if-elif block. |
| **More Pythonic?** | Yes | No |
| **Clearer explanation?** | Yes | Yes |

**Which did you prefer and why?**

Claude Sonnet 4.6, as the dictionary-based approach is cleaner and more extensible than a long chain of if-statements.
