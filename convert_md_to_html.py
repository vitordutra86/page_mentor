
import markdown
import os

def convert_md_to_html(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Get list of all markdown files in the root of my-nextra-site
    all_md_files = []
    for filename in os.listdir("/home/ubuntu/my-nextra-site/"):
        if filename.endswith(".md") and filename != "README.md": # Exclude README.md
            all_md_files.append(filename.replace(".md", ".html"))
    all_md_files.sort()

    nav_items = ""
    for html_file in all_md_files:
        title = html_file.replace(".html", "").replace("-", " ").title()
        nav_items += f"<a href=\"{html_file}\">{title}</a>\n"

    # Now process the markdown files from the root of my-nextra-site
    for filename in os.listdir("/home/ubuntu/my-nextra-site/"):
        if filename.endswith(".md") and filename != "README.md":
            input_filepath = os.path.join("/home/ubuntu/my-nextra-site/", filename)
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
            --primary-color: #007bff;
            --secondary-color: #6c757d;
            --text-color: #343a40;
            --heading-color: #212529;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --border-color: #dee2e6;
            --code-bg: #e9ecef;
            --code-text: #bd4147;
        }}
        body {{
            font-family: \'Inter\', \'Helvetica Neue\', Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
        }}
        .container {{
            max-width: 960px;
            width: 100%;
            background-color: var(--card-bg);
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            box-sizing: border-box;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: var(--heading-color);
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            line-height: 1.3;
            font-weight: 700;
        }}
        h1 {{
            font-size: 2.8em;
            border-bottom: 3px solid var(--primary-color);
            padding-bottom: 15px;
            margin-bottom: 1.2em;
            text-align: center;
        }}
        h2 {{
            font-size: 2.2em;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 1em;
        }}
        p {{
            margin-bottom: 1em;
            font-size: 1.1em;
        }}
        pre {{
            background-color: var(--code-bg);
            padding: 18px;
            border-radius: 8px;
            overflow-x: auto;
            font-size: 0.95em;
            line-height: 1.5;
            border: 1px solid var(--border-color);
            color: var(--code-text);
        }}
        code {{
            font-family: \'Fira Code\', \'SFMono-Regular\', Consolas, \'Liberation Mono\', Menlo, Courier, monospace;
            background-color: var(--code-bg);
            padding: 3px 7px;
            border-radius: 5px;
            font-size: 0.9em;
            color: var(--code-text);
        }}
        a {{
            color: var(--primary-color);
            text-decoration: none;
            transition: color 0.3s ease-in-out, text-decoration 0.3s ease-in-out;
        }}
        a:hover {{
            text-decoration: underline;
            color: #0056b3;
        }}
        ul, ol {{
            margin-left: 25px;
            margin-bottom: 1em;
            font-size: 1.1em;
        }}
        li {{
            margin-bottom: 0.6em;
        }}
        /* Navbar styles */
        .navbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: var(--primary-color);
            padding: 10px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .navbar a {{
            color: white;
            padding: 8px 15px;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }}
        .navbar a:hover {{
            background-color: #0056b3;
        }}
        .dropdown {{
            position: relative;
            display: inline-block;
        }}
        .dropdown-content {{
            display: none;
            position: absolute;
            background-color: var(--primary-color);
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
            border-radius: 5px;
        }}
        .dropdown-content a {{
            color: white;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            text-align: left;
        }}
        .dropdown-content a:hover {{background-color: #0056b3;}}
        .dropdown:hover .dropdown-content {{display: block;}}

        /* Responsive adjustments */
        @media (max-width: 768px) {{
            body {{
                padding: 15px;
            }}
            .container {{
                padding: 25px;
            }}
            h1 {{
                font-size: 2em;
            }}
            h2 {{
                font-size: 1.6em;
            }}
            p, ul, ol {{
                font-size: 1em;
            }}
            .navbar {{
                flex-direction: column;
                align-items: flex-start;
            }}
            .navbar a {{
                width: 100%;
                text-align: left;
            }}
            .dropdown {{
                width: 100%;
            }}
            .dropdown-content {{
                width: 100%;
            }}
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="navbar">
            <a href="index.html">Home</a>
            <div class="dropdown">
                <a href="#" class="dropbtn">Técnicas &#9662;</a>
                <div class="dropdown-content">
{nav_items}
                </div>
            </div>
        </div>
        {html_content}
    </div>
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


