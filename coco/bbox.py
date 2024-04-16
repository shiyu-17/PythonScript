import torch
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from PIL import Image, ImageDraw
import json
import os

# 加载预训练的 Faster R-CNN 模型  000000463730
model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# 图像文件夹路径
image_folder = 'pic'
output_results = []

# 图像转换和标准化
transform = T.Compose([T.ToTensor()])

# 循环处理每张图像
for image_file in os.listdir(image_folder):
    if image_file.endswith(".jpg"):
        image_path = os.path.join(image_folder, image_file)
        original_image = Image.open(image_path)

        # 图像转换和标准化
        input_image = transform(original_image).unsqueeze(0)

        # 模型推理
        with torch.no_grad():
            prediction = model(input_image)

        # 提取边界框信息
        bbox = prediction[0]['boxes'][0].tolist()  # 假设只有一个物体

        # 将边界框表示形式更改为[x, y, w, h]
        x, y, w, h = bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]

        # 输出边界框信息
        category_id = 1  # 假设类别为1
        image_id = os.path.splitext(image_file)[0]
        score = prediction[0]['scores'][0].item()

        result = {"bbox": [x, y, w, h], "category_id": category_id, "image_id": image_id, "score": score}
        output_results.append(result)

        print(image_id)

        # # 在原始图像上绘制边界框
        # draw = ImageDraw.Draw(original_image)
        # draw.rectangle([x, y, x + w, y + h], outline="red", width=3)  # 矩形框，红色，线宽3像素
        #
        # # 保存带有边界框的图像
        # output_image_path = os.path.join('visualizations', f'output_{image_file}')
        # original_image.save(output_image_path)

# 打印生成的结果
print(json.dumps(output_results, indent=4))

output_file = "AP.json"

with open(output_file, "w") as f:
    f.write(json.dumps(output_results, indent=4))

print(f"JSON data saved to {output_file}.")
