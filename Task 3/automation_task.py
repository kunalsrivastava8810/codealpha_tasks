import os
import re
import shutil

import requests


def move_jpg_files(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    moved_files = 0

    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)

        if os.path.isfile(source_path) and file_name.lower().endswith(".jpg"):
            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(source_path, destination_path)
            moved_files += 1

    print(f"Moved {moved_files} JPG file(s) to {destination_folder}.")


def extract_email_addresses(input_file, output_file):
    email_pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    emails = sorted(set(re.findall(email_pattern, content)))

    with open(output_file, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"Extracted {len(emails)} email address(es) to {output_file}.")


def scrape_webpage_title(url, output_file):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    title_match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "No title found"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(title + "\n")

    print(f"Saved webpage title to {output_file}: {title}")


def get_input_path(prompt):
    return os.path.abspath(input(prompt).strip())


def main():
    print("Small Task Automation")
    print("1. Move all .jpg files to a new folder")
    print("2. Extract email addresses from a .txt file")
    print("3. Scrape a webpage title and save it")

    choice = input("Choose an option (1/2/3): ").strip()

    if choice == "1":
        source_folder = get_input_path("Enter the source folder path: ")
        destination_folder = get_input_path("Enter the destination folder path: ")
        move_jpg_files(source_folder, destination_folder)
    elif choice == "2":
        input_file = get_input_path("Enter the input .txt file path: ")
        output_file = get_input_path("Enter the output file path: ")
        extract_email_addresses(input_file, output_file)
    elif choice == "3":
        url = input("Enter the webpage URL: ").strip()
        output_file = get_input_path("Enter the output file path: ")
        scrape_webpage_title(url, output_file)
    else:
        print("Invalid choice. Please run the script again and choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
