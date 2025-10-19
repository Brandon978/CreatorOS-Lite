import os
import tkinter as tk
from tkinter import messagebox
import threading
import subprocess

def safe_open_path(path):
    """安全打开路径"""
    if os.path.exists(path):
        try:
            os.startfile(path)
        except Exception as e:
            messagebox.showerror("错误", f"无法打开路径：\n{path}\n\n原因：{e}")
    else:
        messagebox.showwarning("未找到", f"路径不存在：\n{path}")

def run_system_check():
    """运行系统检测工具"""
    def task():
        try:
            subprocess.run(["python", "init_system.py"], check=True)
            messagebox.showinfo("完成", "系统检测已完成！报告已生成。")
        except Exception as e:
            messagebox.showerror("错误", f"执行系统检测失败：\n{e}")

    threading.Thread(target=task, daemon=True).start()

def create_gui():
    root = tk.Tk()
    root.title("🧰 CreatorOS Lite")
    root.geometry("700x400")
    root.configure(bg="#1e1e1e")

    title = tk.Label(root, text="💽 CreatorOS Lite 控制中心", fg="#00ffcc", bg="#1e1e1e", font=("Consolas", 18, "bold"))
    title.pack(pady=20)

    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(pady=10)

    # 通用按钮样式
    btn_opts = {"width": 20, "height": 2, "bg": "#2d2d2d", "fg": "#00ffcc", "font": ("Consolas", 11, "bold")}

    # 第一行
    tk.Button(frame, text="🧹 清理缓存", **btn_opts, command=lambda: safe_open_path(r"D:\系统工具_System\隐私工具_Privacy\清理_Cleaners\BleachBit")).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(frame, text="🎨 打开 GIMP", **btn_opts, command=lambda: safe_open_path(r"D:\创作空间_Creative\工具_Tools\GIMP")).grid(row=0, column=1, padx=10, pady=10)

    # 第二行
    tk.Button(frame, text="🔊 Audacity", **btn_opts, command=lambda: safe_open_path(r"D:\创作空间_Creative\工具_Tools\Audacity")).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(frame, text="🎮 游戏工具", **btn_opts, command=lambda: safe_open_path(r"D:\游戏_Games\工具_Tools")).grid(row=1, column=1, padx=10, pady=10)

    # 第三行
    tk.Button(frame, text="🧩 系统检测", **btn_opts, command=run_system_check).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(frame, text="⚙️ PowerToys", **btn_opts, command=lambda: safe_open_path(r"D:\系统工具_System\增强_Enhancement\PowerToys")).grid(row=2, column=1, padx=10, pady=10)
    tk.Button(frame, text="📦 自动安装软件", width=20,command=lambda: os.system("python D:\\CreatorOS_Project\\installer.py")).grid(row=3, column=0, padx=5, pady=5)

    # 状态栏
    status = tk.Label(root, text="✅ CreatorOS Lite 已就绪", bg="#1e1e1e", fg="#888", anchor="w", font=("Consolas", 10))
    status.pack(side="bottom", fill="x", pady=5, padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
