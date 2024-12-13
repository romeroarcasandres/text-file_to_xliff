# text-file_to_xliff
This script converts a pair of text files containing translations into xliff format.

## Overview
The `text-file_to_xliff` script facilitates the conversion of paired source and target text files into an XLIFF file. XLIFF (XML Localization Interchange File Format) is widely used in translation and localization workflows. This tool ensures that the number of lines in the source and target files match, and generates a well-structured XLIFF file in version 1.2 format.

Users can specify the directory containing text files, choose the source and target files, provide language codes, and the script will generate an XLIFF file with translation units. The output xliff file is saved in the same directory as the input files.

See "text-file_to_xliff_1.JPG" and text-file_to_xliff_2.JPG for reference.

## Requirements
- Python 3
- The script uses standard Python libraries (`os`, `xml.etree.ElementTree`), included with the Python installation.

## Files
`TXTtoXLIFF.py`

## Usage
1. Prepare source and target text files where each line corresponds to a translation pair.
2. Run the text-file_to_xliff script.
3. Enter the directory containing the text files when prompted.
4. Select the source and target files from the list displayed by the script.
5. Provide the source and target language codes (e.g., `en` for English, `fr` for French).
6. The script generates an XLIFF file named <source_file>_<source_lang>_<target_lang>.xliff in the same directory as the input files.

## Important Note
- The script ensures that the source and target files have the same number of lines. If the line counts do not match, an error will be displayed.
- By default, the script supports `.txt` and commonly used language-specific extensions (e.g., `.en`, `.fr`). Users can dynamically add new extensions during execution.
- Input text files are read using UTF-8 encoding. To modify the encoding, edit the relevant sections in the script.

## License
This project is governed by the CC BY-NC 4.0 license. For comprehensive details, kindly refer to the LICENSE file included with this project.
