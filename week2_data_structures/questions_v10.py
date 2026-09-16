# questions_v10.py
# Week 2 Day 4: Identity Engine (Cognitive OS + Emotional OS Fusion)

import json
import os
import datetime

DATA_FOLDER = "../data"
STATE_FILE = "../data/emotional_state.json"
IDENTITY_FILE = "../data/identity_profile.json"

def load_emotional_state():
    """Load persistent emotional state."""
    if not os.path.exists(STATE_FILE):
        return {"state": "Neutral", "strength": 0, "last_update": None}

    with open(STATE_FILE, "r") as f:
        return json.load(f)

def load_identity():
    """Load persistent identity profile."""
    if not os.path.exists(IDENTITY_FILE):
        return {
            "core_archetype": "Undefined",
            "cognitive_history": [],
            "emotional_history": [],
            "identity_shift": "Stable",
            "last_update": None
        }

    with open(IDENTITY_FILE, "r") as f:
        return json.load(f)

def save_identity(identity):
    """Save persistent identity profile."""
    with open(IDENTITY_FILE, "w") as f:
        json.dump(identity, f, indent=4)

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

def determine_cognitive_archetype(axes):
    """Determine cognitive archetype based on axes."""
    logic = axes["logic_emotion"]
    structure = axes["structure_spontaneity"]
    alone = axes["alone_social"]
    evidence = axes["evidence_intuition"]

    if logic > 0 and structure > 0:
        return "Architect"
    if logic > 0 and alone > 0:
        return "Analyst"
    if evidence < 0 and alone < 0:
        return "Empath"
    return "Balanced"

def fuse_identity(cognitive_archetype, emotional_state):
    """Fuse cognitive archetype + emotional state into identity."""
    if emotional_state == "Radiant":
        return f"{cognitive_archetype} (Radiant)"
    if emotional_state == "Shadow":
        return f"{cognitive_archetype} (Shadow)"
    return f"{cognitive_archetype} (Neutral)"

def detect_identity_shift(identity_history):
    """Detect long-term identity evolution."""
    if len(identity_history) < 2:
        return "Stable"

    first = identity_history[0]
    last = identity_history[-1]

    if first != last:
        return "Evolving"
    return "Stable"

def run_identity_engine():
    print("\n--- Identity Engine (Week 2 Day 4) ---\n")

    # Load emotional state
    emotional_state = load_emotional_state()
    print(f"Current Emotional State: {emotional_state['state']}")

    # Cognitive questions
    axes = {
        "logic_emotion": 0,
        "structure_spontaneity": 0,
        "alone_social": 0,
        "evidence_intuition": 0
    }

    print("\nAnswer the cognitive questions:\n")

    axes["logic_emotion"] += 1 if input("Logic or emotion? ").strip().lower() == "logic" else -1
    axes["structure_spontaneity"] += 1 if input("Structure or spontaneity? ").strip().lower() == "structure" else -1
    axes["alone_social"] += 1 if input("Alone or others? ").strip().lower() == "alone" else -1
    axes["evidence_intuition"] += 1 if input("Evidence or intuition? ").strip().lower() == "evidence" else -1

    # Determine cognitive archetype
    cognitive_archetype = determine_cognitive_archetype(axes)

    # Fuse with emotional state
    fused_identity = fuse_identity(cognitive_archetype, emotional_state["state"])

    # Load identity profile
    identity = load_identity()

    # Update identity history
    identity["cognitive_history"].append(cognitive_archetype)
    identity["emotional_history"].append(emotional_state["state"])

    # Detect identity shift
    identity["identity_shift"] = detect_identity_shift(identity["cognitive_history"])

    # Update core archetype
    identity["core_archetype"] = fused_identity
    identity["last_update"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save identity
    save_identity(identity)

    print("\n--- Identity Summary ---")
    print(f"Core Identity: {identity['core_archetype']}")
    print(f"Cognitive History: {identity['cognitive_history']}")
    print(f"Emotional History: {identity['emotional_history']}")
    print(f"Identity Shift: {identity['identity_shift']}")
    print(f"Last Update: {identity['last_update']}")

    print("\nWeek 2 Day 4 complete.\n")

if __name__ == "__main__":
    run_identity_engine()
