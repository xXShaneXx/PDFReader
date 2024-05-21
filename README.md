# PDF Search & Viewer

PDF Search & Viewer is a Python application that allows you to search for specific text within PDF files in a specified folder and open the pages where the text is found.

## Features

- Search for text within PDF files in a specified folder
- Open the PDF file at the page where the text is found

## Requirements

- Python 3.6+
- PyMuPDF (fitz)
- webbrowser (included with Python standard library)

## Installation

To install the necessary dependencies for this project, navigate to the project directory and run the following command:

```bash
make install
```

## Usage
To use this application, you can run the following command:

```bash
make run folder_path=<folder_path> search_text=<search_text>
```
You can also run it without specifying the folder path. In this case, the application will search for PDFs in the default folder (src/pdfs):

```bash
make run search_text=<search_text>
```
