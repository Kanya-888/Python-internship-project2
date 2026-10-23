
import random
import string
from collections import Counter


def play_guessing_game():
    """Play a number guessing game with attempts and scoring."""
    best_score = 0

    print("\n=== NUMBER GUESSING GAME ===")
    print("Guess a number between 1 and 100.")
    print("You have 7 attempts.")
    print("Scoring: Start at 100 points; lose 10 points per wrong guess.")
    print("A correct guess earns at least 10 points.")

    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        score = 0
        won = False

        while attempts < 7:
            guess_text = input(
                f"\nAttempt {attempts + 1}/7 - Enter your guess: "
            ).strip()

            # Validate that the guess is a whole number
            try:
                guess = int(guess_text)
            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue

            if not 1 <= guess <= 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess == secret_number:
                score = max(10, 100 - (attempts - 1) * 10)
                print(f"Correct! The secret number was {secret_number}.")
                print(f"You guessed it in {attempts} attempt(s).")
                print(f"Your score: {score}")
                won = True

                if score > best_score:
                    best_score = score
                    print("New best score!")

                break

            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

            print(f"Attempts remaining: {7 - attempts}")

        if not won:
            print(f"\nGame over! The number was {secret_number}.")
            print("Your score: 0")

        print(f"Best score: {best_score}")

        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay not in ("y", "yes"):
            break


def count_words(path="sample.txt"):
    """Read a text file and return word frequencies."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read().lower()

    except FileNotFoundError:
        print(f"File not found: {path}")
        print("Create sample.txt in the same folder as this program.")
        return None

    except (OSError, UnicodeError) as error:
        print(f"Could not read the file: {error}")
        return None

    # Remove punctuation and split the text into words
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    return Counter(words)


def word_counter():
    """Ask for a text file and display its word statistics."""
    print("\n=== WORD COUNTER ===")
    path = input(
        "Enter text file name (press Enter for sample.txt): "
    ).strip()

    if not path:
        path = "sample.txt"

    counts = count_words(path)

    if counts is None:
        return

    total_words = sum(counts.values())
    unique_words = len(counts)

    print("\n=== WORD COUNT RESULTS ===")
    print(f"File: {path}")
    print(f"Total words : {total_words}")
    print(f"Unique words: {unique_words}")

    if total_words == 0:
        print("The file is empty or contains no words.")
        return

    print("\nTop 10 most common words")
    print("-" * 30)
    print(f"{'Word':<20}{'Count':>10}")
    print("-" * 30)

    for word, count in counts.most_common(10):
        print(f"{word:<20}{count:>10}")

    print("-" * 30)
    print("Note: Common words such as 'the' and 'and' may appear most often.")


def main():
    """Display the main menu."""
    while True:
        print("\n" + "=" * 38)
        print(" NUMBER GUESSING GAME & WORD COUNTER")
        print("=" * 38)
        print("1. Play the Number Guessing Game")
        print("2. Count Words in a Text File")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            play_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
