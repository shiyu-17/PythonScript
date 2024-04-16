import json

# 读取JSON文件
with open('AP_pic.json', 'r') as f:
    data = json.load(f)

# 初始化训练集、验证集和测试集
train_data = []
val_data = []
test_data = []

# 初始化计数器
counter = 0

# 循环将数据分配给训练集、验证集和测试集
for item in data:
    if counter < 8:
        test_data.append(item)
    elif counter < 16:
        val_data.append(item)
    else:
        train_data.append(item)
    
    # 更新计数器，循环
    counter = (counter + 1) % 40

# 保存训练集、验证集和测试集为JSON文件
with open('AP_train.json', 'w') as f:
    json.dump(train_data, f, indent=4)

with open('AP_val.json', 'w') as f:
    json.dump(val_data, f, indent=4)

with open('AP_test.json', 'w') as f:
    json.dump(test_data, f, indent=4)
