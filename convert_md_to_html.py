
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

            # Add basic HTML structure and styling
            final_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename.replace(".md", "").replace("-", " ").title()}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 


            \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Fira Sans\", \"Droid Sans\", \"Helvetica Neue\", sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #222;
            margin-top: 1em;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        code {{
            font-family: \"SFMono-Regular\", Consolas, \"Liberation Mono\", Menlo, Courier, monospace;
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }}
        a {{
            color: #0070f3;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
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


