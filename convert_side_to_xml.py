import json
import xml.etree.ElementTree as ET

with open("login.side", "r") as f:
    data = json.load(f)

root = ET.Element("testSuite")

for test in data.get("tests", []):
    test_case = ET.SubElement(root, "testCase")
    test_case.set("name", test.get("name", "Unnamed"))

    for command in test.get("commands", []):
        step = ET.SubElement(test_case, "step")

        ET.SubElement(step, "command").text = command.get("command", "")
        ET.SubElement(step, "target").text = command.get("target", "")
        ET.SubElement(step, "value").text = command.get("value", "")

tree = ET.ElementTree(root)
tree.write("output.xml")

print("Done converting!")
