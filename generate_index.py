import os

BASE_DIR = "uploads"
OUTPUT_FILE = "index.html"

def generate():
    html = ['<html><head><meta charset="UTF-8"><title>EGC 2025</title></head><body>']
    html.append('<h1>EGC 2025</h1>')
    for root, dirs, files in os.walk(BASE_DIR):
        rel_root = os.path.relpath(root, BASE_DIR)
        display_root = rel_root if rel_root != '.' else BASE_DIR

        html.append(f"<h2>{display_root}</h2>")
        section_items = []

        for file in sorted(files):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path)

            if file.endswith(".html"):
                section_items.append(f'<li><a href="{rel_path}">📝 {file}</a></li>')
            elif file.endswith(".pdf"):
                section_items.append(f'<li><a href="{rel_path}" target="_blank">📄 {file}</a></li>')
            elif file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
                html.append(f'<p><img src="{rel_path}" alt="{file}" style="max-width:200px;"></p>')

        if section_items:
            html.append("<ul>")
            html.extend(section_items)
            html.append("</ul>")

    html.append("</body></html>")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

if __name__ == "__main__":
    generate()
