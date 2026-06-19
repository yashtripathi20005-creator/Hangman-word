"""
Hangman Word Guessing Game - Main Entry Point
"""
from game import HangmanGame


def main():
    """Main function to run the Hangman game."""
    print("\n" + "="*50)
    print("     WELCOME TO HANGMAN WORD GUESSING GAME")
    print("="*50 + "\n")
    
    game = HangmanGame()
    game.play()


if __name__ == "__main__":
    main()
