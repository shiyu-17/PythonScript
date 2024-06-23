import json

# 读取AP.json文件
with open('E:\Mycode\PythonScript\AP_pickup.json', 'r') as file:
    ap_data = json.load(file)

# 读取pic.json文件
with open('E:\Mycode\PythonScript\pickup.json', 'r') as file:
    pic_data = json.load(file)

# 构建一个字典，key是pose，value是image_id
ap_pose_dict = {item['pose']: item['image_id'] for item in ap_data}

# 遍历pic.json中的数据并修改image_id
for pic_item in pic_data:
    pose = pic_item['pose']
    if pose in ap_pose_dict:
        pic_item['image_id'] = ap_pose_dict[pose]
        pic_item['id'] = pic_item['image_id']
    else:
        print(f"不存在的pose: {pose}")

# 将修改后的pic数据写回到pic_modified.json文件
with open('pic_modified.json', 'w') as file:
    json.dump(pic_data, file, indent=4)

print("已完成修改并保存到pic_modified.json文件")
