import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def convert_recursive_txt_to_pdf(root_folder):
    if not os.path.exists(root_folder):
        print(f"Error: Folder '{root_folder}' not found.")
        return

    styles = getSampleStyleSheet()
    style_normal = styles["Normal"]

    # os.walk yields: root directory, subdirectories, and filenames
    for root, dirs, files in os.walk(root_folder):
        for filename in files:
            if filename.endswith(".txt"):
                # Construct full paths
                txt_path = os.path.join(root, filename)
                pdf_path = os.path.join(root, filename.replace(".txt", ".pdf"))

                print(f"Processing: {txt_path}")
                
                try:
                    doc = SimpleDocTemplate(pdf_path)
                    content = []
                    
                    with open(txt_path, "r", encoding="utf-8") as f:
                        for line in f:
                            line_text = line.strip()
                            if line_text:
                                content.append(Paragraph(line_text, style_normal))
                                content.append(Spacer(1, 0.1 * inch))

                    doc.build(content)
                except Exception as e:
                    print(f"Failed to convert {filename}: {e}")

# Usage
convert_recursive_txt_to_pdf("data")