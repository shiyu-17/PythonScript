import json

# 读取JSON文件
with open('E:\Mycode\PythonScript\pickup.json', 'r') as file:
    data = json.load(file)

# 为每个字典添加pose键，其值为image_id的值
for item in data:
    item['pose'] = item['image_id']

# 将结果写回JSON文件
with open('AP_pickup-pose.json', 'w') as file:
    json.dump(data, file, indent=4)

print("已成功为每个字典添加pose键")
