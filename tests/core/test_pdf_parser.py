import os

import pytest

from unittest.mock import MagicMock, patch, Mock
from pdfparsekit.core.pdf_parser import PDFParser

TEST_PDF_FILE = './tests/test-files/background-checks.pdf'

@pytest.fixture
def PDF_instance():
    """
    Fixture to return an instance of PDFParser initialized with TEST_PDF_FILE.

    Yields:
        PDFParser: An instance of PDFParser ready for testing.
    """

    return PDFParser(TEST_PDF_FILE)

def test_pdf_parser(PDF_instance):
    """
    Test PDFParser with a valid file.
    """
    text = PDF_instance.parse_to_text()
    assert text != "", "Text should not be empty after parsing"


def test_parse_mock_to_text(PDF_instance):
    with patch("pdfplumber.open", new_callable=MagicMock) as mock_pdfplumber_open:
        mock_pdf = MagicMock()
        mock_pdf.pages = [MagicMock(), MagicMock()]
        mock_pdf.pages[0].extract_text.return_value = "Hello"
        mock_pdf.pages[1].extract_text.return_value = "World"

        mock_pdfplumber_open.return_value.__enter__.return_value = mock_pdf
        result = PDF_instance.parse_to_text()

        assert result == "Hello\nWorld"
        mock_pdfplumber_open.assert_called_once_with(TEST_PDF_FILE)


def test_pdf_parser_success(PDF_instance):
    PDF_instance.save('./tests/test-files')
    output_filename = os.path.splitext(os.path.basename(TEST_PDF_FILE))[0]
    with open(f'./tests/test-files/{output_filename}.txt', 'r', encoding='utf-8') as f:
        saved_text = f.read()
    with open(f'./tests/test-files/{output_filename}-origin.txt', 'r', encoding='utf-8') as f:
        original_text = f.read()
    assert original_text == saved_text, "Saved text should be the same as parsed text"

def test_pdf_parser_with_nonexistent_file():
    """
    Test PDFParser with a nonexistent file.
    """
    pdf_parser = PDFParser('nonexistent.pdf')
    text = pdf_parser.parse_to_text()
    assert text == "", "Text should be empty when parsing a nonexistent file"

def test_pdf_parser_save_without_parsing(PDF_instance, caplog):
    """
    Test save method without parsing a PDF first.
    """

    PDF_instance.save('./tests/test-files')
    assert any(record.levelname == 'WARNING' and "No text to save!" in record.message for record in caplog.records), "Expected warning message not found in log output"