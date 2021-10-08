from typing import List


def get_all_index(text: str, word: str) -> List[int]:
    # return [i for i, letter in enumerate(word) if letter == text]
    found_index = []
    for i in range(len(word)):
        if word[i] == text:
            found_index.append(i)
    return found_index

# 1. l -> xxllx
# 2. e -> xellx


def get_new_masked_word(masked_word: str, word: str, indexes: List[int]) -> str:
    new_masked_word = list(masked_word)

    for step in range(len(word)):
        if step in indexes:
            new_masked_word[step] = word[step]

    return "".join(new_masked_word)


def lost() -> None:
    print("Sorry , U have lost")
    exit(1)


def win() -> None:
    print("Congratulation, U have won")
    exit(0)


def new_guess(guess: str, word: str, masked_word: str) -> str:
    index_list = get_all_index(guess, word)
    return get_new_masked_word(masked_word, word, index_list)


def handle_final_guess(text: str, word: str) -> None:
    if text == word:
        win()
    else:
        lost()


if __name__ == "__main__":
    word = "hello"
    MAX_GUESS = 3
    print(f"Hangman application. Try to guess my word. You have {MAX_GUESS}")

    masked_word = len(word) * "x"

    for step in range(MAX_GUESS):
        print(f"{step + 1}. step, pls give me a letter")
        text = input()

        is_new_guess = len(text) == 1
        if is_new_guess:
            new_guess(text, word, masked_word)
            if masked_word == word:
                win()
        else:
            handle_final_guess(text, word)
    lost()
