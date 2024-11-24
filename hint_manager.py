from random import sample

class HintManager:
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.used_hints = set()

    def provide_hint(self):
        """Provides a hint based on the chosen word."""
        hints = []
        if "first_letter" not in self.used_hints:
            hints.append(f"The first letter is '{self.chosen_word[0].upper()}'.")
            self.used_hints.add("first_letter")
        if "random_letter" not in self.used_hints:
            random_letter = sample(self.chosen_word, 1)[0]
            hints.append(f"The word contains the letter '{random_letter.upper()}'.")
            self.used_hints.add("random_letter")

        if hints:
            return hints[0]
        return "No more 'жардам' available."
