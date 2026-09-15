# questions_v9.py
# Week 2 Day 3: Emotional State Machine + Decay + Recovery

import json
import os
import datetime

DATA_FOLDER = "../data"
STATE_FILE = "../data/emotional_state.json"

def load_state():
    """Load persistent emotional state."""
    if not os.path.exists(STATE_FILE):
        return {"state": "Neutral", "strength": 0, "last_update": None}

    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    """Save persistent emotional state."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def apply_decay(strength):
    """Emotional decay: state weakens over time."""
    if strength > 0:
        return strength - 1
    if strength < 0:
        return strength + 1
    return strength

def update_state(current_state, emotional_score):
    """
    Emotional physics:
    - emotional_score > 0 pushes toward Radiant
    - emotional_score < 0 pushes toward Shadow
    - emotional_score = 0 pushes toward Neutral
    """

    strength = current_state["strength"]
    state = current_state["state"]

    # Apply decay first
    strength = apply_decay(strength)

    # Apply new emotional input
    strength += emotional_score

    # Determine new state
    if strength >= 3:
        state = "Radiant"
    elif strength <= -3:
        state = "Shadow"
    else:
        state = "Neutral"

    return {"state": state, "strength": strength, "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

def mood_weight(mood):
    """Convert mood into emotional resonance score."""
    mapping = {
        "happy": 2,
        "excited": 2,
        "calm": 1,
        "tired": -1,
        "stressed": -2,
        "anxious": -2
    }
    return mapping.get(mood, 0)

def run_engine():
    print("\n--- Emotional State Machine (Week 2 Day 3) ---\n")

    # Load persistent state
    current_state = load_state()

    print(f"Previous Emotional State: {current_state['state']} (strength {current_state['strength']})")

    mood = input("How are you feeling today? ").strip().lower()
    emotional_score = mood_weight(mood)

    # Update emotional state
    new_state = update_state(current_state, emotional_score)

    # Save updated state
    save_state(new_state)

    print("\n--- Updated Emotional State ---")
    print(f"New State: {new_state['state']}")
    print(f"State Strength: {new_state['strength']}")
    print(f"Last Update: {new_state['last_update']}")

    print("\nWeek 2 Day 3 complete.\n")

if __name__ == "__main__":
    run_engine()
