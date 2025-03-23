import openai

def ask_genai(prompt):
    print(f"Asking GenAI '{prompt}'")
    client = openai.OpenAI(
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "Rajesh Hegde", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "hackathon.ai", # Optional. Site title for rankings on openrouter.ai.
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
