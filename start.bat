@echo off
chcp 65001 >nul
title CreatorOS Lite Boot

setlocal enabledelayedexpansion
cls
color 0A

:: --- 显示 LOGO ---
type "D:\CreatorOS_Project\gui\logo.txt"
echo.
echo 🚀 正在加载 CreatorOS Lite，请稍候...
timeout /t 1 >nul

:: --- 检查环境是否初始化过 ---
if not exist "D:\CreatorOS_Project\system_report.txt" (
    echo 🧩 检测到首次运行，启动初始化工具...
    timeout /t 1 >nul
    python "D:\CreatorOS_Project\gui\init_system.py"
)

:: --- 动态加载动画 ---
for /L %%i in (1,1,10) do (
    set dots=
    for /L %%j in (1,1,%%i) do set dots=!dots!.
    cls
    color 0A
    type "D:\CreatorOS_Project\gui\logo.txt"
    echo.
    echo 🔧 正在加载模块!dots!
    timeout /nobreak /t 1 >nul
)

:: --- 启动 GUI ---
echo ✅ 系统加载完成，启动主界面...
timeout /t 1 >nul
if not exist "D:\CreatorOS_Project\system_report.txt" (
    start "" python "D:\CreatorOS_Project\gui\init_gui.py"
) else (
    start "" python "D:\CreatorOS_Project\gui\main.py"
)
exit
