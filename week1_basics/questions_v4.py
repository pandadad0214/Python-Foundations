# questions_v4.py
# Day 5: JSON export + session logging

import datetime
import json
import os

def run_engine():
    session_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_name = input("Before we begin, what is your name? ")
    print(f"\nWelcome, {user_name}! Let's begin.\n")

    print("Welcome to the Persistent Pattern Engine Prototype (Day 5)")
    print("Please answer the following questions:\n")

    # Weighted question structure
    questions = {
        "decision_style": {
            "prompt": "1. Do you make decisions more from logic or emotion? ",
            "weights": {"logic": 2, "emotion": 1}
        },
        "structure_preference": {
            "prompt": "2. Do you prefer structure or spontaneity? ",
            "weights": {"structure": 2, "spontaneity": 1}
        },
        "recharge_style": {
            "prompt": "3. Do you recharge alone or with others? ",
            "weights": {"alone": 2, "others": 1}
        },
        "trust_basis": {
            "prompt": "4. Do you trust intuition or evidence more? ",
            "weights": {"intuition": 1, "evidence": 2}
        }
    }

    answers = {}
    score = 0

    # Ask questions + apply weights
    for key, data in questions.items():
        user_answer = input(data["prompt"]).strip().lower()
        answers[key] = user_answer

        if user_answer in data["weights"]:
            score += data["weights"][user_answer]
        else:
            score += 1  # neutral fallback

    # Mood question (non-weighted)
    mood = input("How are you feeling today? ")
    answers["mood"] = mood

    print(f"\nGot it — you're feeling {mood}.\n")

    # Pattern interpretation
    pattern = interpret_pattern(score)

    # Build session object
    session_data = {
        "user": user_name,
        "session_time": session_time,
        "answers": answers,
        "score": score,
        "pattern": pattern
    }

    # Save to JSON
    save_session(session_data)

    # Summary
    print("\n--- Session Summary ---")
    print(f"User: {user_name}")
    print(f"Session Time: {session_time}\n")

    print("--- Answers ---")
    for key, value in answers.items():
        print(f"{key}: {value}")

    print(f"\nWeighted Score: {score}")
    print(f"Pattern Interpretation: {pattern}")

    print("\nSession saved to JSON.")
    print("Day 5 complete.\n")

def interpret_pattern(score):
    if score >= 7:
        return "You lean toward structure, logic, independence, and evidence-based thinking."
    elif score >= 5:
        return "You show a balanced pattern between logic and emotion, structure and spontaneity."
    else:
        return "You lean toward intuition, emotion, social recharge, and flexible thinking."

def save_session(session_data):
    # Ensure data folder exists
    if not os.path.exists("../data"):
        os.makedirs("../data")

    # Build filename
    filename = f"../data/session_{session_data['session_time'].replace(':', '-')}.json"

    # Save JSON
    with open(filename, "w") as f:
        json.dump(session_data, f, indent=4)

if __name__ == "__main__":
    run_engine()
