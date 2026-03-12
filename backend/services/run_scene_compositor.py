import json
import os
from PIL import Image
from .scene_compositor import compose_scene

OUTPUT_DIR = "backend/static/previews"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("backend/workers/image_gen.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)  

for i, scene in enumerate(scenes, start=1):
    img = compose_scene(scene)  
    # Convert to RGB before saving to ensure compatibility
    if img.mode == "RGBA":
        # Create a white background and composite
        rgb_img = Image.new("RGB", img.size, (255, 255, 255))
        rgb_img.paste(img, mask=img.split()[3])  # Use alpha channel as mask
        img = rgb_img
    img.save(f"{OUTPUT_DIR}/scene_{i}.png")
    print(f"Scene {i} generated")

print(" All scenes generated successfully")
