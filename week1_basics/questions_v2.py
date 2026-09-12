# questions_v2.py
# Day 3: Dictionary-based question engine

import datetime

def run_engine():
    # Timestamp for the session
    session_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_name = input("Before we begin, what is your name? ")
    print(f"\nWelcome, {user_name}! Let's begin.\n")

    print("Welcome to the 111 Prototype Engine (Day 3)")
    print("Please answer the following questions:\n")

    # Store answers in a dictionary
    answers = {}

    answers["decision_style"] = input("1. Do you make decisions more from logic or emotion? ")
    answers["structure_preference"] = input("2. Do you prefer structure or spontaneity? ")
    answers["recharge_style"] = input("3. Do you recharge alone or with others? ")
    answers["trust_basis"] = input("4. Do you trust intuition or evidence more? ")

    mood = input("How are you feeling today? ")
    answers["mood"] = mood

    print(f"\nGot it — you're feeling {mood}.\n")

    # Summary
    print("\n--- Session Summary ---")
    print(f"User: {user_name}")
    print(f"Session Time: {session_time}\n")

    print("--- Answers ---")
    for key, value in answers.items():
        print(f"{key}: {value}")

    print("\nAnswers stored successfully in dictionary format.")
    print("Day 3 complete.\n")

if __name__ == "__main__":
    run_engine()
