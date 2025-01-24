import json
import os

# 这里读取的是coco/bbox.py 生成的AP.json文件，里面包含了所有图片的bbox信息
with open('AP.json') as bbox_file:
    bbox_data = json.load(bbox_file)

# 将bbox_data转换为字典，以便根据image_id获取bbox
bbox_dict = {bbox["image_id"]: bbox["bbox"] for bbox in bbox_data}

# 获取val目录下的所有JSON文件
json_files = [file for file in os.listdir('standup') if file.endswith('.json')]

# 创建一个列表来存储每个JSON对象
keypoints_list = []

for json_file in json_files:
    # 获取JSON文件的image_id
    image_id = os.path.splitext(json_file)[0]

    # 读取JSON文件
    with open(f'standup/{json_file}') as file:
        data = json.load(file)

    # 获取shapes中的points值
    points = []
    for shape in data['shapes']:
        points.extend(shape['points'][0] + [2])

    bbox = bbox_dict[image_id]
    area = bbox[2] * bbox[3]

    # 将超出bbox范围的坐标点的全部值置为0
    for i in range(0, len(points), 3):
        x, y, v = points[i], points[i + 1], points[i + 2]
        if x < bbox[0] or x > bbox[0] + bbox[2] or y < bbox[1] or y > bbox[1] + bbox[3]:
            points[i:i + 3] = [0, 0, 0]

    num_keypoints = sum(1 for i in range(2, len(points), 3) if points[i] != 0)

    # 创建包含"image_id"和"keypoints"键及其对应值的字典
    keypoints_dict = {'image_id': image_id,
                      "num_keypoints": num_keypoints, 'keypoints': points,
                      "category_id": 1, 'id': image_id, "iscrowd": 0, "area": area, "bbox": bbox
                      }

    keypoints_list.append(keypoints_dict)

# 将列表转换为JSON字符串
keypoints_json = json.dumps(keypoints_list)

# 将JSON字符串写入文件
output_file = "standup.json"
with open(output_file, "w") as f:
    f.write(keypoints_json)