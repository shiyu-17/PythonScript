import json

# 读取ap_json文件
with open('AP_train.json', 'r') as f:
    ap_data = json.load(f)

# 读取key.json文件
with open('person_keypoints_pic.json', 'r') as f:
    key_data = json.load(f)

# 获取ap_json中存在的image_id集合
ap_image_ids = {item['image_id'] for item in ap_data}

# 过滤key.json中的数据
new_key_data = []
for item in key_data['images']:
    if item['id'] in ap_image_ids:
        print(item['id'])
        new_key_data.append(item)

key_data['images'] = new_key_data

# 过滤key.json中的数据
new_key_ann = []
for item in key_data['annotations']:
    if item['id'] in ap_image_ids:
        new_key_ann.append(item)

# 更新key.json文件
key_data['annotations'] = new_key_ann

# 保存更新后的key.json文件
with open('person_keypoints_train.json', 'w') as f:
    json.dump(key_data, f, indent=4)
