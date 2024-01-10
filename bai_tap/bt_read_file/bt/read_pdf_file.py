import json
import fitz


def extract_xml_info(pdf_path):
    pdf_info = {}

    pdf_document = fitz.open(pdf_path)

    num_page = pdf_document.page_count
    pdf_info["num_pages"] = num_page

    page_info_list = []
    for page_number in range(num_page):
        page = pdf_document[page_number]
        page_info = {
            "page_number": page_number + 1,
            "text": page.get_text("text"),
        }
        page_info_list.append(page_info)

    pdf_info["pages"] = page_info_list

    pdf_document.close()

    return pdf_info


pdf_path = r"D:\git_training\unittest\bt\769367.pdf"
pdf_info = extract_xml_info(pdf_path)
print(json.dumps(pdf_info, indent=2))

pdf_path = r"D:\git_training\unittest\bt\hd.pdf"
pdf_info = extract_xml_info(pdf_path)
print(json.dumps(pdf_info, indent=2))
