import xml.etree.ElementTree as ET
import json


def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in result:
            if type(result[child.tag]) is list:
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    return result


def extract_xml_info(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        data_dict = {root.tag: xml_to_dict(root)}
        json_data = json.dumps(data_dict, indent=2)
        return json_data
    except Exception as e:
        return f"Error converting XML to JSON: {str(e)}"


xml_path = r"D:\git_training\unittest\bt\769793.xml"
xml_info = extract_xml_info(xml_path)
print(xml_info)