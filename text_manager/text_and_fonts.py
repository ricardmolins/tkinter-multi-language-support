import csv
import os

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(funcName)s:%(message)s')

file_handler = logging.FileHandler('run.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

TEXT_INDEX = 0
FONT_INDEX = 1

import platform

class TextAndFontsManager:


    def __init__(self):

        base_folder = os.path.dirname(__file__)
        texts_csv = os.path.join(base_folder, 'texts.csv')
        fonts_csv = os.path.join(base_folder, 'fonts.csv')
        print(platform.python_version())


        # Read Text CSV
        with open(texts_csv, newline='', encoding="ISO-8859-1") as csvfile:
            data_text = list(csv.reader(csvfile))
            csvfile.close()

        # Read Font CSV
        with open(fonts_csv, newline='', encoding="ISO-8859-1") as csvfile:
            data_csv = list(csv.reader(csvfile))
            csvfile.close()


        logger.debug(data_text)
        logger.debug(data_csv)

        # Getting heading columns 
        self.text_headings_string = data_text.pop(0)
        self.texts_data = data_text
        self.font_headings_string = data_csv.pop(0)
        self.font_data = data_csv

        # Update Column index of TEXTS
        self.text_col_alias = self.text_headings_string.index("Alias")
        self.col_language = self.text_headings_string.index("eng")
        self.text_col_font = self.text_headings_string.index("Font")
        # Update Column index of FONTS
        self.font_col_alias = self.font_headings_string.index("Alias")
        self.font_col_name = self.font_headings_string.index("Name")
        self.font_col_size = self.font_headings_string.index("Size")
        self.font_is_bold = self.font_headings_string.index("Bold")
        self.font_is_italic = self.font_headings_string.index("Italic")
        self.font_is_underline = self.font_headings_string.index("Underline")
        self.dict_alias_to_font = dict() # Given font ID gives font
        self.dict_alias_to_text = dict() # Given text ID gives (text, font_id)
        self._UpdateAliasToText()
        self._UpdateAliasToFont()

    def _UpdateAliasToFont(self):
        dict_alias_to_font = dict()
        for i in range(0, len(self.font_data), 1):
            data_entry = self.font_data[i]
            data_entry_alias = data_entry[self.font_col_alias]
            data_entry_font_name = data_entry[self.font_col_name]
            data_entry_font_size = data_entry[self.font_col_size]

            font_style = ""
            if ( data_entry[self.font_is_bold] != "0" ):
                font_style += "bold "
            if ( data_entry[self.font_is_italic] != "0" ):
                font_style += "italic "
            if ( data_entry[self.font_is_underline] != "0" ):
                font_style += "underline "
            
            if font_style!="":
                dict_alias_to_font[data_entry_alias] = (data_entry_font_name, int(data_entry_font_size),font_style.strip())
            else:
                dict_alias_to_font[data_entry_alias] = (data_entry_font_name, int(data_entry_font_size))
        self.dict_alias_to_font = dict_alias_to_font

    def _UpdateAliasToText(self):
        dict_alias_to_text = dict()
        for i in range(0, len(self.texts_data), 1):
            data_entry = self.texts_data[i]
            data_entry_alias = data_entry[self.text_col_alias]
            data_entry_text = data_entry[self.col_language]
            data_entry_font_id = data_entry[self.text_col_font]
            # Updating the dictionaris
            dict_alias_to_text[data_entry_alias] = (data_entry_text,data_entry_font_id)
            
        self.dict_alias_to_text = dict_alias_to_text

    def SetLanguage(self, language):
        try: 
            self.col_language = self.text_headings_string.index(language)
        except ValueError:
            logger.debug("Language does not exist")
            self.col_language = self.text_headings_string.index("eng")

        self._UpdateAliasToText()

    def GetText(self, text_id):
        my_text = ""
        try: 
            my_text = self.dict_alias_to_text[text_id][0]
        except KeyError:
            logger.debug("Key " + text_id + " does not exists")
        return my_text

    def GetFont(self,font_id):
        # Setting default font 
        my_text = ("Arial", 99) 
        try: 
            my_text = self.dict_alias_to_font[font_id]
        except KeyError:
            logger.debug("Key " + font_id + " does not exists")
        return my_text

    def Get(self, text_id):
        my_text = ""
        my_font = ("Arial", 10) 
        try: 
            text_data = self.dict_alias_to_text[text_id]
            my_text = text_data[TEXT_INDEX]
            font_id  = text_data[FONT_INDEX]
            my_font = self.GetFont(font_id)
        except KeyError:
            logger.debug("Key " + text_id + " does not exists")
        return my_text, my_font

    def GetFontFromText(self, text_id):
        my_font = ("Arial", 10) 
        try: 
            text_data = self.dict_alias_to_text[text_id]
            font_id  = text_data[FONT_INDEX]
            my_font = self.GetFont(font_id)
        except KeyError:
            logger.debug("Key " + text_id + " does not exists")
        return my_font

        