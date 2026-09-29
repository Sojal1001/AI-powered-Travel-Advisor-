import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
data = pd.read_csv('models/destinations.csv')
data.columns = data.columns.str.strip()

# Check required columns
required_cols = ['destination', 'description', 'category']
for col in required_cols:
    if col not in data.columns:
        raise ValueError(f"Missing column: {col}")

# Combine text fields for TF-IDF
data['combined'] = (
    data['description'].fillna('') + " " +
    data['category'].fillna('') + " " +
    data['state'].fillna('')
).str.lower()

# Train TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(data['combined'])

# Save vectorizer & data
with open('models/tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf, f)

with open('models/destination_data.pkl', 'wb') as f:
    pickle.dump(data, f)

print("Model training complete — vectorizer and data saved successfully!")
