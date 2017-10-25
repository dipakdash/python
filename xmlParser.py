# This script could be used to parse any XML file to get the following:
# XML Tags names (Also called Elements)
# XML Element Attibutes

import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self, xml_file):
         self.xml_file = xml_file
         self.tree = ET.parse(self.xml_file)
         self.root = self.tree.getroot()
         # print type(self.root.tag)       # A str object
         # print type(self.root.attrib)    # A dict object
         self.elements = []                # This would contain duplicate elements if the XML file has got duplicate elements 
         self.elements_unique = []         # This list would contain unique elements existing in the entire XML file
         self.attributes = []              # This would contain duplicate attributes if the XML file has got duplicate attributes
         self.attributes_unique = []       # This list would contain unique attributes existing in the entire XML file
         self.element_attrib = {}          # This would contain the element:attrib mapping     
         self._create_unique_element_and_attrib_lists()
         self._map_elements_to_attribs()

    def _create_unique_element_and_attrib_lists(self):
        for child in self.root:
            element = str(child.tag)
            self.elements.append(element)
            attribute = str(child.attrib)
            for (k, v) in child.attrib.iteritems():
                self.attributes.append(k)
            
        # [self.elements_unique.append(item) for item in self.elements if item not in self.elements_unique]
        # [self.attributes_unique.append(item) for item in self.attributes if item not in self.attributes_unique]
        self.elements_unique = set(self.elements)        # Better way to make a list unique
        self.attributes_unique = set(self.attributes)    # Better way to make a list unique
                          
    def _map_elements_to_attribs(self):
        for child in self.root:
            if str(child.tag) not in self.element_attrib: # To ensure a key value [] is not over written due to duplicate key (child.tag))
                self.element_attrib[str(child.tag)] = []
            for (k, v) in child.attrib.iteritems():
                if k not in self.element_attrib[str(child.tag)]: # To ensure no duplicate key values are appended to the dictionary value lists
                    self.element_attrib[str(child.tag)].append(k)
        
    # Get all the value of the attributes of the matching element. There might be multiple element with same attribute and different values.
    # Returns a list of found attribute values for an (element, attribute) pair
    def get_element_attribute_value_list(self, element, attribute):
        attrib_value_list = []
        for elm in self.root.findall(element.strip()):
            att = elm.get(attribute.strip())
            if att:
                attrib_value_list.append(att)
        return attrib_value_list

    # Returns True if (element --> attribute --> value) is found else False
    def check_element_attribute_value(self, element, attribute, value):
        value_list = self.get_element_attribute_value_list(element.strip(), attribute.strip())
        if value.strip() in value_list:
            return True
        else:
            return False
        
if __name__ == "__main__":
    xml_file = 'request_features_decoded.xml'
    xp = XMLParser(xml_file)
   
    # element = 'FileSystemLogging '
    # attribute = 'LogNameS '
    # value = '30'
    # print xp.get_element_attribute_value_list(element, attribute)
    # print xp.check_element_attribute_value(element, attribute, value)
    
    # for (element, attriblist) in xp.element_attrib.iteritems():
            # for attribute in attriblist:
                # list = xp.get_element_attribute_value_list(element, attribute)
                # print element + ' --> ' + attribute + ' --> ' + str(list)
    
    f = open('xml_out.txt', 'w')
    for (k, v) in xp.element_attrib.iteritems():
        f.write(k + ' = ' + str(v))
        f.write('\n')
    f.close()