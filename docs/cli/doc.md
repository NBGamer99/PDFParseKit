# PDF Parse Kit CLI

The PDF Parse Kit CLI is a command-line interface for parsing PDF files to text. It is implemented in the `pdf_parser_cli.py` file.

## Usage

You can use the CLI with the following command:

```sh
python -m pdfparsekit [-h] [-n NEWLINE] -i INPUT [-o OUTPUT] [-v]
```

## Arguments

- `-h`, `--help`: This argument is optional. If provided, the help text will be printed to the terminal.

- `-n`, `--newline`: This argument is optional. It specifies the newline character to use when writing the text to a file. If not provided, the default newline character will be used.

> ⚠️ As stated in the [core](../core/doc.md) documentation, the `newline` argument does not affect the saved files rather the `self.text` attribute which is what gets printed in the terminal

- `-i`, `--input`: This argument is required. It specifies the path to the input PDF file.

- `-o`, `--output`: This argument is optional. It specifies the path to the output folder. If not provided, the output file will have the same name as the input file, but with a `.txt` extension.

- `-v`, `--verbose`: This argument is optional. If provided, the text content will be printed directly to the terminal.

## Example

Here's an example of how to use the CLI:

```sh
python -m pdfparsekit -i example.pdf -o example.txt -v
```

or using `poetry`

```sh
poetry run pdfparsekit -i example.pdf -o example.txt -v
```

In this example, the `example.pdf` file will be parsed to text. The text will be saved in the `example.txt` file and also printed to the terminal.
