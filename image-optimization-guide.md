# Image Optimization Guide for Dallas Tow Trucks

## Image Requirements for SEO

### File Naming Convention
✅ **Good:** `dallas-tow-truck-service.jpg`
❌ **Bad:** `IMG_1234.jpg`

**Recommended file names:**
- `dallas-emergency-towing.jpg`
- `tow-truck-dallas-downtown.jpg`
- `roadside-assistance-dallas.jpg`
- `flatbed-tow-truck-dallas.jpg`
- `heavy-duty-towing-dallas.jpg`
- `dallas-tow-truck-night.jpg`

### Image Optimization Checklist

- [ ] Resize to appropriate dimensions (max 1920px width for hero, 800px for cards)
- [ ] Compress to reduce file size (use TinyPNG or similar)
- [ ] Convert to WebP format (better compression, modern browsers support)
- [ ] Add descriptive file names with keywords
- [ ] Add geolocation EXIF data (Dallas coordinates)
- [ ] Create alt text for each image

---

## Adding Geolocation to Images

### Dallas, TX Coordinates:
- **Latitude:** 32.7767° N
- **Longitude:** -96.7970° W

### Tools to Add Geotags:

#### Option 1: Online Tool
- **GeoImgr** - https://www.geoimgr.com/
  1. Upload your image
  2. Enter coordinates: 32.7767, -96.7970
  3. Download with embedded GPS data

#### Option 2: ExifTool (Command Line)
Download from: https://exiftool.org/

```bash
# Add GPS coordinates to image
exiftool -GPSLatitude="32.7767" -GPSLatitudeRef="N" -GPSLongitude="96.7970" -GPSLongitudeRef="W" image.jpg

# Add additional location data
exiftool -City="Dallas" -State="Texas" -Country="United States" image.jpg
```

#### Option 3: Smartphone Photos
- Take photos with location services enabled
- Your phone automatically adds GPS data
- Just verify location is Dallas area

---

## Image Specifications

### Hero Section Image
- **Size:** 1920 x 1080px (16:9 ratio)
- **Format:** WebP or JPG
- **File size:** <200KB (compressed)
- **Subject:** Tow truck on Dallas street, downtown skyline, or highway scene

### Service Card Images
- **Size:** 800 x 600px (4:3 ratio)
- **Format:** WebP or JPG
- **File size:** <100KB each
- **Subjects:**
  1. Emergency towing (tow truck with hazard lights)
  2. Roadside assistance (technician helping driver)
  3. Junk car removal (old car being loaded)
  4. Heavy duty towing (large truck/RV being towed)

### Icons/Logos
- **Size:** 512 x 512px (square)
- **Format:** PNG with transparency or SVG
- **File size:** <50KB

---

## Image Compression Tools

### Online (Free):
- **TinyPNG** - https://tinypng.com/ (best for PNG/JPG)
- **Squoosh** - https://squoosh.app/ (Google's tool, supports WebP)
- **Compressor.io** - https://compressor.io/

### Desktop:
- **ImageOptim** (Mac) - https://imageoptim.com/
- **RIOT** (Windows) - https://riot-optimizer.com/

---

## WebP Conversion

WebP provides 25-35% better compression than JPEG.

### Online Converter:
https://cloudconvert.com/jpg-to-webp

### Command Line (if you have it):
```bash
cwebp -q 80 input.jpg -o output.webp
```

### Fallback Support:
Use `<picture>` tag for older browsers:
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Dallas tow truck service">
</picture>
```

---

## Suggested Images for Your Site

### 1. Hero Image (Main Banner)
**File:** `hero-dallas-tow-truck.jpg`
**Alt text:** "24-hour emergency tow truck service in Dallas, TX"
**Scene:** Professional tow truck on Dallas street, preferably with recognizable Dallas landmark

### 2. Emergency Towing
**File:** `emergency-towing-dallas.jpg`
**Alt text:** "Emergency towing service available 24/7 throughout Dallas"
**Scene:** Tow truck with flashing lights assisting a vehicle

### 3. Roadside Assistance
**File:** `roadside-assistance-dallas.jpg`
**Alt text:** "Professional roadside assistance including tire changes and jump starts in Dallas"
**Scene:** Technician helping a stranded motorist

### 4. Junk Car Removal
**File:** `junk-car-removal-dallas.jpg`
**Alt text:** "Fast junk car removal service in Dallas and Fort Worth"
**Scene:** Old vehicle being loaded onto flatbed

### 5. Heavy Duty Towing
**File:** `heavy-duty-towing-dallas.jpg`
**Alt text:** "Heavy duty towing for trucks, RVs, and commercial vehicles in Dallas"
**Scene:** Large tow truck with big rig or RV

### 6. Service Area Map
**File:** `dallas-service-area-map.jpg`
**Alt text:** "Towing service coverage map for Dallas, Fort Worth, and DFW metroplex"
**Scene:** Map showing service area with Dallas highlighted

### 7. Logo
**File:** `dallas-towing-logo.png`
**Alt text:** "24 Hour Towing Dallas logo"

---

## AI Image Generation Prompts

If using DALL-E, Midjourney, or similar:

### Prompt 1 - Hero Image:
```
Professional flatbed tow truck on a Dallas city street during daytime,
modern white and orange tow truck, Dallas downtown skyline visible in
background, clear blue sky, photorealistic, high quality, wide angle shot
```

### Prompt 2 - Emergency Scene:
```
Tow truck with amber flashing lights helping a broken down car on highway
at dusk, Dallas highway scene, professional emergency towing, photorealistic,
dramatic lighting
```

### Prompt 3 - Roadside Assistance:
```
Professional tow truck operator in uniform helping change a tire on the
side of a Dallas road, friendly service, daytime, photorealistic
```

### Prompt 4 - Heavy Duty:
```
Large heavy-duty tow truck towing an RV on Texas highway, professional
commercial towing operation, photorealistic, high quality
```

### Prompt 5 - Night Service:
```
Professional tow truck with lights on during nighttime in Dallas, 24-hour
emergency service, city lights in background, photorealistic
```

---

## Alt Text Best Practices

### Good Alt Text Structure:
`[What it is] + [What it's doing] + [Where/Context] + [Key details]`

**Examples:**

✅ **Good:**
- "Red flatbed tow truck loading a sedan in downtown Dallas during emergency call"
- "Professional tow truck operator providing roadside assistance on Dallas highway"
- "Heavy duty tow truck transporting RV through Fort Worth, Texas"

❌ **Bad:**
- "Tow truck" (too generic)
- "Image1234" (not descriptive)
- "Dallas towing Dallas tow truck Dallas TX towing" (keyword stuffing)

### Include Keywords Naturally:
- Dallas / Fort Worth / DFW
- Towing / tow truck
- Emergency / roadside assistance
- 24-hour / 24/7
- Service type (flatbed, heavy duty, etc.)

---

## Image SEO Metadata

When you have images, add this data:

### EXIF Data:
- **GPS Coordinates:** 32.7767° N, 96.7970° W
- **City:** Dallas
- **State:** Texas
- **Country:** United States
- **Copyright:** © 2024 24 Hour Towing Dallas
- **Description:** Brief description of image

### File Metadata:
- **Title:** Descriptive title with keywords
- **Description:** Full sentence describing image
- **Keywords:** Comma-separated relevant keywords

---

## Where Images Will Go on Your Site

I'll update the HTML to include image placeholders in these locations:

1. **Hero section** - Large banner image
2. **Service cards** - 4 images (one per service)
3. **About section** - Supporting image
4. **Footer** - Small logo
5. **Favicon** - Tiny icon in browser tab

---

## Once You Have Images...

Save them in a folder and let me know. I will:
1. ✅ Create an `/images` folder in your project
2. ✅ Update the HTML with proper `<picture>` tags
3. ✅ Add optimized alt text
4. ✅ Add schema markup for images
5. ✅ Create responsive image sizing
6. ✅ Add lazy loading for performance
7. ✅ Update sitemap to include images

---

## Quick Action Steps

1. **Get 5-7 images** from any source above
2. **Rename them** using the suggested names
3. **Compress them** using TinyPNG
4. **Optionally add geotags** using GeoImgr
5. **Send them to me or save to project folder**
6. **I'll integrate them into your website**

---

## Free Stock Photo Sources (No AI Needed)

### Tow Truck Photos:
- https://unsplash.com/s/photos/tow-truck
- https://www.pexels.com/search/tow%20truck/
- https://pixabay.com/images/search/tow%20truck/

### Dallas Skyline/Streets:
- https://unsplash.com/s/photos/dallas-texas
- https://www.pexels.com/search/dallas/

**Remember:** Stock photos are fine, but real photos of YOUR trucks = best for credibility!

---

Need help with anything else?