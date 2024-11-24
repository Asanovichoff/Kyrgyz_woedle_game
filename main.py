from words import kyrgyz_five_letter_words, kyrgyz_four_letter_words
from wordle_game import WordleGame

def main():
    word_lists = {
        "1": (kyrgyz_five_letter_words, 5),
        "2": (kyrgyz_four_letter_words, 4)
    }
    game = WordleGame(word_lists)
    game.play()

if __name__ == "__main__":
    main()
