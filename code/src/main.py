from fastapi import FastAPI, File, UploadFile
from genai_prompt import ask_genai
import os
import json
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

@app.post("/entity/assessment")
async def upload_file(file: UploadFile = File(...)):
    print("Starting the analysis...")
    content = await file.read()
    transactionDetails = content.decode("utf-8")

    # Prompt for extracting entities
    prompt = f"Identify people and company in '{transactionDetails}'. Return a JSON with objects identifiedRisks, entityBasicRiskRating, entityName and entityType. entityType can be Entity classification in to catagories like Person, Corporation, Non-profit, Shell company, Government agency etc. . IdentifiedRisks field should have risks identified with people or company based on transaction input given. entityBasicRisk rating will be very low, low, medium, high, very high based on notes and other details in transaction. Keep the original transaction detail fields associated with each entity for verification."
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
    assessmentPrompt = f"Use the following assessment rules and come up with report for each entity in '{entities}', AssessmentRules:'{assessmentRules}'. Original transaction details can be found here: '{transactionDetails}' Look for internet for more recent data and news. Example check in Google for any negative news or results. Use anomaly detection in these transactions to find fraudulent or shell companies. Check in OpenCorporate, Wikipedia, Sanctions lists around the world. Keep the original transaction detail fields associated with each entity for verification. In Rationale mention which source of data was the reason like Transaction detail, Google, Wikipedia, Sanctions List, OpenCorporate etc. Provide output in JSON format. JSON should contain following fields: Transaction ID - Transaction id provided, Extracted Entity - [Comma separated list of entities in same transaction], Entity Type: [Entity classification in to catagories like corporation, non-profit, shell company, government agency etc. same order as entities in extracted entities], Risk Score: 0 - 1, Supporting Evidence: [List of sources like websites, transaction details etc so that analyst can refer them], Confidence Score: 0 - 1, Reason: Reasons for the current risks rating and classifications. Each transaction will have one entry in report. Dont add any other text in output apart from this report. ```json and ``` should be used to format the output."
    # Step 2: Risk Assessement using GenAI
    riskAndComplianceReport = ask_genai(assessmentPrompt, "Risk Assessment")
    print("Final Risk and Compliance Report:")
    print(riskAndComplianceReport)
    print("Analysis is complete. Returning the result.")
    # Clean the string by removing "```json" and "```" if present
    if riskAndComplianceReport.startswith("```json") and riskAndComplianceReport.endswith("```"):
        cleaned_str = riskAndComplianceReport.removeprefix("```json").removesuffix("```").strip()
    elif riskAndComplianceReport.startswith("```") and riskAndComplianceReport.endswith("```"):
        cleaned_str = riskAndComplianceReport.removeprefix("```").removesuffix("```").strip()
    else:
        cleaned_str = riskAndComplianceReport.strip()
    # Parse the cleaned JSON string
    parsed_json = json.loads(cleaned_str)
    return parsed_json

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
