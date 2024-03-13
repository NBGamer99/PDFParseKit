# PDFParseKit

PDFParseKit is a python library for parsing PDF files. It is a wrapper around the pdfplumber library. It is designed to be used in python projects to extract text and tables from PDF files.

## Dependencies

You need to have `poetry` installed in your local machine as it's a python dependency manager that helps with managing and organizing dependencies.

for that run the following command in your terminal:

```bash
pip install --user poetry
```

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

> ### 🎉 Congratulations you did it, you are a certified poetry wizard

💡running the command `poetry env list` will show you all the virtual envs you have created, and the one you are currently using

### Documentation

After you have installed the project, you can run the following command to see the documentation for the project:

```bash
mkdocs serve
```

