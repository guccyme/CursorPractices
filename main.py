"""
Multilingual Hello World GUI Application
Author: Fay zhang
Created: 2024-03-07
Last Modified: 2024-03-07

A Python/Tkinter GUI application that displays "Hello World" in multiple languages.
Each greeting is shown with unique fonts and colors.

Features:
- Supports five languages: English, Chinese, French, Spanish, and Japanese
- Unique font and color combinations for each language
- MacOS-optimized GUI display

Dependencies:
- Python 3.x
- tkinter (Python standard library)
"""
import os
os.environ['TK_SILENCE_DEPRECATION'] = "1"

import tkinter as tk
from tkinter import font

print("开始创建窗口...")  # 调试信息

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        print("初始化窗口...")  # 调试信息
        self.title("Hello World")
        self.geometry("400x300")
        

        # 定义不同语言的文本、颜色和字体
        greetings = [
            ("Hello, World!", "Arial", "#FF0000"),
            ("你好，世界！", "SimHei", "#00FF00"),
            ("Bonjour, Monde!", "Times New Roman", "#0000FF"),
            ("Hola, Mundo!", "Courier", "#FF00FF"),
            ("こんにちは、世界！", "MS Gothic", "#FFA500")
        ]
        
    
        print("创建标签...")  # 调试信息
        for text, font_name, color in greetings:
            label = tk.Label(
                self, 
                text=text,
                font=(font_name, 14),
                fg=color
            )
            label.pack(pady=10)
        print("标签创建完成...")  # 调试信息


def hello_world():
    print("启动应用...")  # 调试信息
    app = App()
    print("开始主循环...")  # 调试信息
    app.mainloop()
    print("程序结束...")  # 调试信息

if __name__ == "__main__":
    hello_world()
