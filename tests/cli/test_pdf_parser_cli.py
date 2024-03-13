from importlib import import_module

import pytest

from tests.cli_test_helpers.commands import shell


def test_main_module():
    """
    Exercise (most of) the code in the ``__main__`` module.
    """
    import_module("pdfparsekit.__main__")


def test_runas_module():
    """
    Can this package be run as a Python module?
    """
    result = shell("python -m pdfparsekit --help")
    assert result.exit_code == 0

def test_entrypoint():
    """
    Is entrypoint script installed? (setup.py)
    """
    result = shell("pdfparsekit --help")
    assert result.exit_code == 0


def test_pdf_parser_cli():
    """
    Exercise the code in the ``pdf_parser_cli`` module.
    """
    result = shell("pdfparsekit -i ./tests/test-files/background-checks.pdf")
    assert result.exit_code == 0

def test_pdf_parser_cli_output():
    """
    Exercise the code in the ``pdf_parser_cli`` module.
    """
    shell("pdfparsekit -i ./tests/test-files/background-checks.pdf -o ./tests/test-files -v")

    with open('./tests/test-files/background-checks-origin.txt', 'r', encoding='utf-8') as f:
        original_text = f.read()
    with open('./tests/test-files/background-checks.txt', 'r', encoding='utf-8') as f:
        saved_cli_text = f.read()

    assert saved_cli_text == original_text, "Saved text should be the same as parsed text"