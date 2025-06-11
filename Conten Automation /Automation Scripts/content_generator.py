import json
from gpt_models.openai_integration import generate_content
from utils import load_template, replace_variables

def generate_from_template(template_type, variables):
    """Generate content using a predefined template."""
    template = load_template(template_type)  # Loads JSON/CSV
    prompt = template["prompt"] if "prompt" in template else template
    filled_prompt = replace_variables(prompt, variables)
    return generate_content(filled_prompt)

# Example: Generate a welcome email
email_vars = {"company_name": "DataMart", "user_name": "Jane Doe"}
print(generate_from_template("welcome_email", email_vars))
