
import markdown
import os

def convert_md_to_html(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_filepath = os.path.join(input_dir, filename)
            output_filename = filename.replace(".md", ".html")
            output_filepath = os.path.join(output_dir, output_filename)

            with open(input_filepath, "r", encoding="utf-8") as f:
                md_content = f.read()
            
            html_content = markdown.markdown(md_content)

            # Add enhanced HTML structure and styling
            final_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename.replace(".md", "").replace("-", " ").title()}</title>
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
        h1, h2, h3, h4, h5, h6 {{
            color: var(--text-color);
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            line-height: 1.3;
        }}
        h1 {{
            font-size: 2.5em;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 1em;
        }}
        h2 {{
            font-size: 1.8em;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 5px;
            margin-bottom: 1em;
        }}
        p {{
            margin-bottom: 1em;
        }}
        pre {{
            background-color: var(--code-bg);
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 0.9em;
            line-height: 1.5;
            border: 1px solid var(--border-color);
        }}
        code {{
            font-family: \"SFMono-Regular\", Consolas, \"Liberation Mono\", Menlo, Courier, monospace;
            background-color: var(--code-bg);
            padding: 2px 5px;
            border-radius: 4px;
            font-size: 0.9em;
        }}
        a {{
            color: var(--link-color);
            text-decoration: none;
            transition: color 0.2s ease-in-out;
        }}
        a:hover {{
            text-decoration: underline;
            color: #2980b9;
        }}
        ul, ol {{
            margin-left: 20px;
            margin-bottom: 1em;
        }}
        li {{
            margin-bottom: 0.5em;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

            with open(output_filepath, "w", encoding="utf-8") as f:
                f.write(final_html)
            print(f"Converted {input_filepath} to {output_filepath}")

if __name__ == "__main__":
    input_pages_dir = "/home/ubuntu/my-nextra-site/pages"
    output_html_dir = "/home/ubuntu/my-nextra-site/out"
    
    convert_md_to_html(input_pages_dir, output_html_dir)


