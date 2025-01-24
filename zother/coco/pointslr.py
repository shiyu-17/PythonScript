import json
import cv2

# 读取json文件
with open('keypoints_walk.json') as f:
    data = json.load(f)

# 循环处理每个图像的数据
for item in data:
    image_id = item['image_id']
    keypoints = item['keypoints']


    # 读取图像并显示
    image_path = f'walk/{image_id}.jpg'
    image = cv2.imread(image_path)
    cv2.imshow('Image', image)
    cv2.waitKey(1)

    # 等待输入
    valid_input = False
    while not valid_input:
        user_input = input("请输入 'l' 或 'r' 并按下回车键：")
        if user_input == 'o' or user_input == 'p':
            valid_input = True
        else:
            print("无效输入，请重新输入 'l' 或 'r'")

    # 关闭当前显示的图像
    cv2.destroyAllWindows()

    # 根据输入进行处理
    if user_input == 'o':
        # 将第二个和第四个三元组的x、y、v置为零（索引从0开始）
        keypoints[3] = keypoints[4] = keypoints[5] = keypoints[10] = keypoints[11] = keypoints[9] = 0
    elif user_input == 'p':
        # 将第三个和第五个三元组的x、y、v置为零
        keypoints[7] = keypoints[8] = keypoints[6] = keypoints[13] = keypoints[14] = keypoints[12] = 0

    # 更新数据中的keypoints
    item['keypoints'] = keypoints
    item['num_keypoints'] = 15

    # 保存更新后的数据到新的json文件
    with open('keypoints_wak_updated.json', 'w') as f:
        json.dump(data, f)