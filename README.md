# 前言

## 开发起因
用于提供给普通用户现成的数据集，压缩后传到b站，配合[VITS-fast-fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning)，实现快速的AI语音模型的合成。

## 功能介绍
基于python3实现将指定文件夹下的所有音频文件合成为一个音频文件，每个音频文件之间有一个固定的静音间隔。

## 开发环境
操作系统：win10  
语言：python3.8.15  
编辑器：VS Code  
依赖库：pydub （pip install pydub）  

## 目录结构
- audio （存储待合成的音频）
  - 1.wav
  - 2.wav
  - child
    - 1.wav
    - 2.wav
- doc （存储说明）
  - demo.png
- config.json （配置文件）
- main.exe （编译打包好的程序）
- main.py （程序源码）
- package.json （打包程序的相关配置）

# 使用

## 1.配置
自行修改为合适的配置即可。
```
{
    // 待合成的音频路径
    "audio_path": "audio",
    // 各个音频之间的间隔（毫秒）
    "duration": 521,
    // 合成后输出的文件路径和文件名
    "out_path": "result.wav"
}
```

## 2.运行
双击`main.exe`即可。

