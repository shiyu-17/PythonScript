import json

# 读取pic.json文件
with open('E:\Mycode\PythonScript\pic_modified.json', 'r') as file:
    pic_data = json.load(file)

# 构建新的json数据
new_data = []
for item in pic_data:
    new_item = {
        "id": item["id"],
        "pose": item["pose"],
        "height": 640,
        "width": 480,
        "file_name": f"{item['id']:012}.jpg"
    }
    new_data.append(new_item)

# 将新数据写入新的json文件
with open('new_pic.json', 'w') as file:
    json.dump(new_data, file, indent=4)

print("已完成新JSON文件的生成，并保存到new_pic.json文件")
