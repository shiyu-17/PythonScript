# 读取原始文件内容
with open("e:/Mycode/preprocessing/Cambridge_pose/seq11.txt", "r") as infile:
    lines = infile.readlines()

# 提取每行的后半部分（去掉文件名）
modified_lines = [line.split(' ', 1)[1] for line in lines]

# 将修改后的内容写入新的文件
with open("seq1.txt", "w") as outfile:
    outfile.writelines(modified_lines)

print("处理完成，结果保存在 output_modified.txt")
