import numpy as np
import torch
import cv2
import os
import sys

sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator


def save_anns_with_fixed_colors(anns, output_path, label_colors):
    """
    使用固定的颜色为分割掩码上色并保存为图像文件。
    :param anns: 分割掩码列表
    :param output_path: 输出图像的路径
    :param label_colors: 预定义的标签颜色（Nx3的矩阵，其中N为标签数量）
    """
    if len(anns) == 0:
        return

    # 获取掩码尺寸
    height, width = anns[0]['segmentation'].shape[:2]
    
    # 初始化彩色图像
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # 对掩码按照面积排序（从大到小）
    sorted_anns = sorted(anns, key=lambda x: x['area'], reverse=True)
    
    # 遍历每个掩码并应用对应颜色
    for idx, ann in enumerate(sorted_anns):
        segmentation = ann['segmentation']
        color_idx = idx % len(label_colors)  # 循环分配颜色
        color = label_colors[color_idx]
        img[segmentation] = color  # 将对应的区域填充颜色

    # 保存分割图像
    cv2.imwrite(output_path, img)


# 加载 SAM 模型和 Mask Generator
sam_checkpoint = r"E:\Mycode\preprocessing\weight\sam_vit_b_01ec64.pth"
model_type = "vit_b"
device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

mask_generator = SamAutomaticMaskGenerator(sam)

# 输入文件夹和输出文件夹
input_folder = r"E:\Mycode\preprocessing\raw\seq1"  # 替换为实际输入文件夹路径
output_folder = r"E:\Mycode\preprocessing\raw\seq1_11"  # 替换为实际输出文件夹路径
os.makedirs(output_folder, exist_ok=True)

# 定义标签颜色矩阵
label_colors = np.array([
    [175, 6, 140],
    [65, 54, 217],
    [156, 198, 23],
    [184, 145, 182],
    [211, 80, 208],
    [232, 250, 80],
    [234, 20, 250],
    [99, 242, 104],
    [142, 1, 246],
    [81, 13, 36],
    [112, 105, 191],
], dtype=np.uint8)

# 遍历输入文件夹的所有图片
for i, filename in enumerate(os.listdir(input_folder)):
    if filename.endswith((".png", ".jpg", ".jpeg")):  # 支持 PNG, JPG, JPEG 格式
        input_path = os.path.join(input_folder, filename)
        print(f"Processing image: {input_path}")
        
        # 加载输入图像
        image = cv2.imread(input_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 生成分割掩码
        masks = mask_generator.generate(image)

        # 输出文件路径
        output_path = os.path.join(output_folder, f'segmentation_{i + 1}.png')

        # 保存分割结果，使用固定颜色
        save_anns_with_fixed_colors(masks, output_path, label_colors)
        print(f"Segmentation result saved to: {output_path}")
