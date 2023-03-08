# -*- coding: utf-8 -*-
# 开发环境：python3.8.15、VS Code、Win10
# 安装第三方库：pip install pydub
# 注意：pydub库，默认使用的ffmpeg或avconv软件，需要安装后配置环境变量
from pydub import AudioSegment

import os, sys
import json

# 音频路径 默认为 项目根目录下的audio
audio_path = "audio"
# 音频之间的间隔时间（毫秒）
duration = 520
# 存储audio文件夹下所有文件路径
files = []
# 输出文件路径和文件名
out_path = "result.wav"


# 打开本地文件
with open('config.json', 'r', encoding='utf-8') as f:
    # 通过load方法将文件内容读入到字典中
    data = json.load(f)

try:
    audio_path = data['audio']['audio_path']
    duration = data['audio']['duration']
    out_path = data['audio']['out_path']
    print("[当前配置]\n音频路径:{}\n音频间隔:{}\n输出路径:{}".format(audio_path, duration, out_path))
    f.close()
except Exception as e:
    print(e)
    print("解析config.json出错，请检查配置是否正确")
    sys.exit()

# 遍历文件夹 获取所有文件路径
for root, dirs, filenames in os.walk(audio_path):
    for filename in filenames:
        filepath = os.path.join(root, filename)
        files.append(filepath)

# print(files)
print("文件总数:{}".format(len(files)))

# 创建一个指定长度的空白音频片段 duration毫秒的间隔
silence = AudioSegment.silent(duration=duration)

# 存储拼接的音频
combined = silence

# 遍历文件路径
for file_path in files:
    # 使用AudioSegment.from_file()函数以及适当的参数加载每个音频文件
    audio = AudioSegment.from_file(file_path)
    # 将每个音频片段以及静音片段进行拼接
    combined = combined + audio + silence

file_ext = os.path.splitext(out_path)[1][1:]
# 将合并后的音频保存到磁盘
combined.export(out_path, format=file_ext)
print("合成完毕，运行结束~")
