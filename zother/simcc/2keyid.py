import json

# 读取JSON文件
with open('E:\Mycode\PythonScript\AP_pickup-pose.json', 'r') as file:
    data = json.load(file)

# 为每个字典中的id按顺序赋值
for index, item in enumerate(data, start=1):
    item['image_id'] = index

# 将结果写回JSON文件
with open('data_modified.json', 'w') as file:
    json.dump(data, file, indent=4)

print("已成功修改JSON文件中的id值")
