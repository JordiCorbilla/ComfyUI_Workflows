# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:42:22 2024

@author: jordi corbilla
"""

import os
from PIL import Image

def convert_jpg_to_png(directory_path):
    """
    Converts all .jpg files in the specified directory to .png format.

    Args:
        directory_path (str): The path to the directory containing .jpg files.

    Returns:
        None
    """

    if not os.path.isdir(directory_path):
        print(f"The path {directory_path} is not a valid directory.")
        return

    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.jpg'):
            jpg_path = os.path.join(directory_path, filename)
            png_path = os.path.join(directory_path, f"{os.path.splitext(filename)[0]}.png")
            
            try:
                with Image.open(jpg_path) as img:
                    img.save(png_path, 'PNG')
                    print(f"Converted: {jpg_path} to {png_path}")
            except Exception as e:
                print(f"Error converting {jpg_path}: {e}")

convert_jpg_to_png('C:/temp/1_jovanka')