# questions_v13.py
# Week 2 Day 7: Identity Map (Graph Structure for Visualization)

import json
import os
import datetime

IDENTITY_FILE = "../data/identity_profile.json"
FORECAST_FILE = "../data/identity_forecast.json"
MAP_FILE = "../data/identity_map.json"

def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def build_identity_nodes(identity, forecast):
    """Create graph nodes for identity evolution."""
    nodes = []

    # Past identity nodes
    for i, (cog, emo) in enumerate(zip(identity["cognitive_history"], identity["emotional_history"])):
        nodes.append({
            "id": f"past_{i}",
            "type": "past_state",
            "cognitive": cog,
            "emotional": emo,
            "timestamp": identity["last_update"] if i == len(identity["cognitive_history"]) - 1 else "historical"
        })

    # Current identity node
    nodes.append({
        "id": "current_identity",
        "type": "current_state",
        "core_identity": identity["core_archetype"],
        "identity_shift": identity["identity_shift"],
        "timestamp": identity["last_update"]
    })

    # Future identity node
    nodes.append({
        "id": "future_identity",
        "type": "predicted_state",
        "future_projection": forecast["future_identity_projection"],
        "predicted_emotional_trajectory": forecast["predicted_emotional_trajectory"],
        "predicted_cognitive_trajectory": forecast["predicted_cognitive_trajectory"],
        "timestamp": forecast["timestamp"]
    })

    return nodes

def build_identity_edges(identity):
    """Create edges showing identity evolution over time."""
    edges = []

    # Past → Past transitions
    for i in range(len(identity["cognitive_history"]) - 1):
        edges.append({
            "from": f"past_{i}",
            "to": f"past_{i+1}",
            "type": "historical_transition"
        })

    # Last past → current
    if len(identity["cognitive_history"]) > 0:
        edges.append({
            "from": f"past_{len(identity['cognitive_history']) - 1}",
            "to": "current_identity",
            "type": "current_transition"
        })

    # Current → future
    edges.append({
        "from": "current_identity",
        "to": "future_identity",
        "type": "forecast_transition"
    })

    return edges

def build_identity_map():
    identity = load_json(IDENTITY_FILE)
    forecast = load_json(FORECAST_FILE)

    if identity is None or forecast is None:
        print("Missing identity or forecast data. Run previous steps first.")
        return

    nodes = build_identity_nodes(identity, forecast)
    edges = build_identity_edges(identity)

    identity_map = {
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nodes": nodes,
        "edges": edges
    }

    with open(MAP_FILE, "w") as f:
        json.dump(identity_map, f, indent=4)

    print("\n--- Identity Map Generated ---")
    print(f"Nodes: {len(nodes)}")
    print(f"Edges: {len(edges)}")
    print(f"Saved to identity_map.json")

    print("\nWeek 2 complete.\n")

if __name__ == "__main__":
    build_identity_map()
