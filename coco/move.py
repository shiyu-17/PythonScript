import os
import shutil

# 源文件夹路径
source_folder = 'E:/Myproject/raw/pic_walk'
# 目标文件夹路径
destination_folder = 'E:/Myproject/raw/walk'

# 创建目标文件夹（如果不存在）
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 遍历源文件夹下的每个文件夹
for folder_name in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, folder_name)
    # 检查路径是否为文件夹
    if os.path.isdir(folder_path):
        # 获取文件夹下的所有文件
        files = os.listdir(folder_path)
        # 遍历文件夹下的每个文件
        for file_name in files:
            # 检查文件名是否为 '20.jpg'
            if file_name == '20.jpg':
                folder_name = os.path.splitext(folder_name)[0]
                # 构造目标文件名
                destination_file_name = folder_name + '.jpg'
                # 源文件路径
                source_file_path = os.path.join(folder_path, file_name)
                # 目标文件路径
                destination_file_path = os.path.join(destination_folder, destination_file_name)
                # 复制文件到目标文件夹
                shutil.copyfile(source_file_path, destination_file_path)