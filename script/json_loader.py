"""Loader of MobSec Checklist content from JSON file"""
from json import load
from os.path import dirname, abspath, join

from category import Category

def load_data():
    """Loads MobSec Checlist data from 'requirements.json' file.

    Returns list of Categories loaded from the JSON file.
    """

    path = abspath(join(dirname(__file__), '..', 'requirements.json'))
    with open(path, encoding='utf-8') as json_file:
        json = load(json_file)
        return __load_categories(json)

def __load_categories(json):
    categories = []
    for uuid, category_json in enumerate(json, 1):
        categories.append(Category.load_json(uuid, category_json))
    return categories
