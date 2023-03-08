# pip install moviepy
# 同样依赖ffmpeg
# 注意：合成可能会出现没有声音的情况，可以重试或者更改参数编码等
from moviepy.editor import *

import sys
import json

# 合成用的音频路径
audio_path = "result.wav"
# 合成用的图片路径数组
img_path_arr = ['1.png']
# 视频帧率
video_fps = 24
# 视频宽
video_width = 1280
# 视频高
video_height = 720
# 视频码率
video_bitrate = "1000k"
# 视频编解码器
video_codec = "libx264"
# 视频输出路径和文件名
out_path = "output.mp4"


# 打开本地文件
with open('config.json', 'r', encoding='utf-8') as f:
    # 通过load方法将文件内容读入到字典中
    data = json.load(f)

try:
    audio_path = data['video']['audio_path']
    img_path_arr = data['video']['img_path_arr']
    video_fps = data['video']['video_fps']
    video_width = data['video']['video_width']
    video_height = data['video']['video_height']
    video_bitrate = data['video']['video_bitrate']
    video_codec = data['video']['video_codec']
    out_path = data['video']['out_path']
    print("[当前配置]\n合成用的音频路径:{}".format(audio_path), flush=True)
    print("视频帧率:{}\n视频宽:{}\n视频高:{}\n视频码率:{}\n视频编解码器:{}\n视频输出路径和文件名:{}".format(video_fps, video_width, 
        video_height, video_bitrate, video_codec, out_path), flush=True)
    f.close()
except Exception as e:
    print(e)
    print("解析config.json出错，请检查配置是否正确")
    sys.exit()

# 读取音频文件
audio = AudioFileClip(audio_path)

# 创建视频
video = ImageSequenceClip(img_path_arr, fps=video_fps)

# 设置视频参数
video = video.resize((video_width, video_height))  # 设置分辨率 
video = video.set_fps(video_fps)  # 设置帧率

# 合成音频和视频
video.audio = audio

# 保存视频文件 视频路径 视频帧数 视频比特率 视频编解码器
# 如果您安装了 ffmpeg，那么您可以使用以下编解码器：
# 'libx264'：H.264 编解码器
# 'libvpx-vp9'：VP9 编解码器
# 'mpeg4'：MPEG-4 编解码器
video.write_videofile(out_path, fps=video_fps, bitrate=video_bitrate, codec=video_codec)

print("合成完毕，运行结束~")
