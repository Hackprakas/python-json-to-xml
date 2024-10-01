import json
import xml.etree.ElementTree as ET

def json_to_xml(json_data):
    object = ET.Element("Object")
    

    def process_element(element, parent,key=None):
        if isinstance(element, dict):
            if key:
                child = ET.SubElement(parent,"Dictionary",name=key)
            else:
                child = ET.SubElement(parent,"Dictionary")
            for key, value in element.items(): 
                    process_element(value, child,key)  

        elif isinstance(element, list):
               child = ET.SubElement(parent,"Array",name=key if key else "" )
               for value in element:
                    process_element(value, child)
        elif isinstance(element, bool):
            child = ET.SubElement(parent,"Boolean" ,name=key if key else "" )
            child.text=str(element)
        elif isinstance(element, int):
             child = ET.SubElement(parent,"Number", name=key if key else "" )
             child.text=str(element)
            
        elif isinstance(element, str):
            
                 child = ET.SubElement(parent,"String",name=key if key else "" )
                 child.text=str(element)
        elif isinstance(element, type(None)):
            
                 child = ET.SubElement(parent,"Null",name=key if key else "" )
                 child.text=str(element)
        else:
            
            parent.text=str(element)         
            
            

    process_element(json_data, object)

    tree = ET.ElementTree(object)
    tree.write("output.xml")

if __name__ == "__main__":
    with open('sample.json',"r") as json_file:
        try:
             datas = json.load(json_file)
             json_to_xml(datas)
             print("xml file written")
        except:
         print("something went wrong..pls upload a valid JSON FILE")

    
