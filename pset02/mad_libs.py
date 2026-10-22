import random

templates = [
    {"text": "The :color :animal :verb over the :adjective :plant.", "author": "Alice"},
    {"text": "A :adjective :person once :verb a :color :animal in :place.", "author": "Bob"},
    {"text": "Every :day, the :adjective :animal would :verb through the :place.", "author": "Carol"},
    {"text": "The :noun and the :noun :verb together under a :adjective :noun.", "author": "David"},
    {"text": "Once upon a time, a :adjective :person :verb into a :place and found a :color :noun.", "author": "Eve"},
    {"text": "The :adjective :person :verb loudly while carrying a :color :noun through :place.", "author": "Frank"},
    {"text": "In :place, a :color :animal learned to :verb and became very :adjective.", "author": "Grace"},
    {"text": "A :adjective :noun is worth two :adjective :noun in :place.", "author": "Hank"},
    {"text": "The :person :verb the :color :noun and then :verb into the :adjective :place.", "author": "Ivy"},
    {"text": "Never :verb a :adjective :animal without first :verb in :place.", "author": "Jack"},
]

yes_answers = {"yes", "y", "sí", "si", "oui", "yep", "yeah", "yup", "sure", "absolutely"}

def get_user_word(prompt):
    while True:
        word = input(f"  Enter {prompt}: ").strip()
        if 1 <= len(word) <= 30:
            return word
        print("  Please enter a word between 1 and 30 characters long.")

def play():
    template = random.choice(templates)
    words = template["text"].split()

    filled = {}
    print("\nFill in the blanks!\n")
    for word in words:
        if word.startswith(":"):
            placeholder = word.rstrip(".,!?;:")
            if placeholder not in filled:
                filled[placeholder] = get_user_word(placeholder[1:])

    result = []
    for word in words:
        if word.startswith(":"):
            placeholder = word.rstrip(".,!?;:")
            punctuation = word[len(placeholder):]
            result.append(filled[placeholder] + punctuation)
        else:
            result.append(word)

    print("\n" + " ".join(result))
    print(f"\nTemplate by: {template['author']}")

def main():
    print("Welcome to Mad Libs!")
    while True:
        play()
        print()
        again = input("Do you want to play again? ").strip().lower()
        if again in yes_answers:
            continue
        else:
            print("Thanks for playing!")
            break

main()