
import os

def create_index_html(output_dir):
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
        :root {{
            --text-color: #2c3e50;
            --bg-color: #ffffff;
            --link-color: #3498db;
            --code-bg: #ecf0f1;
            --border-color: #e0e0e0;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Fira Sans\", \"Droid Sans\", \"Helvetica Neue\", sans-serif;
            line-height: 1.8;
            color: var(--text-color);
            background-color: var(--bg-color);
            max-width: 900px;
            margin: 40px auto;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            box-sizing: border-box;
        }}
        h1 {{
            color: var(--text-color);
            text-align: center;
            font-size: 2.5em;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 1em;
        }}
        h2 {{
            color: var(--text-color);
            font-size: 1.8em;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 5px;
            margin-bottom: 1em;
        }}
        p {{
            margin-bottom: 1em;
        }}
        ul {{
            list-style: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 10px;
        }}
        a {{
            color: var(--link-color);
            text-decoration: none;
            font-size: 1.2em;
            transition: color 0.2s ease-in-out;
        }}
        a:hover {{
            text-decoration: underline;
            color: #2980b9;
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
    
    create_index_html(output_html_dir)


