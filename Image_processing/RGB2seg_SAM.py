import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import os
import sys

sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator


def save_anns(anns, output_path):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    
    # Create an RGBA image with a transparent background
    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:, :, 3] = 0  # Set the alpha channel to 0 (fully transparent)
    
    # Apply each mask with a random color
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])  # Random color with transparency
        img[m] = color_mask  # Apply the mask with the color

    # Convert RGBA to RGB (remove alpha channel for saving as a standard image)
    img_rgb = (img[:, :, :3] * 255).astype(np.uint8)
    
    # Save the image
    cv2.imwrite(output_path, img_rgb)  # Save the image using OpenCV


# 加载 SAM 模型和 Mask Generator
sam_checkpoint = r"E:\Mycode\preprocessing\weight\sam_vit_b_01ec64.pth"
model_type = "vit_b"
device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

mask_generator = SamAutomaticMaskGenerator(sam)

# 输入文件夹和输出文件夹
input_folder = r"E:\Mycode\preprocessing\raw\seq3"  # 替换为实际输入文件夹路径
output_folder = r"E:\Mycode\preprocessing\raw\seq3_segmented"  # 替换为实际输出文件夹路径
os.makedirs(output_folder, exist_ok=True)

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

        # 保存分割结果
        save_anns(masks, output_path)
        print(f"Segmentation result saved to: {output_path}")
