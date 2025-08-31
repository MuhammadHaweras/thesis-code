# This script combines the train and test splits of the PlantDoc dataset into a single directory structure.

import os
import shutil

# Original dataset path
src_root = "PlantDoc-Dataset"
train_src = os.path.join(src_root, "train")
test_src = os.path.join(src_root, "test")

# New combined dataset path
dst_root = "PlantDoc-Combined"
os.makedirs(dst_root, exist_ok=True)

# Function to copy files from one split into combined dataset
def copy_split(src_split):
    for cls in os.listdir(src_split):
        src_cls_dir = os.path.join(src_split, cls)
        if not os.path.isdir(src_cls_dir):
            continue

        dst_cls_dir = os.path.join(dst_root, cls)
        os.makedirs(dst_cls_dir, exist_ok=True)

        for file in os.listdir(src_cls_dir):
            src_file = os.path.join(src_cls_dir, file)
            dst_file = os.path.join(dst_cls_dir, file)

            # Avoid overwriting duplicate names by renaming
            if os.path.exists(dst_file):
                name, ext = os.path.splitext(file)
                i = 1
                while os.path.exists(dst_file):
                    dst_file = os.path.join(dst_cls_dir, f"{name}_{i}{ext}")
                    i += 1

            shutil.copy2(src_file, dst_file)

# Copy both train and test into PlantDoc-Combined
copy_split(train_src)
copy_split(test_src)

print("✅ All files copied into PlantDoc-Combined successfully!")
