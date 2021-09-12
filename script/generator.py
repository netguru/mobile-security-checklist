#! /usr/bin/python3
"""Main module of the MobSec Checklist generator script"""
from json_loader import load_data
from markdown_generator import generate_markdown_files

def main():
    """Entry point of the MobSec Checklist generator script.

    This performs all operations required to generate most recent version
    of the Mobile Security Checklist.

    Data is loaded from the 'requirements.json' and then exported as
    proper '.md' and '.xls' files.
    """

    categories = load_data()
    generate_markdown_files(categories)

if __name__ == "__main__":
    main()
