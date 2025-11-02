#!/usr/bin/env python3
"""Compress images to reduce file sizes for faster page loading"""

import os
from PIL import Image
import piexif

def get_file_size_mb(filepath):
    """Get file size in MB"""
    size_bytes = os.path.getsize(filepath)
    return size_bytes / (1024 * 1024)

def compress_image(image_path, max_width=1920, quality=85):
    """Compress image while maintaining aspect ratio and EXIF data"""
    try:
        # Get original size
        original_size = get_file_size_mb(image_path)

        # Open image
        img = Image.open(image_path)

        # Preserve EXIF data
        try:
            exif_dict = piexif.load(image_path)
            exif_bytes = piexif.dump(exif_dict)
        except:
            exif_bytes = None

        # Convert RGBA to RGB if needed (for JPEG compatibility)
        if img.mode == 'RGBA':
            # Create a white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])  # Use alpha channel as mask
            img = background

        # Resize if too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Save with compression
        if exif_bytes:
            img.save(image_path, 'JPEG', quality=quality, optimize=True, exif=exif_bytes)
        else:
            img.save(image_path, 'JPEG', quality=quality, optimize=True)

        # Rename to .jpg if it was .png
        if image_path.endswith('.png'):
            new_path = image_path.rsplit('.', 1)[0] + '.jpg'
            os.rename(image_path, new_path)
            image_path = new_path

        # Get new size
        new_size = get_file_size_mb(image_path)
        reduction = ((original_size - new_size) / original_size) * 100

        print(f"Compressed: {os.path.basename(image_path)}")
        print(f"   {original_size:.2f}MB -> {new_size:.2f}MB ({reduction:.1f}% reduction)")

        return image_path

    except Exception as e:
        print(f"Error compressing {image_path}: {e}")
        return None

if __name__ == "__main__":
    images_dir = "images"

    print("Compressing images...\n")

    # Process each PNG file
    for filename in os.listdir(images_dir):
        if filename.lower().endswith('.png'):
            filepath = os.path.join(images_dir, filename)
            compress_image(filepath, max_width=1920, quality=85)

    print("\nCompression complete!")
    print("Note: PNG files have been converted to JPG for better compression.")
