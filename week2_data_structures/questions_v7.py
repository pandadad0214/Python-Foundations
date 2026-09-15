# questions_v7.py
# Week 2 Day 1: Emotional OS Layer + Tilt System

import datetime
import json
import os

DATA_FOLDER = "../data"

def run_engine():
    session_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_name = input("Before we begin, what is your name? ")
    print(f"\nWelcome, {user_name}! Let's begin.\n")

    print("Welcome to the Emotional OS Prototype (Week 2 Day 1)")
    print("Please answer the following questions:\n")

    # Multi-axis cognitive structure
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

    # Ask questions + apply cognitive weights
    for key, data in questions.items():
        user_answer = input(data["prompt"]).strip().lower()
        answers[key] = user_answer

        if user_answer in data["weights"]:
            axes[data["axis"]] += data["weights"][user_answer]

    # Mood question (emotional axis)
    mood = input("How are you feeling today? (happy, stressed, calm, anxious, excited, tired) ").strip().lower()
    answers["mood"] = mood

    # Emotional resonance score
    emotional_score = mood_weight(mood)

    # Tilt system (cognitive + emotional fusion)
    tilt = calculate_tilt(axes, emotional_score)

    # Archetype fusion
    archetype = interpret_archetype(axes, emotional_score)

    # Build session object
    session_data = {
        "user": user_name,
        "session_time": session_time,
        "answers": answers,
        "axes": axes,
        "emotional_score": emotional_score,
        "tilt": tilt,
        "archetype": archetype
    }

    save_session(session_data)

    # Summary
    print("\n--- Session Summary ---")
    print(f"User: {user_name}")
    print(f"Session Time: {session_time}\n")

    print("--- Cognitive Axes ---")
    for axis, value in axes.items():
        print(f"{axis}: {value}")

    print(f"\nMood: {mood}")
    print(f"Emotional Score: {emotional_score}")
    print(f"Tilt State: {tilt}")
    print(f"Archetype Fusion: {archetype}")

    print("\nWeek 2 Day 1 complete.\n")

def mood_weight(mood):
    """Convert mood into an emotional resonance score."""
    mapping = {
        "happy": 2,
        "excited": 2,
        "calm": 1,
        "tired": -1,
        "stressed": -2,
        "anxious": -2
    }
    return mapping.get(mood, 0)

def calculate_tilt(axes, emotional_score):
    """Combine cognitive axes + emotional score into a tilt state."""
    total = sum(axes.values()) + emotional_score

    if total >= 3:
        return "Golden Tilt — clarity, structure, forward momentum."
    elif total <= -3:
        return "Shadow Tilt — intuition, emotion, reactive drift."
    else:
        return "Neutral Tilt — balanced, adaptive, stable."

def interpret_archetype(axes, emotional_score):
    """Fuse cognitive archetype + emotional resonance."""
    logic = axes["logic_emotion"]
    structure = axes["structure_spontaneity"]
    alone = axes["alone_social"]
    evidence = axes["evidence_intuition"]

    # Cognitive base archetype
    if logic > 0 and structure > 0:
        base = "Architect"
    elif logic > 0 and alone > 0:
        base = "Analyst"
    elif emotional_score < 0 and alone < 0:
        base = "Empath"
    else:
        base = "Balanced"

    # Emotional fusion
    if emotional_score >= 2:
        return f"{base} + Radiant Resonance"
    elif emotional_score <= -2:
        return f"{base} + Shadow Resonance"
    else:
        return f"{base} + Neutral Resonance"

def save_session(session_data):
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    filename = f"{DATA_FOLDER}/session_{session_data['session_time'].replace(':', '-')}.json"

    with open(filename, "w") as f:
        json.dump(session_data, f, indent=4)

if __name__ == "__main__":
    run_engine()
