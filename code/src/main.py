from fastapi import FastAPI, File, UploadFile
import spacy
import json

app = FastAPI()

# Load NLP model for entity extraction (spaCy example)
nlp = spacy.load("en_core_web_sm")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    
    # Extract entities from text
    entities = extract_entities(text)
    
    # Perform risk assessment (placeholder)
    risk_results = analyze_risk(entities)
    
    return {"entities": risk_results}

def extract_entities(text: str):
    doc = nlp(text)
    entities = {"people": [], "companies": []}
    
    for ent in doc.ents:
        if ent.label_ in ["PERSON"]:
            entities["people"].append(ent.text)
        elif ent.label_ in ["ORG"]:
            entities["companies"].append(ent.text)
    
    return entities

def analyze_risk(entities):
    # Placeholder for risk analysis logic
    results = {}
    for category, items in entities.items():
        results[category] = [{"name": item, "risk_score": 50, "rationale": "Example rationale."} for item in items]
    
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# requirements.txt
requirements = """
fastapi
uvicorn
spacy
en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0.tar.gz
"""

with open("requirements.txt", "w") as f:
    f.write(requirements)
