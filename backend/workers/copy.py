import json
import os
import shutil
from pathlib import Path

# Paths
JSON_FILE = "backend/workers/image_gen.json"
PREVIEW_DIR = "backend/static/previews"

def copy_scene_images():
    """
    Reads image_gen.json to get duration for each scene,
    then creates copies of each scene image based on the formula:
    total copies = (2 * duration) - 1
    """
    
    # Read the JSON file
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        scenes = json.load(f)
    
    # Process each scene
    for scene in scenes:
        scene_id = scene.get("scene_id")
        duration = scene.get("duration", 5)  # Default to 5 if not specified
        
        # Calculate total copies needed
        total_copies = (2 * duration) - 1
        
        # Source image path
        source_image = os.path.join(PREVIEW_DIR, f"scene_{scene_id}.png")
        
        # Check if source image exists
        if not os.path.exists(source_image):
            print(f"Warning: Source image not found: {source_image}")
            continue
        
        print(f"Scene {scene_id}: Duration={duration}s, Creating {total_copies} copies...")
        
        # Create copies
        for copy_num in range(1, total_copies + 1):
            dest_image = os.path.join(PREVIEW_DIR, f"scene_{scene_id} ({copy_num}).png")
            shutil.copy2(source_image, dest_image)
            print(f"  Created: scene_{scene_id} ({copy_num}).png")
        
        print(f"Scene {scene_id}: {total_copies} copies created successfully\n")
    
    print("All scene copies created successfully!")

if __name__ == "__main__":
    copy_scene_images()
