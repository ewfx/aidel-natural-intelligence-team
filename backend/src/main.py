from fastapi import FastAPI, File, UploadFile
import requests
import openai
import json
from backend.src.entity_analysis import analyze_entities

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    # Step 1: Extract entities using spaCy
    entities = analyze_entities(text)
    print("Entities identified:")
    print(entities)
    # Step 2: Perform risk assessment (flag risky entities for deeper analysis)
    risk_results = analyze_risk(entities)

    return {"entities": risk_results}


def analyze_risk(entities):
    """Performs risk assessment using online checks & OpenAI (if needed)."""
    results = {}

    for category, items in entities.items():
        results[category] = []
        
        for item in items:
            # Step 3: Query online sources for risk evaluation
            risk_score, rationale = check_online_risks(item)

            # Step 4: If high risk, ask OpenAI for further analysis
            if risk_score >= 70:
                risk_score, rationale = analyze_with_openai(item)

            results[category].append({
                "name": item,
                "risk_score": risk_score,
                "rationale": rationale
            })

    return results

def check_online_risks(entity_name):
    """Queries Wikipedia & Sanctions List APIs to check risk level."""
    try:
        # Example: Check if entity appears on Wikipedia (Basic Risk Indicator)
        wikipedia_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={entity_name}&format=json"
        response = requests.get(wikipedia_url)
        data = response.json()

        if data["query"]["search"]:
            return 50, f"{entity_name} found on Wikipedia. Requires further analysis."
    except:
        pass  # Ignore errors in API calls

    # Example: Placeholder for Sanctions List API (Manually add real API later)
    sanction_list = ["John Doe", "XYZ Corporation"]  # Example flagged entities
    if entity_name in sanction_list:
        return 90, f"{entity_name} found in sanctions list."

    return 20, "No suspicious activity detected."

def analyze_with_openai(entity_name):
    print(f"Analyzing the entity '{entity_name}'")
    system_content = "You are an AI that assesses financial risk."
    prompt = f"Analyze financial risks and compliance concerns related to '{entity_name}'. Return a JSON with risk_score (0-100) and rationale."
    client = openai.OpenAI(
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="mistralai/mistral-small-3.1-24b-instruct:free",
    messages=[
        {
        "role": system_content,
        "content": [
            {
            "type": "text",
            "text": prompt
            }
        ]
        }
    ]
    )
    print(completion.choices[0])
    try:
        result = json.loads(completion.choices[0].message.content)
        return result.get("risk_score", 50), result.get("rationale", "No rationale provided.")
    except:
        return 50, "Failed to fetch AI-based risk analysis."

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
