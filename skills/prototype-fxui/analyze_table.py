#!/usr/bin/env python3
"""Analyze the FXUI table list reference image."""
from PIL import Image
img = Image.open('/home/jiangch/.hermes/skills/fxui-prototype/fxui-table-list-small.png')
w, h = img.size

print(f'Image: {w}x{h}')

print('\n=== VERTICAL SCAN (center column x=720) ===')
prev = None
changes = []
for y in range(0, h, 2):
    px = img.getpixel((720, y))
    if prev:
        diff = abs(px[0]-prev[0]) + abs(px[1]-prev[1]) + abs(px[2]-prev[2])
        if diff > 25:
            changes.append((y, prev, px))
    prev = px
for y, p1, p2 in changes:
    print(f'  y={y}: {p1} -> {p2}')

print('\n=== TABLE HEADER (y=200) ===')
prev = None
for x in range(130, w, 5):
    px = img.getpixel((x, 200))
    if prev and abs(px[0]-prev[0]) + abs(px[1]-prev[1]) + abs(px[2]-prev[2]) > 30:
        print(f'  x={x}: {prev} -> {px}')
    prev = px

print('\n=== SIDEBAR COLUMN BOUNDARIES ===')
# Left edge of content area
prev = None
for y in [100, 200, 400]:
    for x in range(100, 300, 2):
        px = img.getpixel((x, y))
        if prev and abs(px[0]-prev[0]) + abs(px[1]-prev[1]) + abs(px[2]-prev[2]) > 40:
            print(f'  y={y}, x={x}: {prev} -> {px}')
            break
        prev = px

print('\n=== BOTTOM BAR (y=700) ===')
prev = None
for x in range(130, w, 5):
    px = img.getpixel((x, 700))
    if prev and abs(px[0]-prev[0]) + abs(px[1]-prev[1]) + abs(px[2]-prev[2]) > 30:
        print(f'  x={x}: {prev} -> {px}')
    prev = px

print('\n=== SIDEBAR MENU ITEM POSITIONS ===')
# Left sidebar has white background
# Detect dark text positions (where pixels go dark)
for y in range(80, h-50, 3):
    px = img.getpixel((50, y))  # icon area
    r, g, b = px
    if r < 100 and g < 100 and b < 100:
        print(f'  Dark pixel at y={y}: RGB{px}')

print('\n=== RED/BADGE DETECTION ===')
# Find red/badge colored pixels
for y in range(80, h-50, 5):
    for x in range(40, 260, 5):
        px = img.getpixel((x, y))
        r, g, b = px
        if r > 200 and g < 100 and b < 100:
            print(f'  Red pixel at ({x},{y}): RGB{px}')

print('\n=== BLUE/PRIMARY BUTTONS ===')
for y in range(80, h-50, 5):
    for x in range(260, w-5, 5):
        px = img.getpixel((x, y))
        r, g, b = px
        if 50 < r < 100 and 100 < g < 180 and b > 180:
            print(f'  Blue pixel at ({x},{y}): RGB{px}')
