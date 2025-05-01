# topdf

A simple command-line utility to convert Microsoft Word documents (.docx) to PDF format.

## Description

`topdf` is a lightweight wrapper around the `docx2pdf` Python package that makes converting Word documents to PDF as simple as possible. It automatically handles file extension detection and provides clear success/error messages.

## Installation

1. Clone or download this repository to `C:\Tools\topdf`
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Create a file named `topdf.bat` in `C:\Tools` with the following content:
    ```bat
    @echo off
    python "C:\Tools\topdf\topdf.py" %*
    ```
4. Add `C:\Tools` to your system PATH

## Usage

You can use the utility in two ways:

Run the command:

```
topdf document
```

## Features

-   Automatically appends `.docx` extension if not provided
-   Provides clear success/failure messages
-   Simple, single-command interface

## Requirements

This tool requires:

-   Python 3.6 or higher
-   Windows operating system (for .bat file execution)
