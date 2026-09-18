# questions_v11.py
# Week 2 Day 5: Identity Resonance + Drift + Stability Engine

import json
import os
import datetime

IDENTITY_FILE = "../data/identity_profile.json"

def load_identity():
    """Load persistent identity profile."""
    if not os.path.exists(IDENTITY_FILE):
        return None

    with open(IDENTITY_FILE, "r") as f:
        return json.load(f)

def calculate_resonance(cognitive_history, emotional_history):
    """
    Identity resonance = how often cognitive and emotional states align.
    Radiant + Architect = high resonance
    Shadow + Empath = high resonance
    Neutral + Balanced = medium resonance
    Mismatches = low resonance
    """

    score = 0

    for cog, emo in zip(cognitive_history, emotional_history):
        if "Architect" in cog and emo == "Radiant":
            score += 2
        elif "Analyst" in cog and emo == "Neutral":
            score += 1
        elif "Empath" in cog and emo == "Shadow":
            score += 2
        elif emo == "Neutral":
            score += 1
        else:
            score -= 1

    return score

def calculate_identity_stability(cognitive_history):
    """
    Identity stability = how often the same archetype appears.
    More repetition = more stability.
    More variation = more drift.
    """

    if not cognitive_history:
        return 0

    stability = 0
    last = cognitive_history[0]

    for archetype in cognitive_history[1:]:
        if archetype == last:
            stability += 1
        else:
            stability -= 1
        last = archetype

    return stability

def predict_identity_direction(stability, resonance):
    """
    Predict future identity direction:
    - High stability + high resonance → identity crystallization
    - Low stability + high resonance → emotional-driven evolution
    - High stability + low resonance → cognitive-driven correction
    - Low stability + low resonance → identity fragmentation
    """

    if stability >= 2 and resonance >= 2:
        return "Crystallizing — your identity is becoming more defined."
    if stability < 0 and resonance >= 2:
        return "Emotionally evolving — your identity is shifting through emotional resonance."
    if stability >= 2 and resonance < 0:
        return "Cognitively correcting — your identity is stabilizing despite emotional turbulence."
    return "Fragmenting — your identity is exploring multiple directions."

def run_identity_resonance():
    print("\n--- Identity Resonance Engine (Week 2 Day 5) ---\n")

    identity = load_identity()

    if identity is None:
        print("No identity profile found. Run questions_v10.py first.")
        return

    cognitive_history = identity.get("cognitive_history", [])
    emotional_history = identity.get("emotional_history", [])

    resonance = calculate_resonance(cognitive_history, emotional_history)
    stability = calculate_identity_stability(cognitive_history)
    direction = predict_identity_direction(stability, resonance)

    print(f"Cognitive History: {cognitive_history}")
    print(f"Emotional History: {emotional_history}\n")

    print(f"Identity Resonance Score: {resonance}")
    print(f"Identity Stability Score: {stability}")
    print(f"Predicted Identity Direction: {direction}")

    print("\nWeek 2 Day 5 complete.\n")

if __name__ == "__main__":
    run_identity_resonance()
