#!/usr/bin/env python3
"""Add GPS geotags to images for Dallas, TX location"""

import sys
import os
import piexif
from PIL import Image

# Dallas, TX coordinates
DALLAS_LAT = 32.7767
DALLAS_LON = -96.7970

def convert_to_degrees(value):
    """Convert decimal degrees to degrees, minutes, seconds tuple"""
    d = int(value)
    m = int((value - d) * 60)
    s = (value - d - m/60) * 3600
    return ((d, 1), (m, 1), (int(s * 100), 100))

def add_geotag(image_path):
    """Add GPS geotag to image"""
    try:
        # Load image
        img = Image.open(image_path)

        # Load existing EXIF data or create new
        try:
            exif_dict = piexif.load(image_path)
        except:
            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

        # Prepare GPS data
        lat_deg = convert_to_degrees(abs(DALLAS_LAT))
        lon_deg = convert_to_degrees(abs(DALLAS_LON))

        # GPS IFD tags
        gps_ifd = {
            piexif.GPSIFD.GPSLatitudeRef: 'N' if DALLAS_LAT >= 0 else 'S',
            piexif.GPSIFD.GPSLatitude: lat_deg,
            piexif.GPSIFD.GPSLongitudeRef: 'E' if DALLAS_LON >= 0 else 'W',
            piexif.GPSIFD.GPSLongitude: lon_deg,
        }

        # Add GPS data to EXIF
        exif_dict["GPS"] = gps_ifd

        # Add image description
        exif_dict["0th"][piexif.ImageIFD.ImageDescription] = b"Dallas Towing Service"
        exif_dict["0th"][piexif.ImageIFD.Copyright] = b"(C) 2024 24 Hour Towing Dallas"

        # Convert to bytes
        exif_bytes = piexif.dump(exif_dict)

        # Save image with new EXIF data
        img.save(image_path, exif=exif_bytes, quality=95)

        print(f"Added geotag to: {image_path}")
        print(f"   Location: {DALLAS_LAT}, {DALLAS_LON} (Dallas, Texas)")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

if __name__ == "__main__":
    image_files = sys.argv[1:]

    print(f"\nAdding Dallas, TX geotags to {len(image_files)} image(s)...\n")

    for image_path in image_files:
        if os.path.exists(image_path):
            add_geotag(image_path)
        else:
            print(f"File not found: {image_path}")

    print("\nDone! Images now have Dallas location data embedded.")
