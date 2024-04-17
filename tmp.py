import os
from tqdm import tqdm
import shutil

if __name__ == "__main__":
    data_path = 'E:/dataset'
    video_data_path = os.path.join(data_path, 'Video')

    # 分出train/test
    for label in tqdm(os.listdir(video_data_path)):
        file_path = os.path.join(video_data_path, label)  
        video_files = [name for name in os.listdir(file_path)]

        # 遍历.dat文件夹下的所有文件
        for video_file in video_files:
            if video_file.endswith('.jpg'):
                file_num = int(video_file.split('.')[0])  # 获取文件名中的数字部分
                if file_num not in [5, 15, 25, 35]:
                    # 如果文件不是05.jpg、15.jpg、25.jpg、35.jpg，则删除
                    os.remove(os.path.join(file_path, video_file))



    