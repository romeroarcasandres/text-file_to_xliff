import os
import xml.etree.ElementTree as ET

def prompt_directory():
    """Prompt the user to input the directory containing the text files."""
    while True:
        directory = input("Enter the directory containing the text files: ").strip()
        if os.path.isdir(directory):
            return directory
        print("Invalid directory. Please try again.")

def list_files_with_extension_check(directory, extensions):
    """List files in the directory and prompt for missing extensions."""
    files = []
    asked_extensions = set()
    for filename in os.listdir(directory):
        ext = os.path.splitext(filename)[1]
        if ext in extensions:
            files.append(filename)
        elif ext not in asked_extensions:
            asked_extensions.add(ext)
            print(f"Unrecognized extension '{ext}' for file: {filename}")
            add_lang = input(f"Would you like to add '{ext}' to the recognized extensions? (y/n): ").strip().lower()
            if add_lang == 'y':
                extensions.add(ext)
                print(f"Extension '{ext}' has been added to the recognized list.")
                files.append(filename)
    return files

def prompt_file_selection(files, file_type):
    """Prompt the user to select a file from the list."""
    print(f"Available {file_type} files:")
    for i, file in enumerate(files, 1):
        print(f"{i}: {file}")
    while True:
        try:
            choice = int(input(f"Select the {file_type} file (1-{len(files)}): "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
        except ValueError:
            pass
        print("Invalid selection. Please try again.")

def prompt_language(prompt):
    """Prompt the user to input a language code."""
    return input(f"Enter the {prompt} language code (e.g., 'en', 'fr'): ").strip()

def read_file_lines(filepath):
    """Read lines from a file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def create_xliff(source_file, target_file, source_lang, target_lang, output_file):
    """Create an XLIFF file from the source and target files."""
    source_lines = read_file_lines(source_file)
    target_lines = read_file_lines(target_file)

    if len(source_lines) != len(target_lines):
        print("Error: The source and target files do not have the same number of lines.")
        return

    xliff = ET.Element("xliff", attrib={"version": "1.2", "xmlns": "urn:oasis:names:tc:xliff:document:1.2"})

    file_tag = ET.SubElement(
        xliff, "file",
        attrib={
            "source-language": source_lang,
            "target-language": target_lang,
            "datatype": "plaintext",
            "original": os.path.basename(source_file)
        }
    )

    body = ET.SubElement(file_tag, "body")

    for i, (src, tgt) in enumerate(zip(source_lines, target_lines), start=1):
        trans_unit = ET.SubElement(body, "trans-unit", attrib={"id": str(i)})
        ET.SubElement(trans_unit, "source").text = src
        ET.SubElement(trans_unit, "target").text = tgt

    tree = ET.ElementTree(xliff)
    ET.indent(tree, space="  ", level=0)  # Pretty print
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"XLIFF file created: {output_file}")

def main():
    # Prompt for directory
    directory = prompt_directory()

    # List and select files
    extensions = {".en", ".fr", ".es", ".de", ".it", ".ru", ".ar", ".jp", ".ko", ".pt", ".nl", ".sv", ".txt"}
    files = list_files_with_extension_check(directory, extensions)
    if not files:
        print(f"No files with extensions {extensions} found in the directory.")
        return

    source_file = prompt_file_selection(files, "source")
    target_file = prompt_file_selection(files, "target")

    # Prompt for language codes
    source_lang = prompt_language("source")
    target_lang = prompt_language("target")

    # Generate XLIFF file
    source_file_path = os.path.join(directory, source_file)
    target_file_path = os.path.join(directory, target_file)
    output_file = os.path.join(
        directory,
        f"{os.path.splitext(source_file)[0]}_{source_lang}_{target_lang}.xliff"
    )

    create_xliff(source_file_path, target_file_path, source_lang, target_lang, output_file)

if __name__ == "__main__":
    main()
