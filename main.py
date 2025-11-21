#!/usr/bin/env python3
import os
import shutil
from PIL import Image

INPUT_DIR = "input_images"
OUTPUT_DIR = "modositott_kepek"


def ensure_directories():
    #Biztosítja, hogy a szükséges mappák létezzenek
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def list_images():
    #Kilistázza az input mappában lévő képeket
    valid_ext = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    return [
        os.path.join(INPUT_DIR, f)
        for f in os.listdir(INPUT_DIR)
        if f.lower().endswith(valid_ext)
    ]


def save_image(im: Image.Image, original_path: str, suffix: str = "", out_format: str = None):
    #Kép mentése az output mappába
    base = os.path.basename(original_path)
    name, ext = os.path.splitext(base)
    if out_format:
        ext = "." + out_format.lower()
    outname = f"{name}_{suffix}{ext}"
    outpath = os.path.join(OUTPUT_DIR, outname)
    try:
        if out_format:
            im.save(outpath, out_format.upper())
        else:
            im.save(outpath)
        print(f"✅ Mentve: {outpath}")
    except Exception as e:
        print(f"⚠️ Nem sikerült menteni {outpath}: {e}")
