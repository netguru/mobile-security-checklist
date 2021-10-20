"""Genereal constants used withing this script"""
from enum import Enum

class Url(Enum):
    """Enum with all URL adresses used in the script"""
    REPO = 'https://github.com/netguru/mobile-security-checklist/tree/master/'

class Color(Enum):
    """Enum with all color hex values used in the script"""
    TODO  = '00FFFFFF'
    DONE  = '00B7E1CD'
    WONT_FIX  = '00FCE8B2'
    NOT_APPLICABLE  = '00B7B7B7'

class SpreadsheetRowIndex(Enum):
    """Enum with index numbers of specific rows in xlsx spreadsheet"""
    FIRST = 1
    LAST = 980
