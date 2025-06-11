import openai

# Upload training data (JSONL format) for fine-tuning
training_file = openai.File.create(
    file=open("prompts/training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# Create a fine-tuned model
response = openai.FineTuningJob.create(
    training_file=training_file.id,
    model="gpt-3.5-turbo"
)

print(f"Fine-tuning job ID: {response.id}")
