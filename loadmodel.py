import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn

# 下载预训练模型
model = fasterrcnn_resnet50_fpn(pretrained=True)
torch.save(model.state_dict(), 'path_to_model.pth')