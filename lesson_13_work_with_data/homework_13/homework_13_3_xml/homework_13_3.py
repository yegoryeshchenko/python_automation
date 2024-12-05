# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення
# timingExbytes/incoming
# результат виведіть у консоль через логер на рівні інфо

import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def read_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except ET.ParseError as parse_error:
        logging.error(f"Failed to parse XML file: {parse_error}")
        return None


def find_incoming_by_group_number(xml_root, group_number):
    for group in xml_root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == str(group_number):
            incoming = group.find('timingExbytes/incoming')
            if incoming is not None:
                incoming_value = incoming.text
                logging.info(f"Incoming value for group {group_number}: {incoming_value}")
                return incoming_value
            else:
                logging.info(f"Group {group_number} does not have an 'incoming' value.")
                return None
    logging.info(f"Group with number {group_number} not found.")
    return None


xml_tree = read_xml_file('groups.xml')
find_incoming_by_group_number(xml_tree, 1)
find_incoming_by_group_number(xml_tree, 2)
find_incoming_by_group_number(xml_tree, 3)
find_incoming_by_group_number(xml_tree, 4)
find_incoming_by_group_number(xml_tree, 5)
