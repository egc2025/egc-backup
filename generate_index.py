import os

BASE_DIR = "uploads"
TEMPLATE_FILE = "base_index.html"
OUTPUT_FILE = "index.html"

def generate_content():
    sections = []

    for root, dirs, files in os.walk(BASE_DIR):
        rel_root = os.path.relpath(root, BASE_DIR)
        display_root = rel_root if rel_root != "." else BASE_DIR

        html = [f"<h4>{display_root}</h4>", "<ul>"]

        for file in sorted(files):
            rel_path = os.path.join("uploads", rel_root, file).replace("\\", "/")

            if file.endswith(".html"):
                html.append(f'<li><a href="{rel_path}">📝 {file}</a></li>')
            elif file.endswith(".pdf"):
                html.append(f'<li><a href="{rel_path}" target="_blank">📄 {file}</a></li>')

        html.append("</ul>")

        for file in sorted(files):
            rel_path = os.path.join("uploads", rel_root, file).replace("\\", "/")
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
                html.append(f'<img src="{rel_path}" alt="{file}" class="img-fluid mb-3" style="max-width:200px;">')

        sections.append("\n".join(html))

    return "\n<hr>\n".join(sections)

def generate_page():
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Błąd: Nie znaleziono pliku szablonu '{TEMPLATE_FILE}'")
        return

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    content = generate_content()
    final_html = template.replace("{{ content }}", content)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Wygenerowano {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_page()
