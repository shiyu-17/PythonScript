import json
import os

with open('val_AP_H_all.json') as bbox_file:
    bbox_data = json.load(bbox_file)

# 将bbox_data转换为字典，以便根据image_id获取bbox
bbox_dict = {bbox["image_id"]: bbox["bbox"] for bbox in bbox_data}

print(bbox_dict[3259])