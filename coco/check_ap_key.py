import json

# 读取ap_json文件
with open('AP_val.json', 'r') as f:
    ap_data = json.load(f)

# 读取key.json文件
with open('person_keypoints_val.json', 'r') as f:
    key_data = json.load(f)

# 获取ap_json中存在的image_id集合
ap_image_ids = {item['image_id'] for item in ap_data}
ann_image_ids = {item['id'] for item in key_data['annotations']}

# 过滤key.json中的数据

for item in ap_image_ids:
    if item not in  ann_image_ids:
        print(item)

for item in ann_image_ids:
    if item not in  ap_image_ids:
        print(item)
        

