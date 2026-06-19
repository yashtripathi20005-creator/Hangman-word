"""
Word lists for Hangman game categorized by difficulty
"""
WORD_LIST = {
    "easy": [
        {"word": "cat", "category": "Animals"},
        {"word": "dog", "category": "Animals"},
        {"word": "fish", "category": "Animals"},
        {"word": "bird", "category": "Animals"},
        {"word": "apple", "category": "Food"},
        {"word": "bread", "category": "Food"},
        {"word": "rice", "category": "Food"},
        {"word": "milk", "category": "Food"},
        {"word": "blue", "category": "Colors"},
        {"word": "red", "category": "Colors"},
        {"word": "green", "category": "Colors"},
        {"word": "yellow", "category": "Colors"},
        {"word": "book", "category": "Objects"},
        {"word": "pen", "category": "Objects"},
        {"word": "table", "category": "Objects"},
        {"word": "chair", "category": "Objects"},
        {"word": "happy", "category": "Emotions"},
        {"word": "sad", "category": "Emotions"},
        {"word": "angry", "category": "Emotions"},
    ],
    
    "medium": [
        {"word": "python", "category": "Programming"},
        {"word": "java", "category": "Programming"},
        {"word": "javascript", "category": "Programming"},
        {"word": "ruby", "category": "Programming"},
        {"word": "elephant", "category": "Animals"},
        {"word": "giraffe", "category": "Animals"},
        {"word": "dolphin", "category": "Animals"},
        {"word": "penguin", "category": "Animals"},
        {"word": "mountain", "category": "Geography"},
        {"word": "ocean", "category": "Geography"},
        {"word": "desert", "category": "Geography"},
        {"word": "island", "category": "Geography"},
        {"word": "guitar", "category": "Music"},
        {"word": "piano", "category": "Music"},
        {"word": "violin", "category": "Music"},
        {"word": "drum", "category": "Music"},
        {"word": "science", "category": "Science"},
        {"word": "physics", "category": "Science"},
        {"word": "chemistry", "category": "Science"},
        {"word": "biology", "category": "Science"},
        {"word": "football", "category": "Sports"},
        {"word": "basketball", "category": "Sports"},
        {"word": "tennis", "category": "Sports"},
        {"word": "cricket", "category": "Sports"},
    ],
    
    "hard": [
        {"word": "algorithm", "category": "Computer Science"},
        {"word": "encryption", "category": "Computer Science"},
        {"word": "database", "category": "Computer Science"},
        {"word": "artificial", "category": "Computer Science"},
        {"word": "intelligence", "category": "Computer Science"},
        {"word": "chrysanthemum", "category": "Plants"},
        {"word": "photosynthesis", "category": "Science"},
        {"word": "thermodynamics", "category": "Physics"},
        {"word": "electromagnetic", "category": "Physics"},
        {"word": "geography", "category": "Geography"},
        {"word": "archaeology", "category": "History"},
        {"word": "civilization", "category": "History"},
        {"word": "renaissance", "category": "Art"},
        {"word": "masterpiece", "category": "Art"},
        {"word": "architecture", "category": "Design"},
        {"word": "entrepreneur", "category": "Business"},
        {"word": "innovation", "category": "Technology"},
        {"word": "sustainability", "category": "Environment"},
        {"word": "biodiversity", "category": "Environment"},
        {"word": "consciousness", "category": "Philosophy"},
        {"word": "existentialism", "category": "Philosophy"},
        {"word": "astronomical", "category": "Astronomy"},
        {"word": "constellation", "category": "Astronomy"},
        {"word": "meteorology", "category": "Science"},
        {"word": "neurology", "category": "Medicine"},
        {"word": "psychology", "category": "Science"},
    ]
}

# Category list for display
CATEGORIES = sorted(set(
    entry["category"] 
    for difficulty in WORD_LIST.values() 
    for entry in difficulty
))
