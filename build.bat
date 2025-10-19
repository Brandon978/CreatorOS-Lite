@echo off
title CreatorOS Lite - Build Script
color 0A

echo 🔧 正在构建 CreatorOS Lite...
echo.

REM 检查 PyInstaller
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚙️ 未检测到 PyInstaller，正在安装...
    pip install pyinstaller
)

echo 🏗️ 开始打包主界面...
pyinstaller --noconfirm --clean --noconsole --onefile gui\main.py --name CreatorOS_Lite_Main

echo 🏗️ 开始打包初始化界面...
pyinstaller --noconfirm --clean --noconsole --onefile gui\init_gui.py --name CreatorOS_Lite_Init

echo ✅ 打包完成！
echo 可执行文件位于 dist\ 文件夹中。
pause
