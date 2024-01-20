from PIL import Image

# 读取图像
image_path = "val/2.jpg"
image = Image.open(image_path)

# 获取图像的高度和宽度
height, width = image.size

print("Height:", height)
print("Width:", width)
