from glob import glob
import random

# 该目录存储图片数据
patch_fn_list = glob('val/*.jpg')
# 返回存储图片名的列表，不包含图片的后缀
patch_fn_list = [fn.split('\\')[-1][:-4] for fn in patch_fn_list]
# 将图片打乱顺序
random.shuffle(patch_fn_list)

# 按照7:3比例划分train和val
train_num = int(0.7 * len(patch_fn_list))
train_patch_list = patch_fn_list[:train_num]
valid_patch_list = patch_fn_list[train_num:]

# produce train/valid/trainval txt file
split = ['train', 'val', 'trainval']

for s in split:
    # 存储文本文件的地址
    save_path = 'E:/Mycode/Pythonscript/Train/' + s + '.txt'

    if s == 'train':
        with open(save_path, 'w') as f:
            print(save_path)
            for fn in train_patch_list:
                # 将训练图像的地址写入train.txt文件
                f.write('%s\n' % fn)
    elif s == 'val':
        with open(save_path, 'w') as f:
            print(save_path)
            for fn in valid_patch_list:
                # 将验证图像的地址写入val.txt文件
                f.write('%s\n' % fn)
    elif s == 'trainval':
        with open(save_path, 'w') as f:
            print(save_path)
            for fn in patch_fn_list:
                # 将所有图像名的编号写入trainval.txt文件
                f.write('%s\n' % fn)
    print('Finish Producing %s txt file to %s' % (s, save_path))