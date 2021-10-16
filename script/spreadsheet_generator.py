"""Generator of Spreadsheet file as Mobile Security Checklist core tool"""
from string import ascii_uppercase
from os.path import dirname, abspath, join
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Font,  PatternFill
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from openpyxl.worksheet.datavalidation import DataValidation

__column_widths = [10, 20, 15, 45, 55, 30, 13, 15, 30]
__headers = ['Code', 'Status', 'Category', 'Feature', 'Security requirement',
            'Solution in app / Comments', 'Last updated', 'Priority', 'Reference']
__statuses = ['TODO', 'DONE', 'Won\'t fix', 'Not applicable']
__priorities = ['Critical', 'High', 'Medium', 'Low']
__REPO_URL = 'https://github.com/netguru/mobile-security-checklist/tree/master/'

def generate_spreadsheet(categories):
    """Generates content in 'mobile_security_checklist.xlsx' file for given Categories

    Parameters
    ----------
    categories: List[Category]
        list of Categories to fill '.xlsx' file for
    """
    spreadsheet = load_workbook('checklist_base.xlsx')
    for category in categories[::-1]:
        __generate_sheet(spreadsheet, category)
    spreadsheet.save(abspath(join(dirname(__file__), '..', 'mobile_security_checklist.xlsx')))

def  __generate_sheet(spreadsheet, category):
    new_sheet = spreadsheet.create_sheet(category.name, 1)
    new_sheet.freeze_panes = f'{ascii_uppercase[0]}2'

    # Add data validation to `Status` and `Priority` columns
    status_data_validation = DataValidation(type='list', formula1=f'"{",".join(__statuses)}"')
    priority_data_validation = DataValidation(type='list', formula1=f'"{",".join(__priorities)}"')
    for data_validation in [status_data_validation, priority_data_validation]:
        new_sheet.add_data_validation(data_validation)

    # Add conditional formatting
    start_cell = f'{ascii_uppercase[0]}2'
    end_cell = f'{ascii_uppercase[len(__headers)-1]}980'
    colors = ['00FFFFFF', '00B7E1CD', '00FCE8B2', '00B7B7B7']
    conditional_formattings = {}
    for status, color in zip(__statuses, colors):
        conditional_formattings[status] = {
            "range": f'{start_cell}:{end_cell}',
            "formula": f'${ascii_uppercase[1]}2="{status}"',
            "style": DifferentialStyle(fill=PatternFill(bgColor=color, fill_type='solid'))
        }
    for conditional_formatting in conditional_formattings.values():
        new_sheet.conditional_formatting.add(
            conditional_formatting['range'],
            Rule(
                type='expression',
                formula=[conditional_formatting['formula']],
                dxf=conditional_formatting['style']
            )
        )

    current_row = 1

    # Generate headers row
    for column, header in zip(ascii_uppercase, __headers):
        new_sheet[f'{column}{current_row}'] = header
        new_sheet[f'{column}{current_row}'].font = Font(bold=True)
        new_sheet[f'{column}{current_row}'].border = Border()

    # Apply proper column widths
    for column, width in zip(ascii_uppercase, __column_widths):
        new_sheet.column_dimensions[column].width = width

    current_row += 1

    # Generate rows for requirements
    should_add_header = len(category.groups) > 1
    status_cell = f'{ascii_uppercase[1]}{current_row}'
    date_cell = f'{ascii_uppercase[5]}{current_row}'
    for group in category.groups:
        for requirement in group.requirements:
            data = [
                f'{category.code}{group.code if should_add_header else ""}.{requirement.uuid}',
                 __statuses[0],
                 group.name,
                 requirement.feature.replace("<br>","\n"),
                 requirement.description.replace("<br>","\n"),
                 '',
                 f'=IFERROR({status_cell}+{date_cell}{current_row}+"x",TODAY())',
                 requirement.priority.title()
            ]
            for column, value in zip(ascii_uppercase, data):
                new_sheet[f'{column}{current_row}'] = value
                new_sheet[f'{column}{current_row}'].alignment = Alignment(wrap_text=True)

            # Apply proper style and format for 'Last updated' column
            last_updated_col = f'{ascii_uppercase[6]}{current_row}'
            new_sheet[last_updated_col].number_format = 'DD/MM/YYYY'
            new_sheet[last_updated_col].alignment = Alignment(horizontal="right", wrap_text=True)

            # Apply proper style and url for 'Reference' column
            reference_col = f'{ascii_uppercase[8]}{current_row}'
            hyperlink = f'{__REPO_URL}{requirement.reference.replace("../", "")}'
            new_sheet[reference_col].hyperlink = hyperlink
            new_sheet[reference_col].value  = 'Handbook'
            new_sheet[reference_col].style = 'Hyperlink'

            # Apply data validation to `Status` and `Priority` columns
            status_data_validation.add(new_sheet[f'{ascii_uppercase[1]}{current_row}'])
            priority_data_validation.add(new_sheet[f'{ascii_uppercase[7]}{current_row}'])

            current_row += 1

    # Apply data filters to `Category` column
    new_sheet.auto_filter.ref = f'{ascii_uppercase[2]}1:{ascii_uppercase[2]}{current_row-1}'
