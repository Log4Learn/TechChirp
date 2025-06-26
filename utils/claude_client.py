import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def generate_tweets(prompt: str, max_tokens=300, model="claude-3-haiku-20240307"):
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text.strip()
