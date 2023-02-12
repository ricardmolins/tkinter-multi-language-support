
from texts.text_and_fonts import *

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


def test_CheckFirstFont():
    text_manager = TextAndFontsManager()

    menu_button_font = text_manager.GetFont("BOTTOM_BUTTONS")

    logger.debug(menu_button_font)

    assert menu_button_font[0] == "Calibri"
    assert menu_button_font[1] == 14

def test_CheckSecondFont():
    text_manager = TextAndFontsManager()

    menu_button_font = text_manager.GetFont("TEXT_BIG")

    logger.debug(menu_button_font)

    assert menu_button_font[0] == "Arial"
    assert menu_button_font[1] == 25

def test_GetFontFromText():
    text_manager = TextAndFontsManager()

    menu_button_font = text_manager.GetFontFromText("FIRST_BUTTON_TEXT")

    logger.debug(menu_button_font)

    assert menu_button_font[0] == "Arial"
    assert menu_button_font[1] == 25

def test_GetFontFromTextWithUnderline():
    text_manager = TextAndFontsManager()

    menu_button_font = text_manager.GetFont("TEST_UNDERLINE")

    logger.debug(menu_button_font)

    assert menu_button_font[0] == "Arial"
    assert menu_button_font[1] == 12
    assert menu_button_font[2] == "underline"

def test_GetFontFromTextWithBold():
    text_manager = TextAndFontsManager()

    menu_button_font = text_manager.GetFont("TEST_BOLD")

    logger.debug(menu_button_font)

    assert menu_button_font[0] == "Arial"
    assert menu_button_font[1] == 12
    assert menu_button_font[2] == "bold"

def test_GetFontFromTextWithBoldAndItalic():
    text_manager = TextAndFontsManager()

    menu_button_font = text_manager.GetFont("TEST_BOLD_ITALIC")

    logger.debug(menu_button_font)

    assert menu_button_font[0] == "Arial"
    assert menu_button_font[1] == 12
    assert menu_button_font[2] == "bold italic"