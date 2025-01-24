# 将Cambridge数据集中的pose文件，中的散乱的pose，进行排序，使其按照图片名称中的数字排序
# 读取原始文件内容
with open("e:/Mycode/preprocessing/Cambridge_pose/pose.txt", "r") as infile:
    lines = infile.readlines()

# 筛选出以"seq1"开头的行
seq1_lines = [line for line in lines if line.startswith("seq1")]

# 提取出图片名称和对应数据，按图片名称中的数字排序
seq1_lines_sorted = sorted(seq1_lines, key=lambda x: int(x.split('/')[1].split('.')[0][5:]))

# 将排序后的内容写入新的文件
with open("seq11.txt", "w") as outfile:
    outfile.writelines(seq1_lines_sorted)

print("排序完成，结果保存在 output_seq1_sorted.txt")
