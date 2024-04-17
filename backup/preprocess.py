import csv
import json
import os
import re
import random
import shutil

import cv2
import numpy as np
from tqdm import tqdm
from sklearn.model_selection import train_test_split


def normal_process(data_path, output_path):

    print('Data preprocessing...')

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        os.makedirs(os.path.join(output_path, 'train'))
        os.makedirs(os.path.join(output_path, 'valid'))
        os.makedirs(os.path.join(output_path, 'test_dark'))

    video_data_path = os.path.join(data_path, 'Video')

    # 分出train/valid/test
    for label in tqdm(os.listdir(video_data_path)):
        file_path = os.path.join(video_data_path, label)
        video_files = [name for name in os.listdir(file_path)]

        train_and_valid, test = train_test_split(
            video_files, test_size=0.2, random_state=42)
        train, valid = train_test_split(
            train_and_valid, test_size=0.2, random_state=42)

        # 取少量训练数据
        # train = random.sample(train, int(len(train) * 0.8))
        # train = random.sample(train, 10)
        
        train_dir = os.path.join(output_path, 'train', label)
        valid_dir = os.path.join(output_path, 'valid', label)
        test_dir = os.path.join(output_path, 'test_dark', label)

        if not os.path.exists(train_dir):
            os.makedirs(train_dir)
        if not os.path.exists(valid_dir):
            os.makedirs(valid_dir)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        for file in train:
            process_file(data_path, label, file, train_dir)
        for file in valid:
            process_file(data_path, label, file, valid_dir)
        for file in test:
            process_file(data_path, label, file, test_dir)

    print('Preprocessing finished.')


def cross_domain_process(data_path_1, data_path_2, output_path):

    print('Data preprocessing...')

    # if not os.path.exists(output_path):
    #     os.makedirs(output_path)
    #     os.makedirs(os.path.join(output_path, 'train'))
    #     os.makedirs(os.path.join(output_path, 'valid'))
    #     os.makedirs(os.path.join(output_path, 'test'))

    # # 先处理s1的数据
    # data_path = data_path_1
    # video_data_path = os.path.join(data_path, 'Video')

    # # 分出train/valid
    # for label in os.listdir(video_data_path):
    #     file_path = os.path.join(video_data_path, label)
    #     video_files = [name for name in os.listdir(file_path)]

    #     train, valid = train_test_split(
    #         video_files, test_size=0.2, random_state=42)

    #     train_dir = os.path.join(output_path, 'train', label)
    #     valid_dir = os.path.join(output_path, 'valid', label)

    #     if not os.path.exists(train_dir):
    #         os.makedirs(train_dir)
    #     if not os.path.exists(valid_dir):
    #         os.makedirs(valid_dir)

    #     for file in train:
    #         process_file(data_path, label, file, train_dir)
    #     for file in valid:
    #         process_file(data_path, label, file, valid_dir)

    # 再处理s2的数据
    data_path = data_path_2
    video_data_path = os.path.join(data_path, 'Video')

    # 分出tune/test
    for label in os.listdir(video_data_path):
        file_path = os.path.join(video_data_path, label)

        video_files_1, video_files_2 = [], []
        for name in os.listdir(file_path):
            if re.match('lxx', name):
                video_files_1.append(name)
            elif re.match('tsh', name):
                video_files_2.append(name)

        # 160个样本中40用于tune，80用于test
        tune_1, test_1 = train_test_split(
            video_files_1, test_size=0.5, random_state=42)
        tune_2, test_2 = train_test_split(
            video_files_2, test_size=0.5, random_state=42)
        tune_1 = random.sample(tune_1, 20)
        tune_2 = random.sample(tune_2, 20)
        test = test_1 + test_2
        tune = tune_1 + tune_2

        tune_dir = os.path.join(output_path, 'tune_40', label)
        # test_dir = os.path.join(output_path, 'test_80', label)

        if not os.path.exists(tune_dir):
            os.makedirs(tune_dir)
        # if not os.path.exists(test_dir):
        #     os.makedirs(test_dir)

        for file in tune:
            process_file(data_path, label, file, tune_dir)
        # for file in test:
        #     process_file(data_path, label, file, test_dir)

    print('Preprocessing finished.')


def cross_domain_2_process(data_path_1, data_path_2, data_path_3, output_path):

    print('Data preprocessing...')

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        os.makedirs(os.path.join(output_path, 'train'))
        os.makedirs(os.path.join(output_path, 'valid'))
        os.makedirs(os.path.join(output_path, 'test'))

    # 先处理s1的数据
    data_path = data_path_1
    video_data_path = os.path.join(data_path, 'Video')

    # 分出train/valid
    for label in os.listdir(video_data_path):
        file_path = os.path.join(video_data_path, label)
        video_files = [name for name in os.listdir(file_path)]

        # s1数据取一半
        video_files = random.sample(video_files, len(video_files) // 2)

        train, valid = train_test_split(
            video_files, test_size=0.2, random_state=42)

        train_dir = os.path.join(output_path, 'train', label)
        valid_dir = os.path.join(output_path, 'valid', label)

        if not os.path.exists(train_dir):
            os.makedirs(train_dir)
        if not os.path.exists(valid_dir):
            os.makedirs(valid_dir)

        for file in train:
            process_file(data_path, label, file, train_dir)
        for file in valid:
            process_file(data_path, label, file, valid_dir)

    # 再处理s2的数据
    data_path = data_path_2
    video_data_path = os.path.join(data_path, 'Video')

    # 分出train/valid
    for label in os.listdir(video_data_path):
        file_path = os.path.join(video_data_path, label)
        video_files = [name for name in os.listdir(file_path)]

        # s2数据取一半
        video_files = random.sample(video_files, len(video_files) // 2)

        train, valid = train_test_split(
            video_files, test_size=0.2, random_state=42)

        train_dir = os.path.join(output_path, 'train', label)
        valid_dir = os.path.join(output_path, 'valid', label)

        if not os.path.exists(train_dir):
            os.makedirs(train_dir)
        if not os.path.exists(valid_dir):
            os.makedirs(valid_dir)

        for file in train:
            process_file(data_path, label, file, train_dir)
        for file in valid:
            process_file(data_path, label, file, valid_dir)

    # 最后处理s3的数据
    data_path = data_path_3
    video_data_path = os.path.join(data_path, 'Video')

    # 分出tune/test
    for label in os.listdir(video_data_path):
        file_path = os.path.join(video_data_path, label)
        video_files = [name for name in os.listdir(file_path)]

        # 1/4的s2数据用于test，剩下的数据从中取896个样本用于tune

        tune, test = train_test_split(
            video_files, test_size=0.25, random_state=42)
        tune = random.sample(tune, 32)

        tune_dir = os.path.join(output_path, 'tune', label)
        test_dir = os.path.join(output_path, 'test', label)

        if not os.path.exists(tune_dir):
            os.makedirs(tune_dir)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        for file in tune:
            process_file(data_path, label, file, tune_dir)
        for file in test:
            process_file(data_path, label, file, test_dir)

    print('Preprocessing finished.')


def process_file(data_path, label, video_file, output_dir):

    video_data_path = os.path.join(data_path, 'Video')
    csi_data_path = os.path.join(data_path, 'CSI')
    filename = video_file.split('.')[0]
    csi_file = filename + '.csv'

    video_file = os.path.join(video_data_path, label, video_file)
    csi_file = os.path.join(csi_data_path, label, csi_file)

    # 读取单个csv文件中的所有csi信息
    csi = []
    with open(csi_file, 'r') as csif:
        reader = csv.reader(csif)
        for line in reader:
            line_array = np.array([float(v[:6]) for v in line])           # 取字符串前6位从而去除24.5253.1的情况
            csi.append(line_array[np.newaxis, ...])

    # # shape: (1000+, 90)
    csi = np.concatenate(csi, axis=0)

    # 读取单个avi或MP4文件夹中的所有frame
    frames = []
    capture = [os.path.join(video_file, image)
               for image in sorted(os.listdir(video_file))]

    for image in capture:
        # print(image)
        frame = cv2.imread(image)
        if (frame.shape[0] != crop_size) or (frame.shape[1] != crop_size):
            frame_array = np.array(frame).astype(np.float32)
            frame_array = crop(frame_array, frame.shape[0],
                               frame.shape[1], crop_size)

        frames.append(frame_array[np.newaxis, ...])
        # 处理不定长数据时注释该行代码
        if len(frames) >= 40:
            break

    # shape: (40+, 112, 112, 3)
    frames = np.concatenate(frames, axis=0)

    # 将csi和frames对应
    # csi文件长1000+，样本长400，步长200
    # 视频文件长40+帧，样本长16帧，步长8帧

    f_index = 0
    c_index = 0
    i = 0
    while(f_index + clip_len <= len(frames) and c_index + seq_len <= len(csi)):
        frame_feature = frames[f_index:f_index + clip_len, ...]                # shape: (16, 112, 112, 3)
        frame_feature = frame_feature.transpose((3, 0, 1, 2))                  # shape: (3, 16, 112, 112)
        csi_feature = csi[c_index:c_index + seq_len, ...]                      # shape: (400, 90)

        np.savez_compressed(os.path.join(output_dir, data_path.split('/')[-1] + '_' + filename + '_' + str(i) + '.npz'),
                            frames=frame_feature, csi=csi_feature)

        f_index += 8
        c_index += 200
        i += 1


def crop(frame, height, width, crop_size):

    index = width // 2 - height // 2
    frame = frame[:, index:index + height, :]
    frame = cv2.resize(frame, (crop_size, crop_size))
    # 标准化
    frame -= np.array([[[90.0, 98.0, 102.0]]])

    return frame


def test_split(data_path, output_path, num):
    os.makedirs(output_path)
    srcfile = []
    dstfile = []

    for label in os.listdir(data_path):
        file_names = [name for name in os.listdir(os.path.join(data_path, label))]
        sampled_names = random.sample(file_names, num)

        for name in sampled_names:
            srcfile.append(os.path.join(data_path, label, name))
            dstfile.append(os.path.join(output_path, label, name))
        for i in range(len(srcfile)):
            if not os.path.isfile(srcfile[i]):
                print("%s not exist!"%(srcfile[i]))
            else:
                fpath, fname=os.path.split(dstfile[i])
                if not os.path.exists(fpath):
                    os.makedirs(fpath)
                shutil.copy(srcfile[i],dstfile[i])
                print("copy %s -> %s"%( srcfile[i],dstfile[i]))


def video2image(data_path, output_path):
    print('Data preprocessing...')

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    for label in tqdm(os.listdir(data_path)):
        file_path = os.path.join(data_path, label)
        if not os.path.exists(os.path.join(output_path, label)):
            os.mkdir(os.path.join(output_path, label))

        for file_name in os.listdir(file_path):
            if not os.path.exists(os.path.join(output_path, label, file_name)):
                os.mkdir(os.path.join(output_path, label, file_name))
            
            vc = cv2.VideoCapture(os.path.join(file_path, file_name))
            n = 0
            i = 0                        # 计数
            timeF = 1                    # 视频帧计数间隔频率
            
            if not vc.isOpened():        # 判断是否正常打开
                print(f'Open {label}-{file_name} Failed.')
                return
            
            while True:                  # 循环读取视频帧
                rval, frame = vc.read()
                if rval == False:
                    break
                
                if n % timeF == 0:     # 每隔timeF帧进行存储操作
                    cv2.imwrite(os.path.join(output_path, label, file_name, f'{i:06}.jpg'), frame)  # 存储为图像
                    i += 1
                n = n + 1
                cv2.waitKey(1)
            vc.release()
    
    print('Preprocessing finished.')



if __name__ == "__main__":
    # 配置参数
    with open('config.json', 'r') as file:
        config = json.load(file)

    crop_size = config['crop_size']
    seq_len = config['seq_len']
    clip_len = config['clip_len']
    output_path = config['output_path']

    # 数据处理
    # video2image('dataset/raw/motion_recognition/mp4', 'dataset/raw/motion_recognition/Video')
    normal_process('/data8T/XinxinLu/code/teacher-student/dataset/raw/a504', os.path.join(output_path, 'a504_light_gamma15'))
    # cross_domain_process(s2_data_path, s1_data_path, os.path.join(output_path, 's2-s1'))
    # cross_domain_2_process(env1_data_path, env2_data_path,
    #                        env3_data_path, os.path.join(output_path, 'cross-domain-2'))
    # test_split('dataset/experiment/s2-s1/test_80', 'dataset/experiment/s2-s1/test_60', 240)
