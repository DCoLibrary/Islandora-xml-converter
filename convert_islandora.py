################################################################
# Script written by Daniel Davis for the Durham County Library
# SplitS XML containing many <mods> elements into invidual files
# Modified from xmp_split.py script found here: https://github.com/calhist/xml_splitter
################################################################

#IMPORT REQUIRED DEPENDENCIES
import os, lxml
from lxml import etree as ET
import sys


#IMPORT TKINTER LIBRARIES FOR GUI INTERFACE
from tkinter import filedialog as fd
from tkinter import Tk, Label, Button, ttk
from tkinter import messagebox
from tkinter import *

#INITIALIZE GUI
xml_converter = Tk()
xml_converter.title('Islandora XML converter')
xml_converter.geometry("700x400")
filename = "filename";

basedir = os.path.dirname(sys.argv[0])

#OPEN XML FILE
def open_file():
    global xml_file
    xml_file = fd.askopenfilename(filetypes=(("xml files","*.xml"),("all files","*.*")))
    status_label["text"] = "Status: File Selected! - " + xml_file

#CONVERT XML FILE
def convert_xml():
	#define variables
    global save_directory
    save_directory = fd.askdirectory()
    tree = ET.parse(os.path.join(xml_file))
    
    # start cleanup
    # remove any element tails
    for element in tree.iter():
        element.tail = None
        # remove any line breaks or tabs in element text
        if element.text:
            if '\n' in element.text:
                element.text = element.text.replace('\n', '') 
            if '\t' in element.text:
                element.text = element.text.replace('\t', '')
            
    # remove any remaining whitespace
    parser = ET.XMLParser(remove_blank_text=True, remove_comments=True, recover=True)
    treestring = ET.tostring(tree)
    clean = ET.XML(treestring, parser)

    # remove recursively empty nodes
    # found here: https://stackoverflow.com/questions/12694091/python-lxml-how-to-remove-empty-repeated-tags
    def recursively_empty(e):
        if e.text:
            return False
        return all((recursively_empty(c) for c in e.iterchildren()))

    context = ET.iterwalk(clean)
    for action, elem in context:
        parent = elem.getparent()
        if recursively_empty(elem):
            parent.remove(elem)

    # remove nodes with blank attribute
    for element in clean.xpath(".//*[@*='']"):
        element.getparent().remove(element)

    # remove nodes with attribute "null"
    for element in clean.xpath(".//*[@*='null']"):
        element.getparent().remove(element)

    # finished cleanup
    # write out to intermediate file
    with open('clean.xml', 'wb') as f:
        f.write(ET.tostring(clean))
    print("XML is now clean")

    # parse the clean xml
    cleanxml = ET.iterparse('clean.xml', events=('end', ))

    # find the <mods> nodes
    for event, elem in cleanxml:
        if elem.tag == '{http://www.loc.gov/mods/v3}mods':

            # the filenames of the resulting xml files will be based on the <identifier> element
            # edit the specific element or attribute if necessary
            identifier = elem.find('{http://www.loc.gov/mods/v3}identifier[@type="Identifier"]').text
            filename = format(identifier + ".xml")
            completename = os.path.join(save_directory, filename)

             # write out to new file
            #with open(output_path+filename, 'wb') as f:
            with open(completename, 'w', encoding='utf-8') as f:
                f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                f.write(ET.tostring(elem, pretty_print = True, encoding='unicode'))
            print("Writing", filename)

    # remove the intermediate file
    os.remove('clean.xml')
    print("All done!")
    status_label["text"] = "Status: SUCCESS!! - Saved to folder " + save_directory + "/"

#CREATE TKINTER INTERFACE
header_label = Label(xml_converter, text="Islandora XML Converter", font="Arial 24 bold")
header_label.pack()
open_lbl = Label(xml_converter, text="Step 1: Open XML file to convert for Islandora", font="bold")
open_lbl.pack()
open_button = Button(xml_converter, text="Open File", command=open_file)
open_button.pack()

convert_label = Label(xml_converter, text = "Step 2: Choose save location and Convert the XML file", font="bold")
convert_label.pack()
convert_button = Button(xml_converter, text="Convert", command=convert_xml)
convert_button.pack()

status_label = Label(xml_converter, text="Status: Choose File", font="Arial 8 bold")
status_label.pack()

xml_converter.mainloop()

