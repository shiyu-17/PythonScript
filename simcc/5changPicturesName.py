import os
import json

# 读取JSON文件
with open(r'E:\Mycode\PythonScript\new_pic.json', 'r') as file:
    pic_data = json.load(file)

# 构建pose到file_name的映射
pose_to_file_name = {item["pose"]: item["file_name"] for item in pic_data}

# 图片文件所在的文件夹路径
image_folder = 'E:\Mycode\PythonScript'

# 遍历文件夹中的所有文件
for filename in os.listdir(image_folder):
    # 获取文件名和扩展名
    name, ext = os.path.splitext(filename)
    # 如果文件名（去掉扩展名）在pose_to_file_name中
    if name in pose_to_file_name:
        # 获取新的文件名
        new_filename = pose_to_file_name[name] + ext
        # 构建完整的旧文件路径和新文件路径
        old_file_path = os.path.join(image_folder, filename)
        new_file_path = os.path.join(image_folder, new_filename)
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f'Renamed {filename} to {new_filename}')

print("所有文件已重命名")
