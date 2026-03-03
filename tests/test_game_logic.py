import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty

def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_invalid():
    ok, value, err = parse_guess("not-a-number")
    assert ok is False
    assert value is None
    assert "not a number" in err.lower()

def test_update_score_win():
    # Base score 0, Win on attempt 1: 100 - 10*1 = 90
    new_score = update_score(0, "Win", 1)
    assert new_score == 90

def test_update_score_wrong():
    # Base score 10, Too High: 10 - 5 = 5
    new_score = update_score(10, "Too High", 1)
    assert new_score == 5

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
