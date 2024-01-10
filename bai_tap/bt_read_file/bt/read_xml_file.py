import xmltodict
import json


with open(r"D:\git_training\unittest\bt\769793.xml", 'r', encoding='utf-8') as xml_file:
    xml_data = xml_file.read()

xml_dict = xmltodict.parse(xml_data)
print(json.dumps(xml_dict, indent=2))


#dùng đệ quy
# import xml.etree.ElementTree as ET
# import json
#
#
# def xml_to_dict(element):
#     if len(element) == 0:
#         return element.text
#     result = {}
#     for child in element:
#         child_data = xml_to_dict(child)
#         if child.tag in result:
#             if type(result[child.tag]) is list:
#                 result[child.tag].append(child_data)
#             else:
#                 result[child.tag] = [result[child.tag], child_data]
#         else:
#             result[child.tag] = child_data
#     return result
#
#
# def extract_xml_info(xml_path):
#     try:
#         tree = ET.parse(xml_path)
#         root = tree.getroot()
#         data_dict = {root.tag: xml_to_dict(root)}
#         json_data = json.dumps(data_dict, indent=2)
#         return json_data
#     except Exception as e:
#         return f"Error converting XML to JSON: {str(e)}"
#
#
# xml_path = r"D:\git_training\unittest\bt\769793.xml"
# xml_info = extract_xml_info(xml_path)
# print(xml_info)


# def convert_xml_to_json(xml_string):
#     root = ET.fromstring(xml_string)
#     data_dict = {root.tag: xml_to_dict(root)}
#     json_data = json.dumps(data_dict, indent=2)
#     return json_data
#
# # Ví dụ sử dụng chuỗi XML từ câu hỏi của bạn
# xml_string = """<TTKhac><TTin><TTruong>PortalLink</TTruong><KDLieu>string</KDLieu><DLieu>http://0402131186hd.easyinvoice.com.vn</DLieu></TTin><TTin><TTruong>Fkey</TTruong><KDLieu>string</KDLieu><DLieu>U6U3Y8v00760702671042141UtPB</DLieu></TTin></TTKhac>"""
#
# json_data = convert_xml_to_json(xml_string)
# print(json_data)