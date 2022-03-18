# OpenRefine XML Convert
### A tool for converting OpenRefine XML to individual XML files for use in programs like Islandora 
<p align="center">
  <img alt="GUI Interface" width="500" src="https://github.com/gigafide/Islandora-xml-converter/blob/main/images/screenshot.PNG">
</p>

This script is based on the work of **[@calhist](https://github.com/calhist)** and their **(XML Splitter)(https://github.com/calhist/xml_splitter)** python script.
It takes OpenRefine XML ouput and breaks it down into individual XML files for use in programs like [Islandora](https://www.islandora.ca/).
This specific version of the script updates to Python 3 and adds a Tkinter GUI and file browser to streamline the converstion process.


## Usage Instructions

1. Download the [Executable](dist) (located in the **dist** folder of this repository)
2. Once downloaded, double-click on **convert_islandora.exe** to launch it.
<p align="center">
  <img alt="Image of Executable Icon" src="https://user-images.githubusercontent.com/2020580/159050066-9170324c-3b7b-4b34-b602-925c44a6a72c.png">
</p>

3. Click the *Open File* button. Use the file browser choose your OpenRefine XML file.
<p align="center">
  <img alt="Image of opening file" width="500" src="https://user-images.githubusercontent.com/2020580/159051087-28ab52b1-97b7-48ea-85a9-e0bb63ca9771.png">
</p>

4. Once selected, click on the *Convert* button. Use the file browser to choose a folder in which to place the outputted files.
<p align="center">
  <img alt="Image of converting file" width="500" src="https://user-images.githubusercontent.com/2020580/159051548-bf14eff6-b15d-4c1f-9ae8-ef2a0d58bdc8.png">
</p>

5. After the output folder is selected, the program will automatically create individual XML files from the OpenRefine data. Status can be viewed in the executable terminal
<p align="center">
  <img alt="Image of final output" width="500" src="https://user-images.githubusercontent.com/2020580/159051785-d8ff46b9-1ed2-4798-a5b8-a454f97b83f2.png">
</p>

## Editing/Modifying Instructions
### Pre-requisits - Setting up the environment
1. Download the latest version of [Python 3](https://www.python.org/downloads/)
2. Double-click to launch the installer. Make sure **Add Python 3.10 to PATH** is checked before clicking *Install Now*
![image](https://user-images.githubusercontent.com/98832967/159059563-3d9fe067-bdc4-464c-bf5e-b395a5e7c2be.png)
3. After installation, open up a command prompt and install the **lxml** library by typing
```
pip install lxml
```
![image](https://user-images.githubusercontent.com/98832967/159059625-519a3a05-20bb-428e-88bc-192b71a4c92b.png)
4. Next, either git clone or download this repository to your desktop
5. Test that the script runs wihtout errors by navigating to the folder where the python script is located and running 
```
python convert_islandora.py
```

### Top contributors: 
1. **[@gigafide](https://github.com/gigafide)**
