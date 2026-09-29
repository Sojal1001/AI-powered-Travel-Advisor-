import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

with open('models/tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)
with open('models/destination_data.pkl', 'rb') as f:
    data = pickle.load(f)

def get_recommendations(mood, budget=None, days=None):
    mood = mood.lower().strip()
    
    mood_map = {
        "relaxed": ["beach", "nature", "serene", "peaceful", "calm"],
        "happy": ["beach", "nightlife", "adventure", "vibrant", "festival"],
        "romantic": ["heritage", "lake", "hill station", "sunset", "quiet"],
        "spiritual": ["temple", "spiritual", "ghat", "pilgrimage", "monastery"],
        "adventurous": ["trek", "mountain", "skiing", "hiking", "rafting"],
        "excited": ["nightlife", "adventure", "shopping", "festival"],
        "stressed": ["beach", "nature", "yoga", "calm", "spiritual"],
        "curious": ["heritage", "culture", "museum", "architecture"],
        "bored": ["adventure", "nightlife", "beach"],
        "lonely": ["spiritual", "nature", "hill station"]
    }

    related_terms = mood_map.get(mood, [mood])
    all_results = []

    for term in related_terms:
        query_vec = tfidf.transform([term])
        dest_vecs = tfidf.transform(data['combined'])
        similarity = cosine_similarity(query_vec, dest_vecs).flatten()

        top_idx = similarity.argsort()[-5:][::-1]
        for i in top_idx:
            d = data.iloc[i]
            img_query = d["destination"].replace(" ", "+")
            img_url = f"https://source.unsplash.com/600x400/?{img_query},travel"

            all_results.append({
                "destination": d["destination"],
                "category": d["category"],
                "description": d["description"],
                "state": d["state"],
                "avg_cost": int(d["avg_cost"]),
                "image_url": img_url
            })

    seen = set()
    final_results = []
    for r in all_results:
        if r["destination"] not in seen:
            seen.add(r["destination"])
            final_results.append(r)

    return final_results[:5] if final_results else [{"destination": "No matching destinations found."}]
