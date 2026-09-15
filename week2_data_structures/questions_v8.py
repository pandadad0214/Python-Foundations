# questions_v8.py
# Week 2 Day 2: Emotional Memory + Resonance History + Tilt Evolution

import json
import os

DATA_FOLDER = "../data"

def load_sessions():
    """Load all JSON session files."""
    sessions = []
    if not os.path.exists(DATA_FOLDER):
        return sessions

    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".json"):
            filepath = os.path.join(DATA_FOLDER, filename)
            with open(filepath, "r") as f:
                sessions.append(json.load(f))

    return sorted(sessions, key=lambda x: x["session_time"])

def analyze_emotional_history(sessions):
    """Analyze emotional resonance across all sessions."""
    if not sessions:
        return "No emotional data available."

    emotional_scores = []
    moods = []
    tilts = []

    for s in sessions:
        emotional_scores.append(s.get("emotional_score", 0))
        moods.append(s["answers"].get("mood", "unknown"))
        tilts.append(s.get("tilt", "Neutral Tilt"))

    avg_emotion = sum(emotional_scores) / len(emotional_scores)

    drift = detect_emotional_drift(emotional_scores)
    tilt_trend = detect_tilt_trend(tilts)

    return {
        "total_sessions": len(sessions),
        "mood_history": moods,
        "emotional_scores": emotional_scores,
        "average_emotional_score": avg_emotion,
        "emotional_drift": drift,
        "tilt_trend": tilt_trend
    }

def detect_emotional_drift(scores):
    """Detect long-term emotional drift."""
    if len(scores) < 2:
        return "Not enough emotional data for drift detection."

    first = scores[0]
    last = scores[-1]

    if last > first:
        return "Your emotional resonance is trending upward (more positive, more radiant)."
    elif last < first:
        return "Your emotional resonance is trending downward (more shadow, more reactive)."
    else:
        return "Your emotional resonance is stable over time."

def detect_tilt_trend(tilts):
    """Detect how tilt states evolve over time."""
    if len(tilts) < 2:
        return "Not enough tilt data for trend detection."

    golden = tilts.count("Golden Tilt — clarity, structure, forward momentum.")
    shadow = tilts.count("Shadow Tilt — intuition, emotion, reactive drift.")
    neutral = tilts.count("Neutral Tilt — balanced, adaptive, stable.")

    if golden > shadow and golden > neutral:
        return "You trend toward Golden Tilt (clarity, structure, momentum)."
    elif shadow > golden and shadow > neutral:
        return "You trend toward Shadow Tilt (intuition, emotion, drift)."
    else:
        return "You trend toward Neutral Tilt (balanced, adaptive)."

def run_emotional_memory():
    print("\n--- Emotional OS Memory Analysis (Week 2 Day 2) ---\n")

    sessions = load_sessions()
    results = analyze_emotional_history(sessions)

    if isinstance(results, str):
        print(results)
        return

    print(f"Total Sessions: {results['total_sessions']}")
    print(f"Mood History: {results['mood_history']}")
    print(f"Emotional Scores: {results['emotional_scores']}")
    print(f"Average Emotional Score: {results['average_emotional_score']:.2f}")
    print(f"Emotional Drift: {results['emotional_drift']}")
    print(f"Tilt Trend: {results['tilt_trend']}")

    print("\nWeek 2 Day 2 complete.\n")

if __name__ == "__main__":
    run_emotional_memory()
