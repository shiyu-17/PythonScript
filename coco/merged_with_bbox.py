import json

# 读取"merged.json"文件
with open('merged.json', 'r') as merged_file:
    merged_data = json.load(merged_file)

# 读取"AP.json"文件
with open('AP.json', 'r') as bbox_file:
    bbox_data = json.load(bbox_file)

# 将bbox_data转换为字典，以便根据image_id获取bbox
bbox_dict = {bbox["image_id"]: bbox["bbox"] for bbox in bbox_data}

# 遍历merged_data中的每个条目
for item in merged_data:
    image_id = item['image_id']
    if image_id in bbox_dict:
        # 如果image_id在bbox_dict中存在相应的bbox，则将bbox添加到merged_data的相应条目中
        bbox = bbox_dict[image_id]
        item["bbox"] = bbox

# 将更新后的merged_data保存为新的JSON文件
output_file = 'merged_with_bbox.json'
with open(output_file, 'w') as output_file:
    json.dump(merged_data, output_file)

print(f"合并后的数据已保存到文件: {output_file}")