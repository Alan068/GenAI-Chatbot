import yaml

def load_prompts(file_path="app/templates/prompts.yaml"):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)
