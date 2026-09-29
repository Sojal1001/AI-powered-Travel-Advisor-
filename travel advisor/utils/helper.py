import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', text).strip().lower()

def format_results(results):
    formatted = []
    for r in results:
        formatted.append({
            "destination": r.get("destination", "Unknown"),
            "category": r.get("category", "N/A"),
            "description": r.get("description", "No details available"),
            "state": r.get("state", "N/A"),
            "avg_cost": r.get("avg_cost", "Not specified")
        })
    return formatted

def error_message(msg):
    return {"error": True, "message": msg}
