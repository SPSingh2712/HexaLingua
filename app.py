from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load FAQs
with open("faqs.json", "r") as f:
    faqs = json.load(f)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_question = data.get("question", "").lower()

    # Simple keyword-based matching
    for faq in faqs:
        if faq["question"].lower() in user_question:
            return jsonify({"answer": faq["answer"]})

    return jsonify({"answer": "Sorry, I don't know the answer yet. But I'm learning!"})

if __name__ == "__main__":
    app.run(debug=True)
