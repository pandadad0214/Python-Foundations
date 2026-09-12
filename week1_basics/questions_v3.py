# questions_v3.py
# Day 4: Weighted reactive-pattern engine prototype

import datetime

def run_engine():
    session_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_name = input("Before we begin, what is your name? ")
    print(f"\nWelcome, {user_name}! Let's begin.\n")

    print("Welcome to the Weighted Pattern Engine Prototype (Day 4)")
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

        # Apply weight if answer matches known pattern
        if user_answer in data["weights"]:
            score += data["weights"][user_answer]
        else:
            # Neutral fallback if answer is unexpected
            score += 1

    # Mood question (non-weighted)
    mood = input("How are you feeling today? ")
    answers["mood"] = mood

    print(f"\nGot it — you're feeling {mood}.\n")

    # Pattern interpretation
    pattern = interpret_pattern(score)

    # Summary
    print("\n--- Session Summary ---")
    print(f"User: {user_name}")
    print(f"Session Time: {session_time}\n")

    print("--- Answers ---")
    for key, value in answers.items():
        print(f"{key}: {value}")

    print(f"\nWeighted Score: {score}")
    print(f"Pattern Interpretation: {pattern}")

    print("\nDay 4 complete.\n")

def interpret_pattern(score):
    """
    Basic pattern interpretation.
    This will evolve into your full reactive-pattern engine.
    """

    if score >= 7:
        return "You lean toward structure, logic, independence, and evidence-based thinking."
    elif score >= 5:
        return "You show a balanced pattern between logic and emotion, structure and spontaneity."
    else:
        return "You lean toward intuition, emotion, social recharge, and flexible thinking."

if __name__ == "__main__":
    run_engine()
