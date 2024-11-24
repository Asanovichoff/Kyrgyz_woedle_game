from random import choice, sample

# Language word lists
try:
    from words import kyrgyz_five_letter_words, kyrgyz_four_letter_words
except ImportError:
    print("Error: 'words.py' or the required word lists are missing.")
    exit(1)

# Constants
MAX_ATTEMPTS = 6

# Returns a random word based on the selected language and difficulty
def choose_word():
    languages = {"1": (kyrgyz_five_letter_words, 5),
                 "2": (kyrgyz_four_letter_words, 4)}
    print("Welcome to Kyrgyz Wordle!\n")
    print("Please select a difficulty:")
    print("1 - '5-letter words'\n2 - '4-letter words'")
    option = input("\nYour option: ").strip()

    while option not in languages:
        print("\nInvalid input, try again.")
        option = input("Your option: ").strip()

    word_list, word_length = languages[option]
    return choice(word_list), word_length

CHAR_MAPPING = {
    'y': 'ү', 'ү': 'y',
    'и': 'й', 'й': 'и',  
    'o': 'ө', 'ө': 'o',   
    'н': 'ң', 'ң': 'н' 
}

def normalize_word(word):
    return ''.join(CHAR_MAPPING.get(char, char) for char in word)

# Returns feedback on letter placements using Unicode symbols
def letter_placement(user_word, chosen_word):
    user_word = normalize_word(user_word)  # Normalize user input
    chosen_word = normalize_word(chosen_word)
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
            continue  # Skip already matched letters
        elif letter in chosen_word_list:
            feedback[index] = "🟨"
            chosen_word_list[chosen_word_list.index(letter)] = None  

    return " ".join(feedback)


# Provides a hint based on the chosen word
def provide_hint(chosen_word, used_hints):
    hints = []
    if "first_letter" not in used_hints:
        hints.append(f"The first letter is '{chosen_word[0].upper()}'.")
        used_hints.add("first_letter")
    if "random_letter" not in used_hints:
        random_letter = sample(chosen_word, 1)[0]
        hints.append(f"The word contains the letter '{random_letter.upper()}'.")
        used_hints.add("random_letter")

    if hints:
        return hints[0]  # Provide one hint at a time
    return "No more 'жардам' available."


# Main Game Logic
def wordle_game():
    chosen_word, word_length = choose_word()
    attempts = 0
    used_hints = set()  

    print(f"\nThe game has started! Guess the {word_length}-letter Kyrgyz word.")
    print(f"You have {MAX_ATTEMPTS} attempts. Type your guess, 'жардам' for a hint, or 'таппадым' to quit.\n")

    while attempts < MAX_ATTEMPTS:
        user_word = input("> ").strip().lower()

        if user_word == "таппадым":
            print(f"You gave up after {attempts} attempts. The correct word was {chosen_word.upper()}.")
            break

        if user_word == "жардам":
            print(provide_hint(chosen_word, used_hints))
            continue  
        
        if len(user_word) != word_length:
            print(f"Invalid word. Make sure it is a valid {word_length}-letter word.")
            continue

        attempts += 1
        print(f"[ {' '.join(user_word.upper())} ]")
        print(letter_placement(user_word, chosen_word))

        if user_word == chosen_word:
            print(f"\n🎉 Congratulations!\n🎉 🎉 🎉 🎉 \nYOU WON!\n 🎉 🎉 🎉 🎉\n \
                The correct word was {chosen_word.upper()}.\nTotal attempts: {attempts}")
            break
        else:
            remaining_attempts = MAX_ATTEMPTS - attempts
            print(f"Incorrect guess. You have {remaining_attempts} attempt{'s' if remaining_attempts > 1 else ''} left.")

    if attempts == MAX_ATTEMPTS:
        print(f"\n😔 😔 😔 GAME OVER 😔 😔 😔\n You've used all your attempts. The correct word was {chosen_word.upper()}.")


if __name__ == "__main__":
    wordle_game()
