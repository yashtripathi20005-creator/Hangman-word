"""
Hangman Game Logic
"""
import random
from words import WORD_LIST, CATEGORIES
from display import HangmanDisplay
from utils import validate_guess, get_difficulty_level


class HangmanGame:
    """Main game class handling all game logic."""
    
    def __init__(self):
        self.word = ""
        self.category = ""
        self.difficulty = "medium"
        self.max_attempts = 6
        self.remaining_attempts = 6
        self.guessed_letters = set()
        self.correct_guesses = set()
        self.hint_used = False
        self.display = HangmanDisplay()
        self.score = 0
        self.games_played = 0
        self.games_won = 0
    
    def select_word(self):
        """Select a random word and its category based on difficulty."""
        self.difficulty = get_difficulty_level()
        
        # Adjust max attempts based on difficulty
        if self.difficulty == "easy":
            self.max_attempts = 8
        elif self.difficulty == "medium":
            self.max_attempts = 6
        else:  # hard
            self.max_attempts = 5
            
        self.remaining_attempts = self.max_attempts
        
        # Get word list for selected difficulty
        word_pool = WORD_LIST.get(self.difficulty, WORD_LIST["medium"])
        
        # Select random word and its category
        entry = random.choice(word_pool)
        self.word = entry["word"].upper()
        self.category = entry["category"]
        
        # Reset game state
        self.guessed_letters = set()
        self.correct_guesses = set()
        self.hint_used = False
    
    def get_display_word(self):
        """Return the word with unguessed letters hidden."""
        display = []
        for letter in self.word:
            if letter in self.correct_guesses:
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
    
    def is_word_guessed(self):
        """Check if the entire word has been guessed."""
        return all(letter in self.correct_guesses for letter in self.word)
    
    def make_guess(self, guess):
        """Process a player's guess."""
        guess = guess.upper()
        
        # Validate guess
        is_valid, message = validate_guess(guess, self.guessed_letters)
        if not is_valid:
            return False, message
        
        self.guessed_letters.add(guess)
        
        if guess in self.word:
            self.correct_guesses.add(guess)
            if self.is_word_guessed():
                return True, "🎉 Congratulations! You guessed the word!"
            return True, f"✅ Good guess! '{guess}' is in the word."
        else:
            self.remaining_attempts -= 1
            return True, f"❌ Sorry, '{guess}' is not in the word."
    
    def give_hint(self):
        """Provide a hint by revealing a random unguessed letter."""
        if self.hint_used:
            return "⚠️ Hint already used for this word!"
        
        unguessed = [l for l in self.word if l not in self.correct_guesses]
        if not unguessed:
            return "No letters to reveal!"
        
        # Reveal a random unguessed letter
        import random
        letter = random.choice(unguessed)
        self.correct_guesses.add(letter)
        self.guessed_letters.add(letter)
        self.hint_used = True
        self.remaining_attempts -= 1  # Penalty for using hint
        
        return f"💡 Hint: The letter '{letter}' is in the word. (-1 attempt)"
    
    def play_round(self):
        """Play a single round of Hangman."""
        self.select_word()
        
        print(f"\n📚 Category: {self.category}")
        print(f"🎯 Difficulty: {self.difficulty.capitalize()}")
        print(f"💖 Attempts: {self.remaining_attempts}")
        print(f"\nWord: {self.get_display_word()}\n")
        
        while self.remaining_attempts > 0 and not self.is_word_guessed():
            # Show current state
            self.display.show_hangman(self.max_attempts - self.remaining_attempts)
            print(f"\nWord: {self.get_display_word()}")
            print(f"📝 Guessed letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
            print(f"❤️ Remaining attempts: {self.remaining_attempts}")
            
            # Get player input
            print("\nOptions:")
            print("  1. Guess a letter")
            print("  2. Guess the whole word")
            print("  3. Get a hint (-1 attempt)")
            print("  4. Quit game")
            
            choice = input("\nChoose an option (1-4): ").strip()
            
            if choice == "1":
                guess = input("Enter a letter: ").strip()
                success, message = self.make_guess(guess)
                print(f"\n{message}\n")
                
            elif choice == "2":
                guess = input("Enter your word guess: ").strip().upper()
                if guess == self.word:
                    self.correct_guesses = set(self.word)
                    print(f"\n🎉 Perfect! The word was '{self.word}'!\n")
                    break
                else:
                    self.remaining_attempts -= 1
                    print(f"\n❌ Wrong! The word is not '{guess}'. (-1 attempt)\n")
                    
            elif choice == "3":
                print(f"\n{self.give_hint()}\n")
                
            elif choice == "4":
                print(f"\n👋 Thanks for playing! The word was '{self.word}'.")
                return False
                
            else:
                print("\n⚠️ Invalid choice. Please try again.\n")
        
        # Round result
        if self.is_word_guessed():
            self.games_played += 1
            self.games_won += 1
            self.score += self.remaining_attempts * 10
            self.display.show_hangman(self.max_attempts - self.remaining_attempts)
            print(f"\n🎉 You won! The word was '{self.word}'!")
            print(f"⭐ Score for this round: {self.remaining_attempts * 10} points")
            return True
        elif self.remaining_attempts == 0:
            self.games_played += 1
            self.display.show_hangman(self.max_attempts)
            print(f"\n💀 Game Over! The word was '{self.word}'.")
            return False
        
        return True
    
    def play(self):
        """Main game loop."""
        while True:
            self.play_round()
            
            print("\n" + "="*50)
            print(f"📊 Overall Stats:")
            print(f"   Games Played: {self.games_played}")
            print(f"   Games Won: {self.games_won}")
            print(f"   Win Rate: {self.games_won/self.games_played*100:.1f}%" if self.games_played > 0 else "   Win Rate: N/A")
            print(f"   Total Score: {self.score}")
            print("="*50)
            
            play_again = input("\n🔄 Play again? (yes/no): ").strip().lower()
            if play_again not in ['yes', 'y']:
                print("\n👋 Thanks for playing Hangman! Goodbye!")
                break
