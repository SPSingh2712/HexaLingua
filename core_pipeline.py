import json
import os
import re
import torch
from sentence_transformers import SentenceTransformer, util

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
FAQ_FILE = os.path.join(DATA_DIR, 'faqs.json')
LOG_FILE = os.path.join(DATA_DIR, 'query_logs.json')

# Threshold for similarity
SIMILARITY_THRESHOLD = 0.5

# Load FAQ data
with open(FAQ_FILE, "r", encoding="utf-8") as f:
    faq_data = json.load(f)

def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

questions = [preprocess(item["question"]) for item in faq_data]
answers = [item["answer"] for item in faq_data]

# Load model
model = SentenceTransformer("models/distiluse-base-multilingual-cased-v1")  # This will download once


# Always compute embeddings fresh on every run
question_embeddings = model.encode(questions, convert_to_tensor=True)

def log_query(user_query, best_score):
    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                json.dump([], f)
        
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            logs = json.load(f)
        
        logs.append({"query": user_query, "score": best_score})
        
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print("Error logging query:", e)

def get_answer(user_query: str) -> str:
    query_embedding = model.encode(preprocess(user_query), convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(query_embedding, question_embeddings)
    best_match_idx = int(torch.argmax(similarities))
    best_score = float(similarities[0][best_match_idx])

    if best_score < SIMILARITY_THRESHOLD:
        log_query(user_query, best_score)
        return "Sorry, I don't understand the question. Please try again or contact support."

    return answers[best_match_idx]
