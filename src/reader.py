import argparse
import os
import webbrowser
import fitz


def read_pdf_paths(folder_path):
    pdf_paths = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            pdf_paths.append(file_path)
    return pdf_paths


def read_pages_from_pdfs(pdf_paths):
    pdfs_pages = []
    for i, pdf_path in enumerate(pdf_paths):
        doc = fitz.open(pdf_path)
        for j in range(len(doc)):
            page = doc.load_page(j)
            text = page.get_text().lower()
            if text:
                pdfs_pages.append({'text': text, 'page': j, 'pdf': i})
    return pdfs_pages


def find_page(pdfs_pages, text):
    found_pages = []
    text = text.lower()
    for pdf_page in pdfs_pages:
        if text in pdf_page['text']:
            found_pages.append({'page_num': pdf_page['page'], 'pdf_num': pdf_page['pdf']})
    return found_pages


def open_pdf_at_page(pdf_path, page_num):
    if os.path.exists(pdf_path):
        pdf_url = f"file://{os.path.abspath(pdf_path)}#page={page_num + 1}"
        webbrowser.open(pdf_url)
    else:
        print("PDF file not found at:", pdf_path)


def main(folder_path, search_text):
    pdf_paths = read_pdf_paths(folder_path)
    pdfs_pages = read_pages_from_pdfs(pdf_paths)
    found_pages = find_page(pdfs_pages, search_text)

    for found_page in found_pages:
        pdf_num = found_page['pdf_num']
        page_num = found_page['page_num']
        pdf_path = pdf_paths[pdf_num]
        open_pdf_at_page(pdf_path, page_num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search text in PDF files within a folder and open the pages.")
    parser.add_argument('folder_path', type=str, nargs='?', default='pdfs', help='Path to the folder containing PDF files')
    parser.add_argument('search_text', type=str, help='Text to search within the PDF files')

    args = parser.parse_args()
    main(args.folder_path, args.search_text)
