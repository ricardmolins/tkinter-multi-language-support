# tkinter-text-manager

Tool to adds a text and font manager for any GUI using python. Tkinter examples are shown but can be used with any python GUI

Allows
 * All texts and fonts are described in a ```texts_and_fonts.ods``` file which can be modified for non programmers. This allows
   * Manage multiple languages texts without having to modify any code.
   * Simple interface for a translator to do its work
 * Assign fonts to a specific text to simplify refactoring/changes in GUI design
 * All text parameters are centralized in an ```.ods``` file. GUI logic totally separated from text

The module allows definig ```TEXT_ID```s  and ```FONT_ID```s which can later be used within the tkinter objects

## Font ID
Contains the information that describes a font and an alias 
|Alias	|Name	|Size|	Bold|	Italic	|Underline|
|---|---|---|---|---|---|
|FONT_ALIAS_STRING	|Calibri|	14|	0|	0|	0|


## Text ID
|Alias	|Font	|eng|	cat|
|---|---|---|---|
|ALIAS_STRING |	```FONT_ALIAS_STRING```	|First text	|Primer text|


# Integration

All the text/font information is placed in ```texts_and_fonts.ods```. This file is saved in two ```.csv``` files.

* ```fonts.csv```: contains fonts IDS and its values
* ```texts.csv```: contains text IDS and its associated fonts.

Modify the ```texts_and_fonts.ods```, then update the ```.csv``` files.

CSV must be in format Western Europe ISO 8859-15/EURO. UTF 8 format has issues with accents

## Example code to add a text to a tkinter object

```
text_manager = TextAndFontsManager()
label_2 = ttk.Label(root, text = text_manager.GetText("SECOND_BUTTON_TEXT"))
```
## Example code to change language and update text
```
# Set the text 
text_manager = TextAndFontsManager()
text_manager.SetLanguage("eng")
label_2 = ttk.Label(root, text = text_manager.GetText("SECOND_BUTTON_TEXT"))
# Change the language and set the text again
text_manager.SetLanguage("cat")
label_2.configure(text=text_manager.GetText("SECOND_BUTTON_TEXT"))

``` 

# Notes because I forget things

* Create virtual enviroment: python3 -m venv text_manager_venv
* Activate virtual environment: source text_manager_venv/bin/activate
* Run test: python -m pytest tests
* Run example: python example.py
* Install dependencies: sudo apt-get install python3-tk
