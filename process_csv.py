
import pandas as pd
import os
import json

def process_csv_to_md(csv_file, output_dir, meta_file):
    df = pd.read_csv(csv_file)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    new_meta_content = {}

    for index, row in df.iterrows():
        tecnica = row["Técnicas"]
        descricao = row["Descrição"]
        templates = row["Templates"]

        # Sanitize technique name for filename and URL
        filename = tecnica.lower().replace(" ", "-").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ç", "c").replace("ã", "a").replace("õ", "o").replace("â", "a").replace("ê", "e").replace("ô", "o")
        filepath = os.path.join(output_dir, f"{filename}.md") # Changed to .md

        # Create Markdown content
        md_content = f"""
# {tecnica}

## Descrição

{descricao}

## Templates (Prompts)

```
{templates}
```
"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Created {filepath}")
        
        new_meta_content[filename] = tecnica

    # Update _meta.en.json
    meta_filepath = os.path.join(output_dir, meta_file)
    with open(meta_filepath, "r", encoding="utf-8") as f:
        current_meta = json.load(f)
    
    current_meta.update(new_meta_content)

    with open(meta_filepath, "w", encoding="utf-8") as f:
        json.dump(current_meta, f, ensure_ascii=False, indent=2)
    print(f"Updated {meta_filepath}")

if __name__ == "__main__":
    csv_path = "/home/ubuntu/upload/Banco_tecnicas_prompt-Página1.csv"
    output_pages_dir = "/home/ubuntu/my-nextra-site/pages"
    meta_json_file = "_meta.en.json"
    
    process_csv_to_md(csv_path, output_pages_dir, meta_json_file)


