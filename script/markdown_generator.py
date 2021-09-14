"""Generator of Markdown files for GitHub content presentation"""
from os.path import dirname, abspath, join

def generate_markdown_files(categories):
    """Generates markdown files for given Categories

    Parameters
    ----------
    categories: List[Category]
        list of Categories to generate '.md' files for
    """

    for category in categories:
        markdown = category.genereate_markdown()
        file_name = f'{__padded_index(category.uuid)}-{category.name}.md'
        path = abspath(join(dirname(__file__), '..', 'Checklists', file_name))
        with open(path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown)

def __padded_index(index):
    return f'{index}' if index >= 10 else f'0{index}'
