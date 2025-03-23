import spacy
import openai
from transformers import pipeline
from huggingface_hub import login     

# Load spaCy model for fast entity extraction
nlp = spacy.load("en_core_web_sm")
login("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")
# Load Hugging Face NER Model
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

llama_pipeline = pipeline("text-generation", model="meta-llama/Llama-3.2-1B") 

# Function to extract entities using spaCy
def extract_entities_spacy(text):
    doc = nlp(text)
    entities = {"people": set(), "companies": set()}
    
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["people"].add(ent.text)
        elif ent.label_ == "ORG":
            entities["companies"].add(ent.text)
    
    return entities

# Function to extract entities using Hugging Face NER
def extract_entities_huggingface(text):
    ner_results = ner_pipeline(text)
    entities = {"people": set(), "companies": set()}

    for entity in ner_results:
        entity_text = entity["word"]
        entity_label = entity["entity"]

        if "PER" in entity_label:  # Person
            entities["people"].add(entity_text)
        elif "ORG" in entity_label:  # Organization
            entities["companies"].add(entity_text)

    return entities

def extract_with_mistralai(text):
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
    print(completion.choices[0].message.content)

# Function to extract entities using Meta AI API
def extract_entities_metaai(text):
    try:
        prompt = f"Extract people and companies from this text:\n\n{text}\n\nFormat the output as JSON with keys 'people' and 'companies'."
        result = llama_pipeline(prompt, max_length=10000, do_sample=True)
        response_data = result[0]['generated_text']
        people, companies = set(), set()
        for line in response_data.get("choices", [{}])[0].get("text", "").split("\n"):
            if "Person:" in line:
                people.add(line.split(":")[1].strip())
            elif "Company:" in line:
                companies.add(line.split(":")[1].strip())

        return {"people": people, "companies": companies}
    except Exception as e:
        print(f"Error in Meta AI API: {e}")
        return {"people": set(), "companies": set()}

# Main function to process text data
def analyze_entities(text):
    cleaned_text = preprocess_text(text)
    spacy_entities = extract_entities_spacy(cleaned_text)
    hf_entities = extract_entities_huggingface(cleaned_text)
    extract_with_mistralai(text)
    # Merge results from all models
    people = spacy_entities["people"] | hf_entities["people"] 
    companies = spacy_entities["companies"] | hf_entities["companies"] 

    return {
        "people": list(people),
        "companies": list(companies)
    }
    
def preprocess_text(text):
    return " ".join(text.split()) 