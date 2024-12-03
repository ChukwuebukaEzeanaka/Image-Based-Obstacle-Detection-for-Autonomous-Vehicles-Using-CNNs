import os
import shutil
import random

# Paths to the original images and labels
image_dir = r"C:\Users\mo6ix\OneDrive\Desktop\Fall 2024\Introduction to Digital Eng\Datasets\Images\train"
label_dir = r"C:\Users\mo6ix\OneDrive\Desktop\Fall 2024\Introduction to Digital Eng\Datasets\labels\train"

# Paths to the new validation folders
val_image_dir = r"C:\Users\mo6ix\OneDrive\Desktop\Fall 2024\Introduction to Digital Eng\Datasets\Images\val"
val_label_dir = r"C:\Users\mo6ix\OneDrive\Desktop\Fall 2024\Introduction to Digital Eng\Datasets\labels\val"

# Create validation directories if they don't exist
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Define the validation split ratio (e.g., 20% for validation)
val_split_ratio = 0.2

# List all images in the training image folder
all_images = os.listdir(image_dir)

# Randomly select images for the validation set
val_images = random.sample(all_images, int(len(all_images) * val_split_ratio))

# Move each selected image and its corresponding label to the validation folder
for image_file in val_images:
    # Define the full path for the image and corresponding label
    image_path = os.path.join(image_dir, image_file)
    label_path = os.path.join(label_dir, os.path.splitext(image_file)[0] + ".txt")
    
    # Check if both image and label exist
    if os.path.exists(image_path) and os.path.exists(label_path):
        # Move image to the validation image folder
        shutil.move(image_path, os.path.join(val_image_dir, image_file))
        
        # Move label to the validation label folder
        shutil.move(label_path, os.path.join(val_label_dir, os.path.splitext(image_file)[0] + ".txt"))

print("Validation set created successfully.")

