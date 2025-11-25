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

# Képmódosító műveletek

# Átméretezés
def resize_images(percent=None, width=None, height=None):
    imgs = list_images()
    if not imgs:
        print("❌ Nincs egy kép sem az input mappában.")
        return

    for p in imgs:
        try:
            with Image.open(p) as im:
                orig_w, orig_h = im.size
                if percent is not None:
                    new_w = max(1, int(orig_w * percent))
                    new_h = max(1, int(orig_h * percent))
                else:
                    if height is None:
                        new_w = width
                        new_h = max(1, int(orig_h * (new_w / orig_w)))
                    else:
                        new_w = width
                        new_h = height
                new_im = im.resize((new_w, new_h), Image.LANCZOS)
                save_image(new_im, p, f"{new_w}x{new_h}")
        except Exception as e:
            print(f"Hiba a(z) {p} képnél: {e}")

#Méretbekérés
def input_percent_or_dims():
    while True:
        s = input("Add meg a méretet (50% / 800x600 / 800): ").strip()
        if s.endswith("%"):
            try:
                perc = float(s[:-1]) / 100.0
                return {"percent": perc}
            except:
                print("Érvénytelen százalék.")
                continue
        if "x" in s:
            try:
                w, h = s.lower().split("x")
                return {"w": int(w), "h": int(h)}
            except:
                print("Érvénytelen formátum. Példa: 800x600")
                continue
        try:
            return {"w": int(s), "h": None}
        except:
            print("Érvénytelen érték.")

#Forgatás
def rotate_images(angle: int):
    imgs = list_images()
    if not imgs:
        print("❌ Nincs kép az input mappában.")
        return
    for p in imgs:
        try:
            with Image.open(p) as im:
                rotated = im.rotate(angle, expand=True)
                save_image(rotated, p, f"rot{angle}")
        except Exception as e:
            print(f"Hiba: {e}")

#Kivágás
def crop_images(left, top, right, bottom):
    imgs = list_images()
    if not imgs:
        print("❌ Nincs kép az input mappában.")
        return
    for p in imgs:
        try:
            with Image.open(p) as im:
                w, h = im.size
                left_c = max(0, min(left, w - 1))
                top_c = max(0, min(top, h - 1))
                right_c = max(left_c + 1, min(right, w))
                bottom_c = max(top_c + 1, min(bottom, h))
                cropped = im.crop((left_c, top_c, right_c, bottom_c))
                save_image(cropped, p, f"crop_{left_c}_{top_c}_{right_c}_{bottom_c}")
        except Exception as e:
            print(f"Hiba: {e}")

#Konvertálás
def convert_format(new_ext: str):
    imgs = list_images()
    if not imgs:
        print("❌ Nincs kép az input mappában.")
        return
    for p in imgs:
        try:
            with Image.open(p) as im:
                save_image(im, p, suffix=f"conv_{new_ext}", out_format=new_ext)
        except Exception as e:
            print(f"Hiba: {e}")

#Törlés
def clear_output():
    if not os.path.exists(OUTPUT_DIR):
        print("Output mappa nem létezik.")
        return
    for f in os.listdir(OUTPUT_DIR):
        try:
            os.remove(os.path.join(OUTPUT_DIR, f))
        except Exception as e:
            print(f"Nem sikerült törölni {f}: {e}")
    print("✅ Output mappa törölve.")

# Több művelet egyszerre
def batch_process_images():
    imgs = list_images()
    if not imgs:
        print("❌ Nincs kép az input mappában.")
        return

    do_resize = input("Átméretezés? (i/n): ").lower() == "i"
    do_rotate = input("Forgatás? (i/n): ").lower() == "i"
    do_crop = input("Kivágás? (i/n): ").lower() == "i"
    do_convert = input("Formátum konvertálás? (i/n): ").lower() == "i"

    if do_resize:
        size = input_percent_or_dims()
    if do_rotate:
        angle = int(input("Forgatás szöge: "))
    if do_crop:
        print("Add meg a kivágási értékeket:")
        left = int(input("Bal: "))
        top = int(input("Fent: "))
        right = int(input("Jobb: "))
        bottom = int(input("Lent: "))
    if do_convert:
        target_ext = input("Új formátum (pl: jpg, png): ").strip().lower()

    for p in imgs:
        try:
            with Image.open(p) as im:
                # Átméretezés
                if do_resize:
                    if "percent" in size:
                        new_w = max(1, int(im.width * size["percent"]))
                        new_h = max(1, int(im.height * size["percent"]))
                    else:
                        new_w = size["w"] if size["w"] is not None else im.width
                        new_h = size["h"] if size["h"] is not None else im.height
                    im = im.resize((new_w, new_h), Image.LANCZOS)

                # Forgatás
                if do_rotate:
                    im = im.rotate(angle, expand=True)

                # Kivágás
                if do_crop:
                    w, h = im.size
                    left_c = max(0, min(left, w - 1))
                    top_c = max(0, min(top, h - 1))
                    right_c = max(left_c + 1, min(right, w))
                    bottom_c = max(top_c + 1, min(bottom, h))
                    im = im.crop((left_c, top_c, right_c, bottom_c))

                # Formátum konvertálás
                out_format = target_ext if do_convert else None
                save_image(im, p, suffix="_batch", out_format=out_format)

        except Exception as e:
            print(f"Hiba a {p} képnél: {e}")

# Menü
def print_menu():
    print("\nKépmódosító program")
    print("-------------------")
    print("1. Képek átméretezése")
    print("2. Képek forgatása")
    print("3. Képek kivágása")
    print("4. Képek formátum konvertálása")
    print("5. Több művelet egyszerre (batch)")
    print("6. Output mappa ürítése")
    print("7. Kilépés")

