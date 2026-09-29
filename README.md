# 🌍 AI-Powered Travel Advisor

An intelligent, mood-based travel recommendation system built using **Python, Flask, and Machine Learning**. The application recommends Indian travel destinations based on users' moods, interests, and preferences.

## 📌 Project Overview

AI-Powered Travel Advisor is a web-based application designed to simplify travel planning through personalized destination recommendations. It uses Natural Language Processing (NLP) and TF-IDF vectorization to analyze user preferences and identify suitable destinations from a curated dataset of Indian tourist locations.

## ✨ Key Features

- **Mood-Based Recommendations:** Discover destinations based on moods such as relaxed, happy, romantic, spiritual, adventurous, excited, and stressed.
- **AI-Powered Suggestions:** Uses TF-IDF vectorization and similarity-based matching to recommend relevant destinations.
- **Indian Destination Dataset:** Includes a curated collection of 70 Indian travel destinations.
- **Personalized Travel Planning:** Matches destination descriptions with user preferences and interests.
- **Interactive Web Interface:** A responsive frontend for exploring travel recommendations.
- **Destination Information:** Displays relevant destination details to help users plan their trips.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | Flask |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF Vectorizer |
| Data Processing | Pandas, NumPy |
| Frontend | HTML, CSS, JavaScript |
| Dataset | CSV |
| Model Serialization | Pickle |

## ⚙️ How It Works

1. **User Input:** The user selects their current mood or enters travel preferences.
2. **Data Preprocessing:** Destination information is cleaned and prepared for NLP.
3. **Feature Extraction:** TF-IDF converts destination descriptions and user preferences into numerical feature vectors.
4. **Similarity Matching:** The recommendation engine identifies destinations that best match the user's preferences.
5. **Recommendations:** The Flask application displays relevant destinations and their details.

## 📂 Project Structure

A suggested repository structure:

```text
AI-Travel-Advisor/
├── app.py
├── destinations.csv
├── destination_data.pkl
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt
└── README.md
```

Adjust the structure to match the actual repository.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Travel-Advisor.git
cd AI-Travel-Advisor
```

Replace YOUR_USERNAME with your GitHub username and update the repository name if necessary.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Or on macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

Alternatively, if a requirements.txt file is included:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open the local address displayed by Flask in your browser, typically:

```text
http://127.0.0.1:5000/
```

Ensure that the destination dataset and any required serialized model files are available before starting the application.

## 🧠 Recommendation System

The recommendation engine uses TF-IDF (Term Frequency–Inverse Document Frequency) to represent destination descriptions as numerical vectors. User preferences are processed using the same vectorizer, allowing similarity-based matching between user input and available destinations.

The system incorporates mood-based filtering or mapping to personalize its recommendations.

## 📊 Dataset

The project uses a curated dataset containing 70 Indian travel destinations. Destination information is stored in `destinations.csv` and processed by the recommendation engine.

## 🔮 Future Enhancements

- Integrate live weather forecasts.
- Add budget-based travel recommendations.
- Include hotel and transportation suggestions.
- Introduce interactive maps and itinerary generation.
- Improve personalization using user feedback.
- Expand the destination dataset to include international locations.

## 📜 License

Add a license file if you intend to distribute the project under an open-source license.
