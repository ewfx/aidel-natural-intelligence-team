from fastapi import FastAPI, File, UploadFile
import json
from backend.src.genai_prompt import ask_genai
import os
app = FastAPI()
 
@app.post("/entity/assessment")
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
    assessmentPrompt = f"Use the following assessment rules and come up with riskRating, riskRationale, complianceRating and complianceRationle  for each entity in '{entities}', AssessmentRules:'{assessmentRules}'. Look for internet for more recent data and news. Example check in Google for any negative news or results. Check in OpenCorporate, Wikipedia, Sanctions lists around the world. Keep the original transaction detail fields associated with each entity for verification. In Rationale mention which source of data was the reason like Transaction detail, Google, Wikipedia, Sanctions List, OpenCorporate etc.  Provide output in JSON format. Dont add any other text in output apart from this report."
    # Step 2: Risk Assessement using GenAI
    riskAndComplianceReport = ask_genai(assessmentPrompt, "Risk Assessment")
    print("Final Risk and Compliance Report:")
    print(riskAndComplianceReport)
    print("Analysis is complete. Returning the result.")
    # Clean the string by removing "```json" and "```"
    cleaned_str = riskAndComplianceReport.strip("```json").strip("```").strip()

    # Parse the cleaned JSON string
    parsed_json = json.loads(cleaned_str)
    return parsed_json

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
