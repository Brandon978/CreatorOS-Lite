import os
import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import importlib.util   # ✅ 改这里，导入子模块

REQUIRED_MODULES = [
    "tkinter",
    "os",
    "time",
    "threading",
    "importlib",    # ✅ 注意：这里只写 importlib，不要写 importlib.util
    "subprocess",
    "requests",     # 网络功能
    "psutil",       # 系统状态检测
]



# ===============================
# CreatorOS Lite - 图形初始化界面
# ===============================

CHECK_PATHS = [
    r"D:\系统工具_System\隐私工具_Privacy\清理_Cleaners\BleachBit",
    r"D:\创作空间_Creative\工具_Tools\GIMP",
    r"D:\创作空间_Creative\工具_Tools\Krita",
    r"D:\创作空间_Creative\工具_Tools\Blender",
    r"D:\创作空间_Creative\工具_Tools\Audacity",
    r"D:\游戏_Games\工具_Tools\MSIAfterburner",
]

REPORT_PATH = r"D:\CreatorOS_Project\system_report.txt"

def init_system(progress, log_text, root):
    """执行依赖检测 + 路径检测（多线程避免卡死）"""
    total = len(CHECK_PATHS)
    done = 0
    report_lines = []

    # ---------- 检测依赖 ----------
    log_text.insert(tk.END, "📦 开始检测系统依赖...\n")
    root.update_idletasks()
    all_ok = True
    for module in REQUIRED_MODULES:
        time.sleep(0.2)  # 延时让UI有刷新机会
        spec = importlib.util.find_spec(module)
        if spec is not None:
            log_text.insert(tk.END, f"✅ 模块可用：{module}\n")
        else:
            log_text.insert(tk.END, f"⚠️ 缺少模块：{module}\n")
            all_ok = False
        log_text.see(tk.END)
        root.update_idletasks()
    if all_ok:
        log_text.insert(tk.END, "✨ 依赖检测通过。\n\n")
    else:
        log_text.insert(tk.END, "❌ 部分模块缺失，请检查 Python 环境。\n\n")

    # ---------- 检测路径 ----------
    for path in CHECK_PATHS:
        time.sleep(0.5)
        if os.path.exists(path):
            msg = f"✅ 已检测到：{path}"
        else:
            msg = f"⚠️ 缺失：{path}（已自动创建）"
            os.makedirs(path, exist_ok=True)
        done += 1
        progress["value"] = (done / total) * 100
        log_text.insert(tk.END, msg + "\n")
        log_text.see(tk.END)
        root.update_idletasks()
        report_lines.append(msg)

with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    log_text.insert(tk.END, "\n🌟 初始化完成，系统已准备就绪。\n")
    messagebox.showinfo("初始化完成", f"系统检测完成！报告保存至：\n{REPORT_PATH}")

    # ✅ 添加渐隐过渡动画
    for alpha in range(100, -1, -5):
        root.attributes("-alpha", alpha / 100)
        root.update()
        time.sleep(0.03)

    root.destroy()
    os.system("start python D:\\CreatorOS_Project\\gui\\main.py")

def start_check(progress, log_text, root):
    thread = threading.Thread(target=init_system, args=(progress, log_text, root))
    thread.start()

def main():
    root = tk.Tk()
    root.title("CreatorOS Lite - 初始化引导")
    root.geometry("620x400")
    root.configure(bg="#101010")
    root.resizable(False, False)

    title = tk.Label(root, text="CreatorOS Lite 初始化向导", fg="#00FF88", bg="#101010", font=("Consolas", 18, "bold"))
    title.pack(pady=20)

    desc = tk.Label(root, text="系统正在检查必要组件与目录...", fg="#BBBBBB", bg="#101010", font=("Consolas", 11))
    desc.pack()

    progress = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
    progress.pack(pady=20)

    frame = tk.Frame(root, bg="#101010")
    frame.pack(pady=5)

    log_text = tk.Text(frame, width=70, height=10, bg="#181818", fg="#DDDDDD", font=("Consolas", 10))
    log_text.pack()

    start_btn = tk.Button(root, text="开始检测", bg="#00AA66", fg="white", font=("Consolas", 12, "bold"),
                          command=lambda: start_check(progress, log_text, root))
    start_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
