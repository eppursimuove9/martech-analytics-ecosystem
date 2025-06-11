import json
import csv

def load_template(template_name):
    """Load a template from JSON or CSV."""
    if template_name.endswith(".json"):
        with open(f"content_templates/{template_name}") as f:
            return json.load(f)
    elif template_name.endswith(".csv"):
        with open(f"content_templates/{template_name}") as f:
            return list(csv.DictReader(f))[0]  # First row as template

def replace_variables(text, variables):
    """Replace {{placeholders}} with actual values."""
    for key, value in variables.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text
