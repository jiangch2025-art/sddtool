#!/usr/bin/env python3
"""
Screenshot analysis script for FXUI prototype generation.
Usage: python3 analyze_screenshot.py <image_path> [--output <analysis.md>]

Performs pixel-level analysis of a product screenshot to extract:
- Layout boundaries (header, sidebar, content area, bottom bar)
- Color palette (primary, functional, text colors)
- Table structure (columns, row height)
- Menu items and their positions
- Buttons and interactive elements

Output: prints analysis to stdout or saves to specified file.
"""

import sys
import os
from PIL import Image


def analyze_image(image_path, output_path=None):
    img = Image.open(image_path)
    orig_w, orig_h = img.size
    # Scale down for faster processing
    scale = 2  # assuming 2x retina, so /2 gives CSS pixels
    sm = img.resize((orig_w // scale, orig_h // scale))
    w, h = sm.size
    
    lines = []
    lines.append(f"# Screenshot Analysis: {os.path.basename(image_path)}")
    lines.append(f"Original size: {orig_w}x{orig_h}px")
    lines.append(f"Analysis resolution: {w}x{int(h)}px (1:1 CSS pixel scale)")
    lines.append("")

    # ---- 1. Layout Zones (Vertical scan through center) ----
    lines.append("## 1. Layout Zones (Vertical Scan)")
    x_center = w // 2
    prev = None
    zones = []
    for y in range(0, h, 2):
        px = sm.getpixel((x_center, y))
        if prev:
            diff = sum(abs(px[i] - prev[i]) for i in range(3))
            if diff > 30:
                zones.append((y, str(prev), str(px)))
        prev = px
    for y, p1, p2 in zones[:50]:  # limit output
        lines.append(f"  y={y}: {p1} -> {p2}")
    lines.append(f"  ... (total {len(zones)} zone boundaries)")
    lines.append("")

    # ---- 2. Sidebar / Left Column Boundary ----
    lines.append("## 2. Column Boundaries")
    for y in [h // 4, h // 2, 3 * h // 4]:
        prev = None
        for x in range(0, min(w, 500), 2):
            px = sm.getpixel((x, int(y)))
            if prev:
                diff = sum(abs(px[i] - prev[i]) for i in range(3))
                if diff > 50:
                    lines.append(f"  y={int(y)}, x={x}: {prev} -> {px}")
                    break
            prev = px
    lines.append("")

    # ---- 3. Color Palette Extraction ----
    lines.append("## 3. Color Palette")
    # Sample edge colors for page background
    bg_color = sm.getpixel((w-5, h-5))
    lines.append(f"  Page background (bottom-right corner): RGB{bg_color}")
    
    # Detect primary/accent colors (look for orange #ff7d00 related)
    orange_range, blue_range, green_range, red_range = [], [], [], []
    for y in range(0, h, 10):
        for x in range(0, w, 10):
            r, g, b = sm.getpixel((x, y))
            # Orange: R > G ≈ B
            if r > 200 and g < 150 and b < 100:
                orange_range.append((r, g, b))
            # Blue: B > R, G
            if b > 150 and r < 120 and g < 120:
                blue_range.append((r, g, b))
            # Green: G > R, B
            if g > 150 and r < 120 and b < 120:
                green_range.append((r, g, b))
            # Red badge: R >> G, B
            if r > 200 and g < 80 and b < 80:
                red_range.append((r, g, b))
    
    if orange_range:
        avg = tuple(sum(c[i] for c in orange_range) // len(orange_range) for i in range(3))
        lines.append(f"  Orange/primary pixels detected (count: {len(orange_range)}): ~RGB{avg}")
    if blue_range:
        avg = tuple(sum(c[i] for c in blue_range) // len(blue_range) for i in range(3))
        lines.append(f"  Blue/link pixels detected (count: {len(blue_range)}): ~RGB{avg}")
    if green_range:
        avg = tuple(sum(c[i] for c in green_range) // len(green_range) for i in range(3))
        lines.append(f"  Green/success pixels detected (count: {len(green_range)}): ~RGB{avg}")
    if red_range:
        avg = tuple(sum(c[i] for c in red_range) // len(red_range) for i in range(3))
        lines.append(f"  Red/danger pixels detected (count: {len(red_range)}): ~RGB{avg}")
    lines.append("")

    # ---- 4. Table Detection ----
    lines.append("## 4. Table / Grid Detection")
    # Look for horizontal divider lines (table rows)
    row_count = 0
    for y in range(int(h * 0.2), int(h * 0.85), 2):
        row_colors = set()
        for step, x in enumerate(range(100, w - 100, 20)):
            px = sm.getpixel((x, y))
            row_colors.add((px[0] // 20, px[1] // 20, px[2] // 20))
        # A table row typically has white-ish background with few color variations
        if len(row_colors) <= 3:
            row_count += 1
    lines.append(f"  Estimated data rows: ~{row_count // 4} (based on uniform horizontal bands)")
    lines.append("")

    # ---- 5. Header/Toolbar ----
    lines.append("## 5. Header & Toolbar")
    # Look for the header row boundary
    for y in range(0, int(h * 0.15), 2):
        px = sm.getpixel((100, y))
        r, g, b = px
        if r < 50 and g < 50 and b < 50:
            lines.append(f"  First dark text detected at y={y} — likely header/title area")
            break
    lines.append("")

    result = "\n".join(lines)
    if output_path:
        with open(output_path, 'w') as f:
            f.write(result)
        print(f"Analysis saved to: {output_path}")
    else:
        print(result)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_screenshot.py <image_path> [--output <analysis.md>]")
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_path = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]
    
    analyze_image(image_path, output_path)
