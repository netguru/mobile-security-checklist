from json import load
from os.path import dirname, abspath, join

from category import Category

def load_data():
    with open(abspath(join(dirname(__file__), '..', 'requirements.json'))) as json_file:
        json = load(json_file)
        return __load_categories(json)

def __load_categories(json):
    categories = []
    for id, category_json in enumerate(json, 1):
        categories.append(Category.load_json(id, category_json))
    return categories
