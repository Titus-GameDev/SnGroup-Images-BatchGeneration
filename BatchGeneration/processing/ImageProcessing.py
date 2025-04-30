# Copyright Titus Thompson, 2025. All Rights Reserved.

from PIL import Image;
import sys;
from pathlib import Path;

def make_background_transparent(directory):
    path = Path(directory)
    files = [f for f in path.iterdir() if f.is_file()]

    for file in files:
        image = Image.open(file.absolute())
        image = image.convert("RGBA")
        data = image.getdata()

        new_data = []
        for item in data:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                new_data.append((0, 0, 0, 0))
            else:
                new_data.append(item)

        out_path = 'out_transparentBG/' + file.name
        image.putdata(new_data)
        image.save(out_path, "PNG")

def crop_to_square(directory):
    path = Path(directory)
    files = [f for f in path.iterdir() if f.is_file()]

    for file in files:
        image = Image.open(file.absolute())
        image = image.convert("RGBA")
        
        width, height = image.size
        left = (width / 2) - (height / 2)
        top = 0
        right = (width / 2) + (height / 2)
        bottom = height

        cropped_image= image.crop((left, top, right, bottom))
        out_path = 'out_cropped/' + file.name
        cropped_image.save(out_path, "PNG")

make_background_transparent('input/')
crop_to_square('out_transparentBG/')