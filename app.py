
from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
from rapidfuzz import process, fuzz
import json

app = Flask(__name__)

with open(r"D:\Hackathon\HexaLingua\faqs.json", "r", encoding="utf-8") as f:
    faqs = json.load(f)


greetings = [
    "hello", "hi","hii", "hey", "good morning", "good afternoon", "good evening",
    "how are you", "nice to meet you", "greetings", "how's it going",
    "hiya", "yo", "what's up", "howdy", "hello friend", "hey buddy",
    "long time no see", "good day", "pleasure to meet you"
]

def translate_to_english(text):
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated
    except Exception as e:
        print("Translation error:", e)
        return text 


def get_answer(user_query):
    translated = translate_to_english(user_query.strip().lower())
    
    keywords = translated.split()
    candidate_questions = [faq for faq in faqs if any(k in faq["question"].lower() for k in keywords)]
    
    if candidate_questions:
        all_questions = [q["question"] for q in candidate_questions]
        match, score, idx = process.extractOne(translated, all_questions, scorer=fuzz.token_set_ratio)
        if score >= 60:
            return candidate_questions[idx]["answer"]
    
    all_questions = [q["question"] for q in faqs]
    match, score, idx = process.extractOne(translated, all_questions, scorer=fuzz.token_set_ratio)
    if score >= 60:
        return faqs[idx]["answer"]
    
    return "Sorry, I don't know the answer yet."


@app.route('/')
def home():
    return render_template('chatbot.html')


@app.route('/get-answer', methods=['POST'])
def query():
    data = request.get_json()
    user_query = data.get('query', '').strip()

    if not user_query:
        return jsonify({'answer': "I didn't receive a query."})

    greet_text="hello"
    for greet in greetings:
        if greet in user_query.lower():
            greet_text = greet.capitalize()
            return jsonify({'answer': f"{greet_text}! How can I help you today?"})
        else:
            return jsonify({'answer':"hello! How can I help you today?"})


    bot_response = get_answer(user_query)
    return jsonify({'answer': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
