import spacy
import openai
from transformers import pipeline
from huggingface_hub import login     

def extract_with_openrouter_models(text):
    print(f"Extracting the entities from '{text}'")
    system_content = "You are an AI that identify people and companies."
    prompt = f"Identify people and company in '{text}'. Return a JSON with objects identifiedRisks, entityBasicRiskRating, entityName and entityType. entityType can be People or Company. IdentifiedRisks field should have risks identified with people or company based on transaction input given. entityBasicRisk rating will be very low, low, medium, high, very high based on notes and other details in transaction."
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
    model="deepseek/deepseek-r1-zero:free",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )
    return completion.choices[0].message.content;


# Main function to process text data
def analyze_entities(text):
    return extract_with_openrouter_models(text)
    
    
def preprocess_text(text):
    return " ".join(text.split()) 