"""
Utility functions for Hangman game
"""
import re


def validate_guess(guess, guessed_letters):
    """
    Validate a player's letter guess.
    Returns (is_valid, message)
    """
    if not guess:
        return False, "⚠️ Please enter a guess."
    
    if len(guess) != 1:
        return False, "⚠️ Please enter only one letter."
    
    if not guess.isalpha():
        return False, "⚠️ Please enter a letter (A-Z)."
    
    if guess.upper() in guessed_letters:
        return False, f"⚠️ You already guessed '{guess.upper()}'. Try a different letter."
    
    return True, "Valid guess."


def get_difficulty_level():
    """Get difficulty level from player."""
    while True:
        print("\nSelect difficulty level:")
        print("  1. Easy (8 attempts)")
        print("  2. Medium (6 attempts)")
        print("  3. Hard (5 attempts)")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")


def format_time(seconds):
    """Format seconds into MM:SS format."""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"
