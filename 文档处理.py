# 作用： 读取Markdown文件，将所有的 `[` 前面添加 `/`，以避免Markdown解析错误
import os

def process_md_file(file_path):
    # 读取Markdown文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 处理每一行内容，将所有的 `[` 前面添加 `/`
    processed_content = []
    in_code_block = False  # 标志位，表示是否处于代码块内部
    for line in content:
        # 判断是否进入或退出代码块
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        
        # 如果处于代码块内部，则跳过处理该行
        if in_code_block:
            processed_content.append(line)
            continue
        
        # 如果包含 ()，说明可能是链接，不处理该行
        if '.html' in line :
            processed_content.append(line)
            continue
        
        # 否则，处理该行
        new_line = line.replace('[', '\[')
        processed_content.append(new_line)

    # 将处理后的内容写回Markdown文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(processed_content)

if __name__ == "__main__":
    # 指定Markdown文件的路径
    md_file_path = r'E:\OneDrive\Mynote\0.CoreFolder\tmp.md'

    # 处理Markdown文件
    process_md_file(md_file_path)
