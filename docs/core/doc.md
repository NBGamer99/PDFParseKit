# PDFParser Class

The `PDFParser` class is the core of the PDF Parse Kit. It is responsible for parsing PDF files to text.

## Initialization

The `PDFParser` class is initialized with the path to the PDF file to parse:

```python
parser = PDFParser("path/to/file.pdf")
```

## Methods

### parse_to_text

The `parse_to_text` method parses the PDF to text:

```python
text = parser.parse_to_text()
```

This method takes an optional `newline` parameter that specifies the character to use for newlines. The default is `'\n'`.

> ⚠️ Please note that the `newline` argument only affects the `self.text` attribute, which contains the entire text of the PDF file as a single string. As the pdf extracted text get parsed in different files.

If the PDF file does not exist, this method will print an error message and return an empty string.

### save

The `save` method saves the parsed text to the specified output file:

```python
parser.save("path/to/")
```

This method takes the path to the output folder as a parameter. The output file will be saved in the output folder with the same name as the input file, and if it have multiple pages, a folder will be created with the same name as the input file in the output folder, and the text for each page will be saved in separate file.

## Example

Here's an example of how to use the `PDFParser` class:

```python
parser = PDFParser("path/to/file.pdf")
text = parser.parse_to_text()
parser.save("path/to/")
```

In this example, the `path/to/file.pdf` file will be parsed to text. The text will be saved in the `path/to/file.txt` file.
