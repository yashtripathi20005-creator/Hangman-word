"""
Hangman ASCII Art Display
"""
class HangmanDisplay:
    """Handles the visual display of the hangman."""
    
    HANGMAN_STAGES = [
        # Stage 0: No mistakes
        """
           _______
          |       |
          |       
          |      
          |     
          |    
          |
        ============
        """,
        
        # Stage 1: Head
        """
           _______
          |       |
          |       O
          |      
          |     
          |    
          |
        ============
        """,
        
        # Stage 2: Head + Body
        """
           _______
          |       |
          |       O
          |       |
          |     
          |    
          |
        ============
        """,
        
        # Stage 3: Head + Body + Left Arm
        """
           _______
          |       |
          |       O
          |      /|
          |     
          |    
          |
        ============
        """,
        
        # Stage 4: Head + Body + Both Arms
        """
           _______
          |       |
          |       O
          |      /|\\
          |     
          |    
          |
        ============
        """,
        
        # Stage 5: Head + Body + Both Arms + Left Leg
        """
           _______
          |       |
          |       O
          |      /|\\
          |      /
          |    
          |
        ============
        """,
        
        # Stage 6: Complete hangman
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / \\
          |    
          |
        ============
        """
    ]
    
    def show_hangman(self, mistakes):
        """Display the hangman ASCII art for the given number of mistakes."""
        if mistakes < 0:
            mistakes = 0
        elif mistakes >= len(self.HANGMAN_STAGES):
            mistakes = len(self.HANGMAN_STAGES) - 1
            
        print(self.HANGMAN_STAGES[mistakes])
