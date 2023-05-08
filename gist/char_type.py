#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

from enum import Enum, auto

class CharType(Enum):
    UPPER = auto()
    LOWER = auto()
    NUMBER = auto()
    HIRAGANA = auto()
    KATAKANA = auto()
    KANJI = auto()
    SPACE = auto()
    ZENKAKU_SPACE = auto()
    CARRIAGE_RETURN = auto()
    LINE_FEED = auto()
    OTHER = auto()


def get_char_type(c):
    code = ord(c)
    logger.debug("c, code {} {}".format(c, code)) # debug
    if ord("A") <= code <= ord("Z"):
        return CharType.UPPER
    elif ord("a") <= code <= ord("z"):
        return CharType.LOWER
    elif ord("0") <= code <= ord("9"):
        return CharType.NUMBER
    elif ord("ぁ") <= code <= ord("ゖ"):
        return CharType.HIRAGANA
    elif ord("ァ") <= code <= ord("ヺ"):
        return CharType.KATAKANA
    elif ord("一") <= code <= ord("\u9fef"):
        return CharType.KANJI
    elif code == ord(" "):
        return CharType.SPACE
    elif code == ord("　"):
        return CharType.ZENKAKU_SPACE
    elif code == ord("\r"): # carriage return
        return CharType.CARRIAGE_RETURN
    elif code == ord("\n"):
        return CharType.LINE_FEED
    else:
        return CharType.OTHER
