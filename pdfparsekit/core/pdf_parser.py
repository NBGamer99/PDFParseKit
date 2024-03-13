import os

import pdfplumber
from pdfminer.pdfparser import PDFSyntaxError

from pdfparsekit.utils.colors import Colors
from pdfparsekit.utils.logger import Logger

logger = Logger().logger


class PDFParser:
    def __init__(self, pdf_path: str):
        """
        Initializes a PDFParser object.

        Args:
            pdf_path (str): The path to the PDF file.

        Attributes:
            pdf_path (str): The path to the PDF file.
            text (str): The extracted text from the PDF file.
            pages (list): The list of extracted text from each page of the PDF file.
            __logger (logging.Logger): The logger object for logging messages.

        """
        self.pdf_path = pdf_path
        self.text = ""
        self.pages = []

    def parse_to_text(self, newline="\n"):
        """
        Parses the PDF file and returns the extracted text.

        Args:
            newline (str, optional): The newline character to use when joining the extracted text from different pages.
                Defaults to '\n'.

        Returns:
            str: The extracted text from the PDF file.

        Raises:
            FileNotFoundError: If the PDF file is not found.
            PDFSyntaxError: If there is a syntax error in the PDF file.

        """
        # TODO : image extraction

        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                self.pages = [page.extract_text() for page in pdf.pages]
                self.text = newline.join(self.pages)
                logger.info(
                    "%sSuccessfully parsed %s %s %s %s!",
                    Colors.Fg.green,
                    Colors.reset,
                    Colors.bold,
                    self.pdf_path,
                    Colors.reset,
                )
            return self.text
        except (FileNotFoundError, PDFSyntaxError) as e:
            logger.error(
                "%sError: %s %s %s %s",
                Colors.Fg.red,
                Colors.reset,
                Colors.bold,
                str(e),
                Colors.reset,
            )
            return self.text

    def save(self, output_path: str | None = None):
        """
        Saves the parsed text from the PDF to a file.

        Args:
            output_path (str): The path where the output file will be saved.

        """
        if output_path is None:
            output_path = os.path.dirname(self.pdf_path)
        if not self.pages or all(page == "" for page in self.pages):
            logger.warning("%sNo text to save!%s", Colors.Fg.yellow, Colors.reset)
            return

        output_filename = os.path.splitext(os.path.basename(self.pdf_path))[0]
        full_output_path = (
            os.path.join(output_path, output_filename)
            if len(self.pages) > 1
            else output_path
        )

        os.makedirs(full_output_path, exist_ok=True)
        for i, page in enumerate(self.pages, start=1):
            page_filename = (
                f"{output_filename}_page_{i}.txt"
                if len(self.pages) > 1
                else f"{output_filename}.txt"
            )
            with open(
                os.path.join(full_output_path, page_filename), "w", encoding="utf-8"
            ) as f:
                f.write(page)

        logger.info(
            "%sSuccessfully saved to %s %s %s %s!",
            Colors.Fg.green,
            Colors.reset,
            Colors.bold,
            (
                full_output_path
                if len(self.pages) > 1
                else os.path.join(full_output_path, page_filename)
            ),
            Colors.reset,
        )
