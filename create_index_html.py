
import os

def create_index_html(output_dir, meta_file):
    html_files = []
    for filename in os.listdir(output_dir):
        if filename.endswith(".html") and filename != "index.html":
            html_files.append(filename)
    
    html_files.sort()

    list_items = ""
    for html_file in html_files:
        title = html_file.replace(".html", "").replace("-", " ").title()
        list_items += f"<li><a href=\"{html_file}\">{title}</a></li>\n"

    index_html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia de Técnicas de Prompt</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Fira Sans\", \"Droid Sans\", \"Helvetica Neue\", sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            color: #222;
            text-align: center;
        }}
        ul {{
            list-style: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 10px;
        }}
        a {{
            color: #0070f3;
            text-decoration: none;
            font-size: 1.2em;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>Guia de Técnicas de Prompt</h1>
    <p>Este site reúne diversas técnicas de prompt para otimizar suas interações com IAs generativas. Explore as diferentes abordagens para melhorar a qualidade e a relevância das suas respostas.</p>
    <h2>Técnicas Disponíveis:</h2>
    <ul>
{list_items}
    </ul>
</body>
</html>
"""

    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html_content)
    print(f"Created {os.path.join(output_dir, 'index.html')}")

if __name__ == "__main__":
    output_html_dir = "/home/ubuntu/my-nextra-site/out"
    meta_json_file = "_meta.en.json"
    
    create_index_html(output_html_dir, meta_json_file)


