#!/usr/bin/env python3
"""
Add GPS geotags to images for Dallas, TX location
This helps with local SEO by embedding location data in images

Usage:
    python add-geotags.py image.jpg
    python add-geotags.py images/*.jpg
"""

import sys
import os
from pathlib import Path

# Dallas, TX coordinates
DALLAS_LAT = 32.7767
DALLAS_LON = -96.7970
DALLAS_CITY = "Dallas"
DALLAS_STATE = "Texas"
DALLAS_COUNTRY = "United States"

def check_piexif():
    """Check if piexif is installed, install if not"""
    try:
        import piexif
        return True
    except ImportError:
        print("📦 Installing required package 'piexif'...")
        import subprocess
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "piexif"])
            print("✅ Successfully installed piexif")
            return True
        except:
            print("❌ Failed to install piexif. Please install manually:")
            print("   pip install piexif")
            return False

def convert_to_degrees(value):
    """Convert decimal degrees to degrees, minutes, seconds tuple"""
    d = int(value)
    m = int((value - d) * 60)
    s = (value - d - m/60) * 3600
    return ((d, 1), (m, 1), (int(s * 100), 100))

def add_geotag(image_path):
    """Add GPS geotag to image"""
    import piexif
    from PIL import Image

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

        print(f"✅ Added geotag to: {image_path}")
        print(f"   Location: {DALLAS_LAT}, {DALLAS_LON} ({DALLAS_CITY}, {DALLAS_STATE})")

    except Exception as e:
        print(f"❌ Error processing {image_path}: {e}")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python add-geotags.py <image1.jpg> [image2.jpg] ...")
        print("\nExample:")
        print("  python add-geotags.py tow-truck.jpg")
        print("  python add-geotags.py images/*.jpg")
        sys.exit(1)

    # Check and install piexif if needed
    if not check_piexif():
        sys.exit(1)

    # Import after ensuring it's installed
    import piexif
    from PIL import Image

    # Process each image
    image_files = sys.argv[1:]

    print(f"\n📍 Adding Dallas, TX geotags to {len(image_files)} image(s)...\n")

    for image_path in image_files:
        if os.path.exists(image_path):
            add_geotag(image_path)
        else:
            print(f"⚠️  File not found: {image_path}")

    print("\n✨ Done! Your images now have Dallas location data embedded.")
    print("   This helps with local SEO and shows you're a local business.")

if __name__ == "__main__":
    main()
