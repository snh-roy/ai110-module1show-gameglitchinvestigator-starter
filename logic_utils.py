def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
        return True, value, None
    except (ValueError, TypeError):
        return False, None, "That is not a number."


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    
    # FIX: Corrected inverted hints (Higher guess -> "Too High", Lower guess -> "Too Low")  # Collaboration: used Copilot suggestions and verified with tests
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        return current_score + max(points, 10)

    # FIX: Corrected scoring logic to consistently subtract points for wrong guesses  # Collaboration: used Copilot suggestion; verified behavior with tests
    if outcome in ["Too High", "Too Low"]:
        return current_score - 5

    return current_score
