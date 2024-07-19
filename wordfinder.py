"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    """Machine for finding random words from a dictionary file."""
    
    def __init__(self, filepath):
        """Initializes the WordFinder with a file path and reads words from the file."""
        # Open the file and read words
        try:
            with open(filepath, 'r') as file:
                self.words = self.read_words(file)
            print(f"{len(self.words)} words read")
        except FileNotFoundError:
            print(f"File at {filepath} not found")
            self.words = []

    def read_words(self, file):
        """Reads words from the file and returns a list of words."""
        words = []
        for line in file:
            word = line.strip()
            words.append(word)
        return words

    def get_random_word(self):
        """Returns a random word from the list of words."""
        if not self.words:
            return None
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments."""
    
    def read_words(self, file):
        """Reads words from the file, excluding blank lines and comments."""
        words = []
        for line in file:
            word = line.strip()
            if word and not word.startswith("#"):
                words.append(word)
        return words

# Example usage
if __name__ == "__main__":
    # Test WordFinder with a simple file
    wf = WordFinder("simple.txt")
    print(wf.get_random_word())

    # Test SpecialWordFinder with a complex file
    swf = SpecialWordFinder("complex.txt")
    print(swf.get_random_word())