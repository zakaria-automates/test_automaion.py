from pathlib import Path

# 1. The current folder we are working in right now
current_dir = Path.cwd()

print(" جاري فحص المجلد...")

# 2. We inspect everything placed inside this folder
for item in current_dir.iterdir():
    # If it is a PNG image
    if item.suffix.lower() == ".png":
        # Create a new folder named Images
        images_folder = current_dir / "Images"
        images_folder.mkdir(exist_ok=True)
        
        # Move the image into the new folder
        item.rename(images_folder / item.name)
        print(f" تم تحريك الصورة: {item.name} إلى مجلد Images")

print(" تم الانتهاء من فحص المجلد.")