import xml.etree.ElementTree as ET

# Завантаження XML-файлу
tree = ET.parse('example_xml.xml')
root_el = tree.getroot()


# steps = [{'id': 1, 'name': '', 'actions': [], 'steps': [{...}]}]


for group in root_el.findall('group'):

    bbo_in_group = group.find('bbo')
    bbo_fild_all_in_group = group.findall('bbo')
    print('bbo in group', bbo_in_group)
    print('bbo bbo_fild_all_in_group group', bbo_fild_all_in_group)

    timing_exbytes = group.find('timingExbytes')

    if timing_exbytes is not None:
        bbo = timing_exbytes.find('bbo')
        if bbo is not None:
            print(f"Group: {group.find('name').text}, bbo: {bbo.text}")
        else:
            print(f"Group: {group.find('name').text}, bbo: Не знайдено")

# for sub_el in root_el:
#
#     print(sub_el, '--' * 80)
#     for child in sub_el:
#         print(child.tag)
#
#         if child.tag == 'timingExbytes':
#             for k in child:
#                 if k.tag == 'bbo':
#                     print(f'bbo text', k.text)


root = ET.Element('data')

# Створення під-елементів та додавання їх до кореневого елемента
child1 = ET.SubElement(root, 'child1')
child1.text = 'Data 1'
child2 = ET.SubElement(root, 'child2')
child2.text = 'Data 2'

child2 = ET.SubElement(child2, 'sub-child')
child2.text = 'sub-child 12'


# Запис у XML-файл
tree = ET.ElementTree(root)
tree.write('output.xml')