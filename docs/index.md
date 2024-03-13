# PDF Parse Kit

Welcome to the PDF Parse Kit documentation!

This project provides a set of tools for parsing PDF files to text. It includes a command-line interface (CLI) and a core library.

This project is essentially a wrapper around the [`pdfplumber`](https://github.com/jsvine/pdfplumber) library, which is a Python library for extracting text, images, and metadata from PDF files.

## Features

- Parse PDF files to text
- Save the parsed text to a file
- Print the parsed text to the terminal
- Handle multi-page PDF files

## Getting Started

To get started with the PDF Parse Kit, check out the following sections:

- [CLI](cli/doc.md): Learn how to use the command-line interface.
- [Core](core/doc.md): Learn about the core `PDFParser` class.


## Project Installation

First we need to create a virtual environment for our project. To do that, navigate to the root of the project and run the following command:

```bash
poetry config virtualenvs.in-project true
```

then we need to install the dependencies for the project, to do that run the following command:

```bash
poetry install
```

with this command you will install all the dependencies for the project and create a local virtual environment in the project folder.

## Contributing

We welcome contributions! Please see our [contributing guide](#) for details.

## License

This project is licensed under the MIT License.