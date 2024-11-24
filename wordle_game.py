from word_manager import WordManager
from hint_manager import HintManager

class WordleGame:
    MAX_ATTEMPTS = 6

    def __init__(self, word_lists):
        self.word_manager = WordManager()
        self.hint_manager = None
        self.word_lists = word_lists
        self.attempts = 0

    def select_difficulty(self):
        """Asks the user to select a difficulty level."""
        print("Welcome to Kyrgyz Wordle!\n")
        print("Please select a difficulty:")
        print("1 - '5-letter words'\n2 - '4-letter words'")
        option = input("\nYour option: ").strip()

        while option not in {"1", "2"}:
            print("\nInvalid input, try again.")
            option = input("Your option: ").strip()

        self.word_manager.choose_word(option, self.word_lists)
        self.hint_manager = HintManager(self.word_manager.chosen_word)

    def play(self):
        """Main game loop."""
        self.select_difficulty()
        word_length = self.word_manager.word_length
        print(f"\nThe game has started! Guess the {word_length}-letter Kyrgyz word.")
        print(f"You have {self.MAX_ATTEMPTS} attempts. Type your guess, 'жардам' for a hint, or 'таппадым' to quit.\n")

        while self.attempts < self.MAX_ATTEMPTS:
            user_word = input("> ").strip().lower()

            if user_word == "таппадым":
                print(f"You gave up after {self.attempts} attempts. The correct word was {self.word_manager.chosen_word.upper()}.")
                break

            if user_word == "жардам":
                print(self.hint_manager.provide_hint())
                continue

            if len(user_word) != word_length:
                print(f"Invalid word. Make sure it is a valid {word_length}-letter word.")
                continue

            self.attempts += 1
            print(f"[ {' '.join(user_word.upper())} ]")
            print(self.word_manager.letter_placement(user_word))

            if user_word == self.word_manager.chosen_word:
                print(f"\n🎉 Congratulations!\n🎉 🎉 🎉 🎉 \nYOU WON!\n 🎉 🎉 🎉 🎉\n \
                    The correct word was {self.word_manager.chosen_word.upper()}.\nTotal attempts: {self.attempts}")
                break
            else:
                remaining_attempts = self.MAX_ATTEMPTS - self.attempts
                print(f"Incorrect guess. You have {remaining_attempts} attempt{'s' if remaining_attempts > 1 else ''} left.")

        if self.attempts == self.MAX_ATTEMPTS:
            print(f"\n😔 😔 😔 GAME OVER 😔 😔 😔\n You've used all your attempts. The correct word was {self.word_manager.chosen_word.upper()}.")
