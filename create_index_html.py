
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

    nav_items = ""
    for html_file in html_files:
        title = html_file.replace(".html", "").replace("-", " ").title()
        nav_items += f"<a href=\"{html_file}\">{title}</a>\n"

    index_html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia de Técnicas de Prompt</title>
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
        ul {{
            list-style: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 10px;
        }}
        a {{
            color: var(--primary-color);
            text-decoration: none;
            font-size: 1.2em;
            transition: color 0.3s ease-in-out, text-decoration 0.3s ease-in-out;
        }}
        a:hover {{
            text-decoration: underline;
            color: #0056b3;
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
        <h1>Guia de Técnicas de Prompt</h1>
        <p>Este site reúne diversas técnicas de prompt para otimizar suas interações com IAs generativas. Explore as diferentes abordagens para melhorar a qualidade e a relevância das suas respostas.</p>
        <h2>Técnicas Disponíveis:</h2>
        <ul>
{list_items}
        </ul>
    </div>
</body>
</html>
"""

    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html_content)
    print(f"Created {os.path.join(output_dir, 'index.html')}")

if __name__ == "__main__":
    output_html_dir = "/home/ubuntu/my-nextra-site/out"
    
    create_index_html(output_html_dir)


