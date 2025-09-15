from sentence_transformers import SentenceTransformer
import os

# Define where to save the model locally
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models', 'distiluse-base-multilingual-cased-v1')

# Download the model
print("Downloading the model, please wait...")
model = SentenceTransformer("distiluse-base-multilingual-cased-v1")

# Save it locally
os.makedirs(MODEL_DIR, exist_ok=True)
model.save(MODEL_DIR)

print(f"Model downloaded and saved at {MODEL_DIR}")
