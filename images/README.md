# Images Folder

Place your optimized images in this folder.

## Required Images

### 1. hero-dallas-towing.jpg (Priority: HIGH)
- **Size:** 1920 x 1080px
- **Subject:** Professional tow truck on Dallas street or highway
- **Alt text:** "24-hour emergency tow truck service in Dallas, TX"
- **File size:** <200KB

### 2. emergency-towing.jpg
- **Size:** 800 x 600px
- **Subject:** Tow truck with emergency lights helping vehicle
- **Alt text:** "Emergency towing service available 24/7 throughout Dallas"
- **File size:** <100KB

### 3. roadside-assistance.jpg
- **Size:** 800 x 600px
- **Subject:** Technician helping stranded motorist
- **Alt text:** "Professional roadside assistance including tire changes and jump starts in Dallas"
- **File size:** <100KB

### 4. junk-car-removal.jpg
- **Size:** 800 x 600px
- **Subject:** Old vehicle being loaded onto flatbed
- **Alt text:** "Fast junk car removal service in Dallas and Fort Worth"
- **File size:** <100KB

### 5. heavy-duty-towing.jpg
- **Size:** 800 x 600px
- **Subject:** Large tow truck with RV or commercial vehicle
- **Alt text:** "Heavy duty towing for trucks, RVs, and commercial vehicles in Dallas"
- **File size:** <100KB

### 6. logo.png (Optional but recommended)
- **Size:** 512 x 512px
- **Format:** PNG with transparency
- **Subject:** Your company logo
- **File size:** <50KB

### 7. favicon.ico (Optional)
- **Size:** 32 x 32px or 64 x 64px
- **Format:** ICO or PNG
- **Subject:** Simple icon version of logo

## How to Add Images

### Option 1: Using Free Stock Photos
1. Visit https://unsplash.com or https://pexels.com
2. Search for "tow truck" or "Dallas"
3. Download high-quality images
4. Rename to match the names above
5. Compress using https://tinypng.com
6. Place in this folder

### Option 2: AI Generated (Recommended for Custom Look)
1. Use ChatGPT Plus (DALL-E 3), Midjourney, or Leonardo.ai
2. Use prompts from `image-optimization-guide.md`
3. Download generated images
4. Compress and rename
5. Place in this folder

### Option 3: Your Own Photos (Best for Authenticity!)
1. Take photos of your actual tow trucks
2. Enable location services (auto-adds GPS data)
3. Transfer to computer
4. Resize and compress
5. Place in this folder

## After Adding Images

Run the geotag script:
```bash
python add-geotags.py images/*.jpg
```

This adds Dallas GPS coordinates to all images for better local SEO.

## Current Status
- [ ] hero-dallas-towing.jpg
- [ ] emergency-towing.jpg
- [ ] roadside-assistance.jpg
- [ ] junk-car-removal.jpg
- [ ] heavy-duty-towing.jpg
- [ ] logo.png
- [ ] favicon.ico

Once you add images here, I'll update the HTML to use them!