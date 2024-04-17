import csv
import matplotlib.pyplot as plt
import numpy as np

# 读取 CSV 文件中的数据
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.extend(row)  # 将多个数值拆分开并添加到数据列表中
    return data

# 绘制 CSI 数据的图像
def plot_csi_data(data, filename=None):
    x = np.arange(len(data))  # 使用 np.arange() 创建时间点序列
    y = [float(value) for value in data]

    plt.plot(x, y)
    plt.xlabel('Time')
    plt.ylabel('CSI Value')
    if filename:
        plt.title(f'CSI Data: {filename}')
    else:
        plt.title('Original CSI Data')
    plt.show()

# 测试
original_filename = r'E:\dataset\CSI\pic_clap\hb-2-2-4-1-1-c01.csv'  # 替换为原始 CSI 数据的 CSV 文件路径
split_filenames = [r'F:\data\test\pic_clap\hb-2-2-4-1-1-c01-1.csv', r'F:\data\test\pic_clap\hb-2-2-4-1-1-c01-2.csv'
                   , r'F:\data\test\pic_clap\hb-2-2-4-1-1-c01-3.csv', r'F:\data\test\pic_clap\hb-2-2-4-1-1-c01-4.csv']  # 分割后的四份 CSI 数据的文件路径列表

# 绘制原始 CSI 数据图像
original_csi_data = read_csv(original_filename)
plot_csi_data(original_csi_data)

# 绘制分割后的四张 CSI 数据图像
for i, filename in enumerate(split_filenames, start=1):
    split_csi_data = read_csv(filename)
    plot_csi_data(split_csi_data, filename=f'Split CSI Data {i}: {filename}')
