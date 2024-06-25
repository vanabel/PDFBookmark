import PyPDF2
import csv
import sys
import os


def add_bookmarks(input_txt_file, input_pdf_file, output_pdf_file=None):
    if not output_pdf_file:
        output_pdf_file = os.path.splitext(input_pdf_file)[
            0] + '_bookmarked.pdf'

    # Read CSV file and prepare bookmarks
    with open(input_txt_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        bookmarks = []
        for row in reader:
            if len(row) != 3:
                print(f"Skipping invalid line: {','.join(row)}")
                continue

            title, level, page_number = row
            bookmarks.append(
                (title.strip(), int(level.strip()), int(page_number.strip())))

    # Add bookmarks to the PDF
    fit = PyPDF2.generic.Fit.fit_horizontally()
    pdf_writer = PyPDF2.PdfWriter()
    # Dictionary to track parent bookmarks at each level
    parent_map = {1: None}

    for title, level, page_num in bookmarks:
        # Get parent bookmark for current level
        parent = parent_map.get(level - 1)

        # Add bookmark with parent specified
        outline_item = pdf_writer.add_outline_item(
            title, page_num, parent=parent, fit=fit)

        # Update parent_map with current outline_item as parent for next level
        parent_map[level] = outline_item

    # Write PDF with bookmarks
    with open(input_pdf_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        with open(output_pdf_file, 'wb') as output_file:
            pdf_writer.write(output_file)

    print(f"PDF bookmarks added successfully. Output file: {output_pdf_file}")


def print_help():
    script_filename = sys.argv[0]
    help_text = f"""
    Usage: python {script_filename} <input_txt_file> <input_pdf_file> [<output_pdf_file>]
    
    Example:
        python {script_filename} input.txt Example_input.pdf Example_output_bookmarked.pdf
    
    Parameters:
        <input_txt_file>     : Path to the input text file containing bookmark information
        <input_pdf_file>     : Path to the input PDF file to which bookmarks will be added
        [<output_pdf_file>] : Optional path to the output PDF file that will be created with bookmarks
                              If not provided, defaults to 'Example_output_bookmarked.pdf'
    """
    print(help_text)


# Main function to parse arguments and call add_bookmarks
if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print_help()
        sys.exit(1)

    input_txt_file = sys.argv[1]
    input_pdf_file = sys.argv[2]
    output_pdf_file = sys.argv[3] if len(sys.argv) == 4 else None

    add_bookmarks(input_txt_file, input_pdf_file, output_pdf_file)
