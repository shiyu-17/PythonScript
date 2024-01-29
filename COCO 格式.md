---
url: 
title: COCO 格式 - Rekognition
date: 2024-01-12 21:54:10
tags: 
summary: COCO 数据集由五个信息部分组成，提供了整个数据集的信息。COCO 物体检测数据集的格式记录在 COCO 数据格式 中。
---

创建自定义标签清单，需要使用 COCO 清单文件中的 `images`、`annotations` 和 `categories` 列表。其他两个部分（`info`、`licences`）不是必需的。下面是一个 COCO 清单文件示例。
## 图像列表
`coco_images.py`
COCO 数据集引用的图像列在图像数组中。每个图像对象都包含了有关该图像的信息，例如图像文件名。在以下示例图像对象中，请注意以下信息以及创建 Amazon Rekognition Custom Labels 清单文件需要哪些字段。

*   `id`：（必需）图像的唯一标识符。`id` 字段映射到注释数组（存储边界框信息的地方）中的 `id` 字段。
*   `license`：（非必需）映射到许可证数组。
*   `coco_url`：（可选）图像的位置。
*   `flickr_url`：（非必需）图像在 Flickr 上的位置。
*   `width`：（必需）图像的宽度。
*   `height`：（必需）图像的高度。
*   `file_name`：（必需）图像文件名。在本示例中，`file_name` 与 `id` 匹配，但 COCO 数据集对此不作要求。
*   `date_captured`：（必需）图像拍摄的日期和时间。
```json
{
    "id": 245915,
    "license": 4,
    "coco_url": "http://images.cocodataset.org/val2017/nnnnnnnnnnnn.jpg",
    "flickr_url": "http://farm1.staticflickr.com/88/nnnnnnnnnnnnnnnnnnn.jpg",
    "width": 640,
    "height": 480,
    "file_name": "000000245915.jpg",
    "date_captured": "2013-11-18 02:53:27"
}
```

## 注释（边界框）列表
`coco_annotations.py`
所有图像上的所有物体的边界框信息都存储在注释列表中。单个注释对象包含单个物体的边界框信息以及该物体在图像上的标签。图像上物体的每个实例都有一个注释对象。

在以下示例中，请注意以下信息以及创建 Amazon Rekognition Custom Labels 清单文件需要哪些字段。

* `id`：（非必需）注释的标识符。
* `image_id`：（必需）对应于图像数组中的图像 `id`。
* `category_id`：（必需）用于标识边界框内物体的标签的标识符。它映射到类别数组的 `id` 字段。 
*  `iscrowd`：（非必需）指定图像中是否包含物体群。
*  `segmentation`：（非必需）图像中物体的分段信息Amazon Rekognition Custom Labels 不支持分段。
*  `area`：（非必需）注释的区域。
*  `bbox`：（必需）包含图像中物体的边界框的坐标（以像素为单位）代码在 `bbox.py`中

```json
{
    "id": 1409619,
    "category_id": 1,
    "iscrowd": 0,
    "segmentation": [
        [86.0, 238.8,..........382.74, 241.17]
    ],
    "image_id": 245915,
    "area": 3556.2197000000015,
    "bbox": [86, 65, 220, 334]
}
```

### keypoints
新增 `keypoints`  `（x,y,v）`
	 v为0时表示这个关键点没有标注（这种情况下x=y=v=0）
	 v为1时表示这个关键点标注了但是不可见（被遮挡了）
	 v为2时表示这个关键点标注了同时也可见

`num_keypoints`表示这个目标上被标注的关键点的数量（v > 0 ），比较小的目标上可能就无法标注关键点。
```json
"keypoints": ["nose","left_eye","right_eye","left_ear","right_ear","left_shoulder","right_shoulder","left_elbow","right_elbow","left_wrist","right_wrist","left_hip","right_hip","left_knee","right_knee","left_ankle","right_ankle"]
```
## 类别列表
标签信息存储在类别数组中。
*   `supercategory`：（非必需）标签的父类别。
*   `id`：（必需）标签标识符。`id` 字段映射到 `annotation` 对象中的 `category_id` 字段。在以下示例中，echo dot 的标识符为 2。
*   `name`：（必需）标签名称。

```json
{"supercategory": "person","id": 1,"name": "person"}
```

![[20240112_090159_890.png]]

## bbox
`bbox.py`
![[20240126_080133_302.png]]