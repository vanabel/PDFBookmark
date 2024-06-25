# PDF Bookmarker

Python script to add bookmarks to a PDF file based on input from a text file.

## Installation

Ensure you have Python 3.x installed along with the necessary dependencies.

```bash
pip install -r requirements.txt
```
## Usage
Run the script with the following command:
```bash
python bookmark.py bookmarks.txt input.pdf [output.pdf]
```

## Input File Format
The input text file (bookmarks.txt) should be formatted with each line containing:

  * Title of the bookmark
  * Level of the bookmark (integer)
  * Page number where the bookmark should link to (integer)

Example:
```txt
Cover, 1, 1
Preface, 1, 5
Chapter 1, 2, 10
Section 1.1, 3, 15
```

If the title contains comma, use "<title>" instead.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
