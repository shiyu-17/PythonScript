# 根据AP.json文件中的image_id集合，删除val文件夹下不在AP.json文件中的图片，并保存对应关系
import os
import shutil
import json

# 读取ap_val文件的image_id集合
with open('AP_val.json', 'r') as f:
    ap_val_data = json.load(f)
ap_val_image_ids = {item['image_id'] for item in ap_val_data}

# 获取val文件夹下的所有文件名
val_files = os.listdir('val')

# 遍历val文件夹下的文件，删除不在ap_val_image_ids中的图片，并保存对应关系
val_images = {}
for file_name in val_files:
    # 提取文件名中的数字作为image_id
    image_id = int(os.path.splitext(file_name)[0])
    if image_id in ap_val_image_ids:
        val_images[image_id] = file_name
    else:
        # 如果文件不在ap_val_image_ids中，删除文件
        os.remove(os.path.join('val', file_name))

# 将val_images保存为json文件
with open('val_images.json', 'w') as f:
    json.dump(val_images, f, indent=4)
