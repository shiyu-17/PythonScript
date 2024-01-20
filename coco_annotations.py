import json
import os

with open('val_AP_H_all.json') as bbox_file:
    bbox_data = json.load(bbox_file)

# 将bbox_data转换为字典，以便根据image_id获取bbox
bbox_dict = {bbox["image_id"]: bbox["bbox"] for bbox in bbox_data}

# 获取val目录下的所有JSON文件
json_files = [file for file in os.listdir('val') if file.endswith('.json')]

# 创建一个列表来存储每个JSON对象
keypoints_list = []

for json_file in json_files:
    # 获取JSON文件的image_id
    image_id = int(json_file.split('.')[0].lstrip('0'))  # 使用文件名的第一部分作为image_id

    # 读取JSON文件
    with open(f'val/{json_file}') as file:
        data = json.load(file)

    # 获取shapes中的points值
    points = []
    for shape in data['shapes']:
        points.extend(shape['points'][0] + [2])

    bbox = bbox_dict[image_id]
    area = bbox[2] * bbox[3]

    # 创建包含"image_id"和"keypoints"键及其对应值的字典
    keypoints_dict = {'image_id': image_id,
                      "area": area, "bbox": bbox,
                      "num_keypoints": 17, 'keypoints': points,
                      "category_id": 1, 'id': image_id, "iscrowd": 0
                      }

    keypoints_list.append(keypoints_dict)

# 将列表转换为JSON字符串
keypoints_json = json.dumps(keypoints_list)

# 将JSON字符串写入文件
output_file = "person_keypoints_val.json"
with open(output_file, "w") as f:
    f.write(keypoints_json)