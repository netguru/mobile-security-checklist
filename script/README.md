# Mobile Security Handbook Generator

This is a simple Python script that performs all operations required 
to generate most recent version of the Mobile Security Checklist.

Data is loaded from the 'requirements.json' and then exported as '.md' and '.xls' files.

## Requirements
-  Python 3.9+

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
                        "references": ["http://www.url_to_reference_article.com"]
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
| SD.1 | High | Login / Signup, keeping user session alive | All tokens / credentials must be stored in keychain/keystore if they are persisted | [1](http://www.url_to_reference_article.com) |
```

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
- generate '.xls' file
- automate with GitHub actions
