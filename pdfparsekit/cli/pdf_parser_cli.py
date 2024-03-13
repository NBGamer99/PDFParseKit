import argparse
import codecs

from pdfparsekit.core.pdf_parser import PDFParser
from pdfparsekit.utils.colors import Colors
from pdfparsekit.utils.custom_help_formater import CustomHelpFormatter


def cli_parser():
    """
    CLI implementation of the PDFParseKit, parsing pdf using the cli.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        prog="pdfparsekit",
        description=f"{Colors.Fg.blue}Parse PDF to text.{Colors.reset}",
        formatter_class=CustomHelpFormatter,
    )
    parser.add_argument(
        "-n",
        "--newline",
        type=str,
        default="\n",
        help=f"{Colors.Fg.purple}Character to use for newlines{Colors.reset}",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help=f"{Colors.Fg.green}Path to the input PDF file{Colors.reset}",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help=f"{Colors.Fg.yellow}Path to the output text file{Colors.reset}",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help=f"{Colors.Fg.cyan}Print the text content directly to the terminal{Colors.reset}",
    )
    args = parser.parse_args()

    pdf_path = args.input
    newline = codecs.decode(args.newline, "unicode_escape")
    output_path = args.output

    pdf_parser = PDFParser(pdf_path)
    text = pdf_parser.parse_to_text(newline)
    pdf_parser.save(output_path)
    if args.verbose:
        print("\n" + "=" * 40 + " Text content : " + "=" * 40)
        print(text)
        print("=" * 100)
