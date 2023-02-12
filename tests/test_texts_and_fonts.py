import pytest
import os

from text_manager.text_and_fonts import *

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


def test_GetMainMenuText():
    text_manager = TextAndFontsManager()
    maun_menu_text_eng = text_manager.Get("FIRST_BUTTON_TEXT")

    assert (maun_menu_text_eng[TEXT_INDEX] == "First text")
    assert (maun_menu_text_eng[FONT_INDEX][0] == "Arial")
    assert (maun_menu_text_eng[FONT_INDEX][1] == 25)


    