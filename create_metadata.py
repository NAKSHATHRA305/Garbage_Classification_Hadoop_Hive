import os
import pandas as pd

dataset_path = "standardized_256"

data = []

for category in os.listdir(dataset_path):
    category_path = os.path.join(dataset_path, category)

    if os.path.isdir(category_path):
        for img in os.listdir(category_path):
            img_path = os.path.join(category_path, img)
            size = os.path.getsize(img_path)

            data.append({
                "image_name": img,
                "category": category,
                "file_size": size,
                "path": img_path
            })

df = pd.DataFrame(data)
df.to_csv("garbage_metadata.csv", index=False)

print("Metadata file created!")