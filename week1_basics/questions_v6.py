# questions_v6.py
# Day 7: Multi-axis archetype engine

import datetime
import json
import os

DATA_FOLDER = "../data"

def run_engine():
    session_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_name = input("Before we begin, what is your name? ")
    print(f"\nWelcome, {user_name}! Let's begin.\n")

    print("Welcome to the Archetype Engine Prototype (Day 7)")
    print("Please answer the following questions:\n")

    # Multi-axis question structure
    questions = {
        "decision_style": {
            "prompt": "1. Do you make decisions more from logic or emotion? ",
            "axis": "logic_emotion",
            "weights": {"logic": 1, "emotion": -1}
        },
        "structure_preference": {
            "prompt": "2. Do you prefer structure or spontaneity? ",
            "axis": "structure_spontaneity",
            "weights": {"structure": 1, "spontaneity": -1}
        },
        "recharge_style": {
            "prompt": "3. Do you recharge alone or with others? ",
            "axis": "alone_social",
            "weights": {"alone": 1, "others": -1}
        },
        "trust_basis": {
            "prompt": "4. Do you trust intuition or evidence more? ",
            "axis": "evidence_intuition",
            "weights": {"evidence": 1, "intuition": -1}
        }
    }

    answers = {}
    axes = {
        "logic_emotion": 0,
        "structure_spontaneity": 0,
        "alone_social": 0,
        "evidence_intuition": 0
    }

    # Ask questions + apply axis weights
    for key, data in questions.items():
        user_answer = input(data["prompt"]).strip().lower()
        answers[key] = user_answer

        if user_answer in data["weights"]:
            axes[data["axis"]] += data["weights"][user_answer]

    # Mood question (non-axis)
    mood = input("How are you feeling today? ")
    answers["mood"] = mood

    print(f"\nGot it — you're feeling {mood}.\n")

    # Archetype interpretation
    archetype = interpret_archetype(axes)

    # Build session object
    session_data = {
        "user": user_name,
        "session_time": session_time,
        "answers": answers,
        "axes": axes,
        "archetype": archetype
    }

    save_session(session_data)

    # Summary
    print("\n--- Session Summary ---")
    print(f"User: {user_name}")
    print(f"Session Time: {session_time}\n")

    print("--- Answers ---")
    for key, value in answers.items():
        print(f"{key}: {value}")

    print("\n--- Axis Scores ---")
    for axis, value in axes.items():
        print(f"{axis}: {value}")

    print(f"\nArchetype Interpretation: {archetype}")

    print("\nDay 7 complete.\n")

def interpret_archetype(axes):
    """
    Basic archetype mapping based on multi-axis scores.
    This will evolve into your full Emotional OS.
    """

    logic = axes["logic_emotion"]
    structure = axes["structure_spontaneity"]
    alone = axes["alone_social"]
    evidence = axes["evidence_intuition"]

    # Example archetype logic (simple but expandable)
    if logic > 0 and structure > 0:
        return "The Architect — structured, logical, independent, evidence-driven."
    if logic > 0 and alone > 0:
        return "The Analyst — introspective, logical, prefers solitude."
    if emotion > 0 and spontaneity > 0:
        return "The Explorer — emotional, flexible, socially adaptive."
    if intuition > 0 and social > 0:
        return "The Empath — intuitive, people-oriented, emotionally resonant."

    return "The Balanced — a mix of multiple cognitive patterns."

def save_session(session_data):
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    filename = f"{DATA_FOLDER}/session_{session_data['session_time'].replace(':', '-')}.json"

    with open(filename, "w") as f:
        json.dump(session_data, f, indent=4)

if __name__ == "__main__":
    run_engine()
