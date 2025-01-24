
import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np

# 模型文件保存路径
model_path = r"E:\Mycode\preprocessing\weight\DPT_Large.pt"

# 加载模型
if not os.path.exists(model_path):
    print("Downloading model weights...")
    model_type = "DPT_Large"  # 高质量深度估计模型
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    # 保存权重
    torch.save(midas.state_dict(), model_path)
else:
    print("Loading model weights from local file...")
    model_type = "DPT_Large"
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    midas.load_state_dict(torch.load(model_path))

# 设置为评估模式
midas.eval()

# 输入文件夹和输出文件夹路径
input_folder = r"E:\Mycode\preprocessing\raw\seq1"  # 替换为实际输入文件夹路径
output_folder = r"E:\Mycode\preprocessing\raw\seq1_processed\depth"  # 替换为实际输出文件夹路径

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 图像预处理
transform = transforms.Compose([transforms.Resize(384), transforms.ToTensor()])

# 遍历文件夹中的每张图片
for i, filename in enumerate(os.listdir(input_folder)):
    if filename.endswith(".png"):  # 只处理 PNG 格式图片
        input_path = os.path.join(input_folder, filename)
        print(f"Processing image: {input_path}")
        
        # 加载并转换输入图像
        input_image = Image.open(input_path).convert("RGB")
        input_tensor = transform(input_image).unsqueeze(0)

        # 预测深度图
        with torch.no_grad():
            depth_map = midas(input_tensor)

        # 将深度图调整为 1920x1080
        depth_map = depth_map.squeeze().cpu().numpy()
        
        # 归一化深度图，并转换为 uint8 类型
        depth_map_normalized = (depth_map - np.min(depth_map)) / (np.max(depth_map) - np.min(depth_map)) * 255
        depth_map_uint8 = depth_map_normalized.astype(np.uint8)
        
        # 调整大小为 1920x1080
        depth_map_resized = Image.fromarray(depth_map_uint8).resize((1920, 1080), Image.LANCZOS)
        
        # 保存深度图
        output_path = os.path.join(output_folder, f"depth_{i + 1}.png")
        depth_map_resized.save(output_path)
        print(f"Depth map saved to: {output_path}")
