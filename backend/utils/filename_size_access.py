import os
from PIL import Image

def get_assets_structure():
    # Define paths
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.dirname(curr_dir)
    assets_dir = os.path.join(backend_dir, 'assets')
    output_file = os.path.join(backend_dir, 'assets_structure.md')

    # Allowed extensions
    image_extensions = {'.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif', '.tiff'}
    audio_extensions = {'.mp3', '.wav', '.ogg', '.flac'}

    markdown_content = ["# Assets Directory Structure\n"]

    if not os.path.exists(assets_dir):
        print(f"Error: Assets directory not found at {assets_dir}")
        return

    for root, dirs, files in os.walk(assets_dir):
        # Calculate depth for indentation
        rel_path = os.path.relpath(root, assets_dir)
        if rel_path == '.':
            level = 0
            # Don't add root folder name to list, just start listing contents or subfolders
        else:
            level = rel_path.count(os.sep) + 1
            folder_name = os.path.basename(root)
            indent = '  ' * (level - 1)
            markdown_content.append(f"{indent}- **/{folder_name}**")

        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            
            indent = '  ' * level
            
            if ext in image_extensions:
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        markdown_content.append(f"{indent}- {file} (Resolution: {width}x{height})")
                except Exception as e:
                    markdown_content.append(f"{indent}- {file} (Error reading resolution)")
            
            elif ext in audio_extensions:
                markdown_content.append(f"{indent}- {file}")

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))
    
    print(f"Markdown file created at: {output_file}")

if __name__ == "__main__":
    get_assets_structure()
