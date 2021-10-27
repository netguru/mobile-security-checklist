# Mobile Security Handbook Generator

This is a simple Python script that performs all operations required 
to generate most recent version of the Mobile Security Checklist.

Data is loaded from the 'requirements.json' and then exported as '.md' and '.xlsx' files.

## Requirements
-  Python 3.9+
-  openpyxl 3.0.9+

## Usage

### requirements.json
All requirements data is loaded from a single file — `requirements.json`. The data is structurized into Categories, Groups and Requirements. Each Category is a separate Markdown file or spreadsheet sheet. Category include one or more Groups, for each there's separate Markdown table of associated Requirements.

Example of `requirements.json` file with one Category, Group and Requirement:
```json
[
    {
        "name": "Shared",
        "description": "Shared security requirements between platforms",
        "code": "S",
        "groups": [
            {
                "name": "Default",
                "code": "D",
                "requirements": [
                    {
                        "priority": "high",
                        "feature": "Login / Signup, keeping user session alive",
                        "description": "All tokens / credentials must be stored in keychain/keystore if they are persisted",
                        "reference": "../Handbooks/TODO.md"
                    }
                ]
            },
            ...
        ]
    },
    ...
]
```
With given `requirements.json` file, following Markdown content will be created:
```
# Shared security requirements between platforms

## Default

| ID  | Priority | Feature | Description | Link |
| --  | -- | ---------------------- | ---------------------- | - |
| SD.1 | High | Login / Signup, keeping user session alive | All tokens / credentials must be stored in keychain/keystore if they are persisted | [Handbook](../Handbooks/TODO.md) |
```

The script also generates spreadhseet `mobile_security_checklist.xlsx` to fill while working with the Mobile Security Checklist.
Generation of the `.xlsx` file is based on both `requirements.json` and `script/checklist_base.xlsx` files. The later is used to prefill informative sheets of the spreadsheet.

### Launching the script
To launch the script simply execute the `generator.py` file. The script does not take any arguments.
```bash
python generator.py
```
or
```bash
./generator.py
```

## TODO
- automate with GitHub actions.
- update script (insert new requirements rows into existing checklist spreadsheet).
