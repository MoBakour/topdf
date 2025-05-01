from docx2pdf import convert
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Convert DOCX to PDF")
    parser.add_argument("input", help="File name")
    args = parser.parse_args()

    # Auto-append .docx if not already included
    docx_path = args.input
    if not docx_path.lower().endswith(".docx"):
        docx_path += ".docx"

    if not os.path.exists(docx_path):
        print(f"❌ File not found: {docx_path}")
        sys.exit(1)

    # Determine output file name
    output_path = os.path.splitext(docx_path)[0] + ".pdf"

    try:
        convert(docx_path)
        print(f"✅ Converted: {docx_path} -> {output_path}")
    except Exception as e:
        print(f"❌ An error occurred during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
