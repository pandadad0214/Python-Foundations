# questions_v1.py
# Day 2: First interactive question script

def main():
    user_name = input("Before we begin, what is your name? ")
    print(f"\nWelcome, {user_name}! Let's begin.\n")

    print("Welcome to the 111 Prototype Engine (Day 2)")
    print("Please answer the following questions:\n")

    q1 = input("1. Do you make decisions more from logic or emotion? ")
    q2 = input("2. Do you prefer structure or spontaneity? ")
    q3 = input("3. Do you recharge alone or with others? ")
    q4 = input("4. Do you trust intuition or evidence more? ")

    mood = input("How are you feeling today? ")
    print(f"Got it — you're feeling {mood}.\n")

    print("\n--- Your Answers ---")
    print(f"1: {q1}")
    print(f"2: {q2}")
    print(f"3: {q3}")
    print(f"4: {q4}")

    print("\nThank you for completing Day 2!")

    print("\n--- Summary ---")
    print(f"User: {user_name}")
    print(f"Mood: {mood}")
    print("Answers recorded successfully.")

if __name__ == "__main__":
    main()
