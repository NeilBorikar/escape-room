from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(a, b):
    va = model.encode(a, convert_to_tensor=True)
    vb = model.encode(b, convert_to_tensor=True)
    return util.cos_sim(va, vb).item()

