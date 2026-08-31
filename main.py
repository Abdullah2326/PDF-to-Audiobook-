from tkinter.filedialog import askopenfilename
from piper import PiperVoice
from pypdf import PdfReader
from pathlib import Path
import wave
import time
import os
import re


start_time = time.perf_counter()

print("Select a PDF")

PDF_FILE = askopenfilename(title="Select a PDF file",filetypes=[("PDF files", "*.pdf")])

if not PDF_FILE:
    print("No PDF was selected.")
    exit()

file_name = os.path.splitext(os.path.basename(PDF_FILE))[0]
OUTPUT_FILE = file_name + " audiobook.wav"

VOICE = r"D:\\PDF to audio book\\Different voice mods\\en_US-amy-medium.onnx" # you have to add path of the piper voice .onnx file
    

# Maximum approximate characters per TTS chunk
CHUNK_SIZE = 800


# extract text from pdf

def extract_pdf_text(pdf_path):

    print("Reading PDF File...")

    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        print(f"Reading page {page_number}/{len(reader.pages)}")

        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


# clean pdf text

def clean_text(text):

    # remove excessive spaces
    text = re.sub(r"[ \t]+", " ", text)

    # remove excessive blank lines
    text = re.sub(r"\n+", "\n", text)

    # fix words broken by PDF line wrapping
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # replace remaining newlines with spaces
    text = text.replace("\n", " ")

    return text.strip()


# split text into small chuncks

def split_text(text, max_chars=800):

    sentences = re.split(r"(?<=[.!?])\s+", text)

    chunks = []

    current = ""

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        # If adding this sentence doesn't make the chunk too large
        if len(current) + len(sentence) + 1 <= max_chars:

            if current:
                current += " "

            current += sentence

        else:

            if current:
                chunks.append(current)

            # Very long sentence
            if len(sentence) > max_chars:

                words = sentence.split()

                current = ""

                for word in words:

                    if len(current) + len(word) + 1 <= max_chars:

                        if current:
                            current += " "

                        current += word

                    else:

                        if current:
                            chunks.append(current)

                        current = word

            else:

                current = sentence

    if current:
        chunks.append(current)

    return chunks


# Create audiobook

def create_audiobook(text):

    print("Loading Piper...")

    voice = PiperVoice.load(
        VOICE,
        config_path="D:\\PDF to audio book\\Different voice mods\\en_US-amy-medium.onnx.json") # you have to add path of the piper voice .json file
    chunks = split_text(text, CHUNK_SIZE)

    print()
    print(f"Total chunks: {len(chunks)}")
    print()

    # Create WAV file

    with wave.open(OUTPUT_FILE, "wb") as wav_file:

        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(voice.config.sample_rate)

        for i, chunk in enumerate(chunks, start=1):

            print(
                f"Generating audio "
                f"{i}/{len(chunks)} "
                f"({i / len(chunks) * 100:.1f}%)"
            )

            for audio in voice.synthesize(chunk):

                wav_file.writeframes(audio.audio_int16_bytes)

    print()
    print("Audiobook created successfully!")
    print(f"File: {OUTPUT_FILE}")


# MAIN

if __name__ == "__main__":

    if not Path(PDF_FILE).exists():

        print(f"ERROR: PDF not found: {PDF_FILE}")
        exit()

    text = extract_pdf_text(PDF_FILE)

    if not text.strip():

        print("ERROR: No text could be extracted from the PDF.")
        exit()

    text = clean_text(text)

    print()
    print(f"Extracted characters: {len(text):,}")
    print()

    create_audiobook(text)

    end_time = time.perf_counter()

    elapsed = end_time - start_time

    print(f"\nTotal time: {elapsed:.2f} seconds")
    print(f"Total time: {elapsed / 60:.2f} minutes")