import shutil
import os

def my_move(datadir, trainlistdir, vallistdir, traindir, valdir):
    # 打开train.txt文件
    fopen = open(trainlistdir, 'r')
    # 读取图片名称
    file_names = fopen.readlines()
    for file_name in file_names:
        file_name = file_name.strip('\n')
        # 图片的路径
        traindata = os.path.join(datadir, file_name + '.jpg')
        # 把图片移动至traindir路径下
        # 若想复制可将move改为copy
        shutil.move(traindata, traindir)
    # 同上
    fopen = open(vallistdir, 'r')
    file_names = fopen.readlines()
    for file_name in file_names:
        file_name = file_name.strip('\n')
        valdata = os.path.join(datadir, file_name + '.jpg')
        shutil.move(valdata, valdir)


# 图片存储地址
datadir = r'val'
# 存储训练图片名的txt文件地址
trainlistdir = r'E:/Mycode/Pythonscript/Train/train.txt'
# 存储验证图片名的txt文件地址
vallistdir = r'E:/Mycode/Pythonscript/Train/val.txt'
# coco格式数据集的train2017目录
traindir = r'E:/Mycode/Pythonscript/Train/train2017'
# coco格式数据集的val2017目录
valdir = r'E:/Mycode/Pythonscript/Train/val2017'
my_move(datadir, trainlistdir, vallistdir, traindir, valdir)