from fastapi import FastAPI, File, UploadFile
from backend.src.genai_prompt import ask_genai
import os
app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):

    print("Starting the analysis...")
    content = await file.read()
    transactionDetails = content.decode("utf-8")

    # Prompt for extracting entities
    prompt = f"Identify people and company in '{transactionDetails}'. Return a JSON with objects identifiedRisks, entityBasicRiskRating, entityName and entityType. entityType can be People or Company. IdentifiedRisks field should have risks identified with people or company based on transaction input given. entityBasicRisk rating will be very low, low, medium, high, very high based on notes and other details in transaction. Keep the original transaction detail fields associated with each entity for verification."
    # Step 1: Extract entities using GenAI
    entities = ask_genai(prompt, "Entity Extraction")
    print("Entities identified:")
    print(entities)
    
    # Get current script directory
    BASE_DIR = os.path.dirname(__file__)

    # Use relative path based on script's location
    assessement_file_path = os.path.join(BASE_DIR, "assessment_rules.txt")
    with open(assessement_file_path, "r", encoding="utf-8") as file:
        assessmentRules = file.read()
    # Prompt for coming up with risk assessment
    assessmentPrompt = f"Use the following assessment rules and come up with riskRating, riskRationale, complianceRating and complianceRationle  for each entity in '{entities}', AssessmentRules:'{assessmentRules}'. Look for internet for more recent data and news. Keep the original transaction detail fields associated with each entity for verification. Provide output in JSON format."
    # Step 2: Risk Assessement using GenAI
    riskAndComplainceReport = ask_genai(assessmentPrompt, "Risk Assessment")
    print("Final Risk and Compliance Report:")
    print(riskAndComplainceReport)
    print("Analysis is complete.")
    
    return riskAndComplainceReport

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
