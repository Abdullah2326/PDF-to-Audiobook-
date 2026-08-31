# PDF-to-Audiobook-
A Python-based PDF to audiobook converter using Piper TTS, with automatic text extraction, cleaning, chunking, and WAV generation.

## Features

* Select a PDF using a file picker.
* Extract and clean text from the PDF.
* Automatically split text into manageable chunks.
* Convert text to speech using Piper.
* Save the complete audiobook as a single WAV file.
* Display processing progress and total execution time.

## How It Works

```text
PDF
 ↓
Text Extraction
 ↓
Text Cleaning
 ↓
Text Chunking
 ↓
Piper TTS
 ↓
WAV Audiobook
```

## Requirements

* Python 3.10+
* Piper TTS
* pypdf

Install dependencies:

```bash
pip install piper-tts pypdf
```

## Setup

Download a Piper voice and place the `.onnx` and `.json` files in your project.

Then update the paths in the code:

```python
VOICE = r"path\to\voice.onnx"
```

and:

```python
config_path = r"path\to\voice.onnx.json"
```

## Usage

Run the program:

```bash
python audiobook.py
```

Select a PDF when prompted. The generated audiobook will be saved as:

```text
YourFile audiobook.wav
```

## Configuration

You can change the maximum TTS chunk size:

```python
CHUNK_SIZE = 800
```

## Limitations

This works best with text-based PDFs. Scanned PDFs and complex layouts may require additional text processing.

## Author

**Abdullah Kashif**

Python Developer | AI Developer | Automation Enthusiast
