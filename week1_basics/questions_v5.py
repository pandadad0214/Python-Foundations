# questions_v5.py
# Day 6: Multi-session analysis + engine memory loading

import json
import os
import datetime

DATA_FOLDER = "../data"

def load_all_sessions():
    """Load all JSON session files from the data folder."""
    sessions = []

    if not os.path.exists(DATA_FOLDER):
        return sessions

    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".json"):
            filepath = os.path.join(DATA_FOLDER, filename)
            with open(filepath, "r") as f:
                sessions.append(json.load(f))

    return sessions

def analyze_sessions(sessions):
    """Analyze patterns across multiple sessions."""
    if not sessions:
        return "No past sessions found."

    total_score = 0
    moods = []
    logic_count = 0
    emotion_count = 0

    for s in sessions:
        total_score += s["score"]
        moods.append(s["answers"].get("mood", "unknown"))

        # Track decision style trends
        decision = s["answers"].get("decision_style", "")
        if "logic" in decision:
            logic_count += 1
        if "emotion" in decision:
            emotion_count += 1

    avg_score = total_score / len(sessions)

    # Drift detection
    drift = detect_drift(sessions)

    return {
        "total_sessions": len(sessions),
        "average_score": avg_score,
        "mood_history": moods,
        "logic_vs_emotion": {
            "logic": logic_count,
            "emotion": emotion_count
        },
        "drift": drift
    }

def detect_drift(sessions):
    """Detect changes in patterns over time."""
    if len(sessions) < 2:
        return "Not enough data for drift detection."

    first = sessions[0]["score"]
    last = sessions[-1]["score"]

    if last > first:
        return "Your patterns are shifting toward structure, logic, and independence."
    elif last < first:
        return "Your patterns are shifting toward intuition, emotion, and flexibility."
    else:
        return "Your cognitive pattern is stable over time."

def run_engine_memory():
    """Main function to load and analyze engine memory."""
    print("\n--- Engine Memory Analysis (Day 6) ---\n")

    sessions = load_all_sessions()
    results = analyze_sessions(sessions)

    if isinstance(results, str):
        print(results)
        return

    print(f"Total Sessions: {results['total_sessions']}")
    print(f"Average Score: {results['average_score']:.2f}")
    print(f"Mood History: {results['mood_history']}")
    print(f"Logic vs Emotion: {results['logic_vs_emotion']}")
    print(f"Pattern Drift: {results['drift']}")

    print("\nDay 6 complete.\n")

if __name__ == "__main__":
    run_engine_memory()
