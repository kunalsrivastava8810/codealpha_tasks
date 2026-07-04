# Small Task Automation

This project automates three common repetitive tasks:

- Move all `.jpg` files from one folder to another.
- Extract all email addresses from a `.txt` file and save them to another file.
- Scrape the title of a fixed webpage and save it.

## Key Concepts Used

- `os` for folder paths and file checks
- `shutil` for moving files
- `re` for extracting emails and webpage titles
- `requests` for fetching webpage HTML
- File handling with `open()`

## How to Run

Install the only external dependency:

```bash
pip install requests
```

Run the script:

```bash
python automation_task.py
```

Then choose one of the menu options and enter the requested paths or URL.

## Example Email Input

You can test option 2 with `sample_contacts.txt`.
