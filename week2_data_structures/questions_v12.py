# questions_v12.py
# Week 2 Day 6: Identity Forecasting Engine (Future Identity Timeline)

import json
import os
import datetime

IDENTITY_FILE = "../data/identity_profile.json"
STATE_FILE = "../data/emotional_state.json"
FORECAST_FILE = "../data/identity_forecast.json"

def load_identity():
    if not os.path.exists(IDENTITY_FILE):
        return None
    with open(IDENTITY_FILE, "r") as f:
        return json.load(f)

def load_emotional_state():
    if not os.path.exists(STATE_FILE):
        return None
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def calculate_emotional_trajectory(emotional_history):
    """Predict future emotional direction."""
    if len(emotional_history) < 2:
        return "Insufficient data"

    radiant = emotional_history.count("Radiant")
    shadow = emotional_history.count("Shadow")
    neutral = emotional_history.count("Neutral")

    if radiant > shadow and radiant > neutral:
        return "Trending upward — future emotional state likely Radiant."
    if shadow > radiant and shadow > neutral:
        return "Trending downward — future emotional state likely Shadow."
    return "Stable — future emotional state likely Neutral."

def calculate_cognitive_trajectory(cognitive_history):
    """Predict future cognitive archetype direction."""
    if len(cognitive_history) < 2:
        return "Insufficient data"

    last = cognitive_history[-1]
    freq = cognitive_history.count(last)

    if freq >= len(cognitive_history) // 2:
        return f"Stabilizing — future cognitive archetype likely {last}."
    else:
        return "Drifting — cognitive archetype likely to evolve."

def fuse_future_identity(emotional_prediction, cognitive_prediction):
    """Combine emotional + cognitive predictions into a future identity."""
    if "Radiant" in emotional_prediction and "Stabilizing" in cognitive_prediction:
        return "Radiant Stabilized Identity — clarity, confidence, forward growth."
    if "Shadow" in emotional_prediction and "Stabilizing" in cognitive_prediction:
        return "Shadow Stabilized Identity — introspective, intuitive, depth-focused."
    if "Neutral" in emotional_prediction and "Stabilizing" in cognitive_prediction:
        return "Neutral Stabilized Identity — balanced, adaptive, consistent."
    if "Drifting" in cognitive_prediction:
        return "Evolving Identity — exploring new cognitive and emotional directions."
    return "Uncertain Identity — mixed signals, requires more data."

def build_identity_timeline(identity, emotional_prediction, cognitive_prediction, future_identity):
    """Create a timeline object for long-term identity evolution."""
    return {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "past_core_identity": identity["core_archetype"],
        "past_cognitive_history": identity["cognitive_history"],
        "past_emotional_history": identity["emotional_history"],
        "predicted_emotional_trajectory": emotional_prediction,
        "predicted_cognitive_trajectory": cognitive_prediction,
        "future_identity_projection": future_identity
    }

def save_forecast(forecast):
    with open(FORECAST_FILE, "w") as f:
        json.dump(forecast, f, indent=4)

def run_identity_forecast():
    print("\n--- Identity Forecasting Engine (Week 2 Day 6) ---\n")

    identity = load_identity()
    emotional_state = load_emotional_state()

    if identity is None or emotional_state is None:
        print("Missing identity or emotional state data. Run previous steps first.")
        return

    cognitive_history = identity["cognitive_history"]
    emotional_history = identity["emotional_history"]

    emotional_prediction = calculate_emotional_trajectory(emotional_history)
    cognitive_prediction = calculate_cognitive_trajectory(cognitive_history)
    future_identity = fuse_future_identity(emotional_prediction, cognitive_prediction)

    forecast = build_identity_timeline(identity, emotional_prediction, cognitive_prediction, future_identity)

    save_forecast(forecast)

    print("--- Identity Forecast ---")
    print(f"Predicted Emotional Trajectory: {emotional_prediction}")
    print(f"Predicted Cognitive Trajectory: {cognitive_prediction}")
    print(f"Future Identity Projection: {future_identity}")

    print("\nForecast saved to identity_forecast.json")
    print("\nWeek 2 Day 6 complete.\n")

if __name__ == "__main__":
    run_identity_forecast()
