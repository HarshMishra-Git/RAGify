
from sentence_transformers import SentenceTransformer
import numpy as np

# Load the Sentence Transformer model (LLaMA or another available embedding model)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")  # Change model if needed

def get_text_embedding(text):
    """Generate embedding for a given text."""
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding

def generate_embeddings(texts):
    """Generate embeddings for a list of texts."""
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings
