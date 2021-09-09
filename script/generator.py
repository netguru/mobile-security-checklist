from json_loader import load_data
from markdown_generator import generate_markdown_files

def main():
    categories = load_data()
    generate_markdown_files(categories)

if __name__ == "__main__":
    main()
