import json
import fitz


def extract_xml_info(xml_path):
    xml_info = {}

    xml_document = fitz.open(xml_path)

    num_page = xml_document.page_count
    xml_info["num_pages"] = num_page

    page_info_list = []
    for page_number in range(num_page):
        page = xml_document[page_number]
        page_info = {
            "page_number": page_number + 1,
            "text": page.get_text("text"),
        }
        page_info_list.append(page_info)

    xml_info["pages"] = page_info_list

    xml_document.close()

    return xml_info


xml_path = r"D:\git_training\unittest\bt\769793.xml"
xml_info = extract_xml_info(xml_path)
print(json.dumps(xml_info, indent=2))
