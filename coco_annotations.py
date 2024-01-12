import json
import os

# 获取val目录下的所有JSON文件
json_files = [file for file in os.listdir('val') if file.endswith('.json')]

for json_file in json_files:
    # 获取JSON文件的image_id
    image_id = json_file.split('.')[0].lstrip('0')  # 使用文件名的第一部分作为image_id

    # 读取JSON文件
    with open(f'val/{json_file}') as file:
        data = json.load(file)

    # 获取shapes中的points值
    points = []
    for shape in data['shapes']:
        points.extend(shape['points'][0] + [2])

    # 创建包含"image_id"和"keypoints"键及其对应值的字典
    keypoints_dict = {"num_keypoints": 17,
            "iscrowd": 0, 'keypoints': points, 'image_id': image_id,
                      "bbox": [ ],"category_id": 1
}

    # 将字典转换为JSON字符串
    keypoints_json = json.dumps(keypoints_dict)

    print(keypoints_json)