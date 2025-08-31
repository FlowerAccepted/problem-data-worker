'''
使用方法：
1. 将此脚本保存为 worker.py，放在你的所有题目工作目录下
2. 将文件结构调整为：
.
├── worker.py
├── <题目1目录>
├──├── <程序 IO 名>.py
├──├── <程序 IO 名>（c++编译的可执行文件）
├── <题目2目录>
├── ...
3. cd 至你的题目目录
4. 运行 `../worker.py`，
   输入程序 IO 名（不带扩展名）、测试点名前缀和数据数量
5. 数据将生成在 ./data 目录下，
   文件名格式为 <测试点名前缀><编号>.in 和 <测试点名前缀><编号>.ans
6. 每组数据会调用标准解程序，生成对应的输出文件
7. 生成完成后会打印每组数据的文件路径
8. 确保你的程序 IO 名对应的 Python 脚本能正确生成输入文件，
   并且标准解程序能正确处理输入并生成输出，且确保更新标准解程序
'''
import os
import shutil
import subprocess

def main():
    s = input("请输入程序 IO 名（不带扩展名）: ").strip()
    t = input("请输入测试点名前缀: ").strip()
    n = int(input("请输入数据数量: ").strip())

    data_dir = "./data"
    os.makedirs(data_dir, exist_ok=True)

    for i in range(1, n + 1):
        # 生成数据
        subprocess.run(["python", f"./{s}.py"], check=True)

        # 调用标准解
        subprocess.run([f"./{s}"], check=True)

        # 文件名
        in_src = f"./{s}.in"
        out_src = f"./{s}.out"
        in_dst = os.path.join(data_dir, f"{t}{i}.in")
        ans_dst = os.path.join(data_dir, f"{t}{i}.ans")

        # 移动并重命名
        shutil.move(in_src, in_dst)
        shutil.move(out_src, ans_dst)

        print(f"第{i}组数据生成完成: {in_dst}, {ans_dst}")

if __name__ == "__main__":
    main()