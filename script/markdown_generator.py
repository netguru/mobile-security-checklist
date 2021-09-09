from os.path import dirname, abspath, join

def generate_markdown_files(categories):
    for category in categories:
        markdown = category.genereate_markdown()
        with open(abspath(join(dirname(__file__), '..', 'Checklists', f'{__padded_index(category.id)}-{category.name}.md')), 'w') as md_file:
            md_file.write(markdown)

def __padded_index(index):
    return f'{index}' if index >= 10 else f'0{index}'
