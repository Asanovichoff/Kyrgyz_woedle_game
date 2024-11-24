from random import choice

class WordManager:
    CHAR_MAPPING = {
        'y': 'ү', 'ү': 'y',
        'и': 'й', 'й': 'и',
        'o': 'ө', 'ө': 'o',
        'н': 'ң', 'ң': 'н'
    }

    def __init__(self):
        self.chosen_word = ""
        self.word_length = 0

    def normalize_word(self, word):
        """Replaces characters in the word based on CHAR_MAPPING."""
        return ''.join(self.CHAR_MAPPING.get(char, char) for char in word)

    def choose_word(self, difficulty, word_lists):
        """Randomly selects a word based on the chosen difficulty."""
        word_list, word_length = word_lists[difficulty]
        self.chosen_word = choice(word_list)
        self.word_length = word_length

    def letter_placement(self, user_word):
        """Returns feedback on letter placements using Unicode symbols."""
        user_word = self.normalize_word(user_word)
        chosen_word = self.normalize_word(self.chosen_word)
        feedback = ["⬜"] * len(user_word)
        chosen_word_list = list(chosen_word)

        # First pass: Mark correct placements (🟩)
        for index, letter in enumerate(user_word):
            if letter == chosen_word[index]:
                feedback[index] = "🟩"
                chosen_word_list[index] = None

        # Second pass: Mark wrong placements (🟨)
        for index, letter in enumerate(user_word):
            if feedback[index] == "🟩":
                continue
            elif letter in chosen_word_list:
                feedback[index] = "🟨"
                chosen_word_list[chosen_word_list.index(letter)] = None

        return " ".join(feedback)
