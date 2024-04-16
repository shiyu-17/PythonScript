import os
import json

def generate_image_data(folder_path):
    image_files = os.listdir(folder_path)
    image_data = []

    for i, file_name in enumerate(image_files):
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            image_info = {
                "file_name": file_name,
                "height": 640,
                "width": 480,
                "id": int(file_name.split(".")[0])
            }
            image_data.append(image_info)

    return image_data

folder_path = "val"
image_data = generate_image_data(folder_path)

json_data = {
    "images": image_data
}

json_string = json.dumps(json_data, indent=4)
print(json_string)

output_file = "others/person_keypoints_val.json"

with open(output_file, "w") as f:
    f.write(json_string)

print(f"JSON data saved to {output_file}.")