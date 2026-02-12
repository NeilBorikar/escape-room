from flask import Flask, request, jsonify
from flask_cors import CORS

from game_state import game_state
from qa_data import QA_PAIRS
from matcher import semantic_similarity
from hints import HINTS

app = Flask(__name__)
CORS(app)

# -------------------------
# 🤖 AI CHATBOT
# -------------------------
@app.route("/ask", methods=["POST"])
def ask_ai():
    game_state.reset_if_needed()

    if game_state.time_left() <= 0:
        return jsonify({
            "reply": "⏳ Time is up.",
            "time_left": 0,
            "time_up": True
        })

    data = request.json
    question = data.get("question", "").lower()

    best_score = 0
    best_answer = None

    for pair in QA_PAIRS:
        score = semantic_similarity(question, pair["question"])
        if score > best_score:
            best_score = score
            best_answer = pair["answer"]

    if best_score > 0.45:
        return jsonify({
            "reply": best_answer,
            "time_left": game_state.time_left(),
            "time_up": False
        })

    return jsonify({
        "reply": "That question does not belong here.",
        "time_left": game_state.time_left(),
        "time_up": False
    })


# -------------------------
# 💡 HINT SYSTEM
# -------------------------
@app.route("/hint/<int:stage>", methods=["POST"])
def get_hint(stage):
    used = game_state.hints_used.get(stage, 0)
    hints = HINTS.get(stage, [])

    if used >= len(hints):
        return jsonify({
            "reply": "No more hints available.",
            "time_left": game_state.time_left()
        })

    hint = hints[used]
    game_state.hints_used[stage] = used + 1

    # ➖ Deduct 10 seconds
    game_state.deduct_time(10)

    return jsonify({
        "reply": hint,
        "time_left": game_state.time_left()
    })


# -------------------------
# ⏳ TIMER
# -------------------------
@app.route("/time", methods=["GET"])
def get_time():
    game_state.reset_if_needed()
    return jsonify({
        "time_left": game_state.time_left()
    })


@app.route("/")
def home():
    return "AI_ER backend is running 🚀"

@app.route("/reset", methods=["POST"])
def reset_game():
    game_state.reset()
    game_state.start_game()
    return jsonify({"message": "Game restarted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

