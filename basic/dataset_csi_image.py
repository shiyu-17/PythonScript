# Function: Preprocess the dataset to extract CSI and images from the original dataset.
import csv
import os
import shutil

import numpy as np
from tqdm import tqdm
from sklearn.model_selection import train_test_split


def normal_process(data_path, output_path):

    print('Data preprocessing...')

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        os.makedirs(os.path.join(output_path, 'train'))
        os.makedirs(os.path.join(output_path, 'test'))

    video_data_path = os.path.join(data_path, 'Video')

    # 分出train/test
    for label in tqdm(os.listdir(video_data_path)): 
        file_path = os.path.join(video_data_path, label)    # E:\dataset\Video\pic_clap
        video_files = [name for name in os.listdir(file_path)] # E:\dataset\Video\pic_clap\hb-2-2-4-1-1-c01.dat

        train, test = train_test_split(
            video_files, test_size=0.3, random_state=42, stratify=[label]*len(video_files))

        train_dir = os.path.join(output_path, 'train', label) # F:\data\train\pic_clap
        test_dir = os.path.join(output_path, 'test', label)

        if not os.path.exists(train_dir):
            os.makedirs(train_dir)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        for file in train:
            process_file(data_path, label, file, train_dir)
        for file in test:
            process_file(data_path, label, file, test_dir)

    print('Preprocessing finished.')

                
def process_file(data_path, label, video_file, output_dir):

    video_data_path = os.path.join(data_path, 'Video') # E:\dataset\Video
    csi_data_path = os.path.join(data_path, 'CSI') # E:\dataset\CSI
    filename = video_file.split('.')[0] # hb-2-2-4-1-1-c01
    csi_file = filename + '.csv'      # hb-2-2-4-1-1-c01.csv

    video_file = os.path.join(video_data_path, label, video_file)   # E:\dataset\Video\pic_clap\hb-2-2-4-1-1-c01.dat
    csi_file = os.path.join(csi_data_path, label, csi_file)     # E:\dataset\CSI\pic_clap\hb-2-2-4-1-1-c01.csv

    output_dir_csi = os.path.join(output_dir, 'csi')

    if not os.path.exists(output_dir_csi):
        os.makedirs(output_dir_csi)

    # 读取单个csv文件中的所有csi信息
    csi = []
    with open(csi_file, 'r') as csif:
        reader = csv.reader(csif)
        for line in reader:
            line_array = np.array([float(v[:6]) for v in line])
            csi.append(line_array[np.newaxis, ...])

    # 将 csi 数据平均裁剪为 4 份
    csi = np.concatenate(csi, axis=0)
    if len(csi) < 1000:
        print(f"Warning: csi length is less than 1000 for {filename}")
    
    csi = csi[:1000]
    csi_split = np.array_split(csi, 4)

    # 保存每一份 CSI 数据为不同的 CSV 文件
    for i, csi_part in enumerate(csi_split, start=1):
        part_filename = f"{filename}-{i}.csv"
        part_output_path = os.path.join(output_dir_csi, part_filename)

        with open(part_output_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in csi_part:
                writer.writerow(row)

    # 读取单个avi或MP4文件夹中的所有frame
    frames = []
    capture = [os.path.join(video_file, image)
               for image in sorted(os.listdir(video_file))]
    
    for image in capture:
        imagename = os.path.basename(image)
        if imagename == "1.jpg" or imagename == "12.jpg" or imagename == "23.jpg" or imagename == "34.jpg":
            new_filename = f"{filename}-{imagename[-5:-4]}.jpg"  # hb-2-2-4-1-1-c01-1.jpg 
            print(new_filename)
            output_path = os.path.join(output_dir, new_filename)
            shutil.copyfile(image, output_path)
            


if __name__ == "__main__":

    normal_process(r'E:\dataset', r'F:\data')

