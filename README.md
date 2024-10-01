# Conversion of JSON data to XML file

## Description

This project effectively converts the json data to XML file. This python program make use of the XML tree package. The entire program is coded using recursion.

## Libraries used

1) XML TREE

## How to run?

1) Clone this repository
2) open your JSON data file.
3) after placing the data run the program.
4) the program write the XML file to your directory.
5) View your XML file.

## Code 

```
import json
import xml.etree.ElementTree as ET

def json_to_xml(json_data):
    object = ET.Element("Object")
    

    def process_element(element, parent):
        if isinstance(element, dict):
            for key, value in element.items():  
                    process_element(value, parent)  

        elif isinstance(element, list):
           for value in element:
               child = ET.SubElement(parent,"Array" )
               process_element(value, parent)
        elif isinstance(element, bool):
            child = ET.SubElement(parent,"Boolean" ,name=str(element) )
            child.text=str(element)
        elif isinstance(element, int):
             child = ET.SubElement(parent,"Number", name=str(element) )
             child.text=str(element)
            #  parent.text=str(element)
        elif isinstance(element, str):
            
                 child = ET.SubElement(parent,"String",name=str(element) )
                 child.text=str(element)
        elif isinstance(element, type(None)):
            
                 child = ET.SubElement(parent,"Null",name=str(element) )
                 child.text=str(element)
        else:
            
            parent.text=str(element)         
            
            

    process_element(json_data, object)

    tree = ET.ElementTree(object)
    tree.write("output.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    sample_json ={"person": {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "has":True,
                "Married":None
            }
        } 
        }
    json_to_xml(sample_json)
    print("xml file written")

    
```

## Authors

Prakash