import openai
import json

# Load API key from config (store securely in environment variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content(prompt, model="gpt-4", max_tokens=500):
    " Generate text using OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages [{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating content: {e}")
        return None

# Example usage:
# print(generate_content("Write a 100-word blog intro about AI in marketing."))
