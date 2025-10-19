import os
import requests
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# ===================================
# CreatorOS Lite - 自动安装管理器
# ===================================

DOWNLOAD_DIR = r"D:\CreatorOS_Project\downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

SOFTWARES = {
    "Tor Browser": {
        "path": r"D:\系统工具_System\隐私工具_Privacy\浏览器_Browsers\Tor",
        "url": "https://www.torproject.org/dist/torbrowser/14.0.1/torbrowser-install-win64-14.0.1_ALL.exe",
        "installer": "TorBrowser_Setup.exe"
    },
    "KeePassXC": {
        "path": r"D:\系统工具_System\隐私工具_Privacy\加密_Encryption\KeePassXC",
        "url": "https://github.com/keepassxreboot/keepassxc/releases/latest/download/KeePassXC-Win64.exe",
        "installer": "KeePassXC_Setup.exe"
    },
    "VeraCrypt": {
        "path": r"D:\系统工具_System\隐私工具_Privacy\加密_Encryption\VeraCrypt",
        "url": "https://launchpad.net/veracrypt/trunk/latest/+download/VeraCrypt%20Setup%201.26.15.exe",
        "installer": "VeraCrypt_Setup.exe"
    },
    "BleachBit": {
        "path": r"D:\系统工具_System\隐私工具_Privacy\清理_Cleaners\BleachBit",
        "url": "https://download.bleachbit.org/BleachBit-4.6.0-setup.exe",
        "installer": "BleachBit_Setup.exe"
    },
    "7-Zip": {
        "path": r"D:\系统工具_System\压缩_Archive\7-Zip",
        "url": "https://www.7-zip.org/a/7z2408-x64.exe",
        "installer": "7zip_Installer.exe"
    },
    "Everything": {
        "path": r"D:\系统工具_System\搜索_Search\Everything",
        "url": "https://www.voidtools.com/Everything-1.4.1.1024.x64-Setup.exe",
        "installer": "Everything_Setup.exe"
    },
    "PowerToys": {
        "path": r"D:\系统工具_System\增强_Enhancement\PowerToys",
        "url": "https://github.com/microsoft/PowerToys/releases/latest/download/PowerToysUserSetup-x64.exe",
        "installer": "PowerToys_Setup.exe"
    },
    "Obsidian": {
        "path": r"D:\创作空间_Creative\工具_Tools\Obsidian",
        "url": "https://github.com/obsidianmd/obsidian-releases/releases/latest/download/Obsidian.1.6.7.exe",
        "installer": "Obsidian_Setup.exe"
    },
    "Notepad++": {
        "path": r"D:\创作空间_Creative\工具_Tools\Notepad++",
        "url": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/latest/download/npp.8.7.6.Installer.x64.exe",
        "installer": "NotepadPlusPlus_Setup.exe"
    },
    "VSCode": {
        "path": r"D:\创作空间_Creative\工具_Tools\VSCode",
        "url": "https://update.code.visualstudio.com/latest/win32-x64-user/stable",
        "installer": "VSCode_Setup.exe"
    },
    "GIMP": {
        "path": r"D:\创作空间_Creative\工具_Tools\GIMP",
        "url": "https://download.gimp.org/gimp/v2.10/windows/gimp-2.10.38-setup.exe",
        "installer": "GIMP_Setup.exe"
    },
    "Krita": {
        "path": r"D:\创作空间_Creative\工具_Tools\Krita",
        "url": "https://download.kde.org/stable/krita/5.2.2/krita-x64-5.2.2-setup.exe",
        "installer": "Krita_Setup.exe"
    },
    "Blender": {
        "path": r"D:\创作空间_Creative\工具_Tools\Blender",
        "url": "https://mirrors.ocf.berkeley.edu/blender/release/Blender4.1/blender-4.1.0-windows-x64.msi",
        "installer": "Blender_Setup.msi"
    },
    "Audacity": {
        "path": r"D:\创作空间_Creative\工具_Tools\Audacity",
        "url": "https://github.com/audacity/audacity/releases/latest/download/audacity-win-3.5.1-x64.exe",
        "installer": "Audacity_Setup.exe"
    },
}

# -----------------------------------
# 下载逻辑
# -----------------------------------
def download_file(name, url, filename, progress, log):
    file_path = os.path.join(DOWNLOAD_DIR, filename)
    try:
        log.insert(tk.END, f"⏬ 开始下载 {name}...\n")
        log.see(tk.END)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total = int(r.headers.get('content-length', 0))
            with open(file_path, "wb") as f:
                downloaded = 0
                for chunk in r.iter_content(chunk_size=1024*512):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total > 0:
                            percent = int(downloaded / total * 100)
                            progress["value"] = percent
        log.insert(tk.END, f"✅ 下载完成：{name}\n")
        log.see(tk.END)
        return file_path
    except Exception as e:
        log.insert(tk.END, f"❌ 下载失败：{name} - {e}\n")
        log.see(tk.END)
        return None

# -----------------------------------
# 主安装逻辑
# -----------------------------------
def install_all(progress, log, root):
    for i, (name, info) in enumerate(SOFTWARES.items(), start=1):
        progress["value"] = 0
        root.update_idletasks()

        if os.path.exists(info["path"]):
            log.insert(tk.END, f"✅ 已检测到 {name}，跳过安装。\n")
            log.see(tk.END)
            continue

        file_path = download_file(name, info["url"], info["installer"], progress, log)
        if file_path:
            log.insert(tk.END, f"🚀 正在启动安装程序：{info['installer']}\n\n")
            log.see(tk.END)
            try:
                subprocess.Popen(file_path, shell=True)
            except Exception as e:
                log.insert(tk.END, f"⚠️ 无法启动安装程序：{e}\n")
        root.update_idletasks()

    messagebox.showinfo("CreatorOS Lite", "🎉 所有程序检测完成，部分已自动安装！")

# -----------------------------------
# GUI
# -----------------------------------
def main():
    root = tk.Tk()
    root.title("CreatorOS Lite - 自动安装管理器")
    root.geometry("720x480")
    root.configure(bg="#101010")

    title = tk.Label(root, text="CreatorOS Lite 自动安装模块", fg="#00FF88", bg="#101010", font=("Consolas", 18, "bold"))
    title.pack(pady=15)

    desc = tk.Label(root, text="检测 + 自动下载 + 安装 CreatorOS 所需组件", fg="#CCCCCC", bg="#101010", font=("Consolas", 10))
    desc.pack()

    progress = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
    progress.pack(pady=15)

    log = tk.Text(root, width=85, height=20, bg="#181818", fg="#DDDDDD", font=("Consolas", 9))
    log.pack(padx=10, pady=10)

    start_btn = tk.Button(root, text="开始检测与安装", bg="#00AA66", fg="white",
                          font=("Consolas", 12, "bold"),
                          command=lambda: threading.Thread(target=install_all, args=(progress, log, root)).start())
    start_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
