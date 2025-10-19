@echo off
title CreatorOS Lite - 安装初始化工具
chcp 65001 >nul
color 0A

echo.
echo ==========================================================
echo        💽 CreatorOS Lite - 系统初始化工具 v1.0
echo ==========================================================
echo.
echo   本工具将初始化基础目录结构并创建必要文件。
echo   请确保 D: 盘可用且有足够空间。
echo.

pause

REM ==========================================================
REM 1. 创建系统文件夹结构
REM ==========================================================
echo.
echo [1/4] 正在创建文件夹结构...
echo.

set BASE=D:\
set SYS=%BASE%系统工具_System
set CRE=%BASE%创作空间_Creative
set GAM=%BASE%游戏_Games
set DAT=%BASE%资料_Data
set OUT=%BASE%输出_Output
set TMP=%BASE%临时_Temp

REM 系统工具
mkdir "%SYS%\备份_Backup\Installers"
mkdir "%SYS%\隐私工具_Privacy\加密_Encryption"
mkdir "%SYS%\隐私工具_Privacy\清理_Cleaners"
mkdir "%SYS%\隐私工具_Privacy\浏览器_Browsers"
mkdir "%SYS%\搜索_Search"
mkdir "%SYS%\分析_Analyzer"
mkdir "%SYS%\增强_Enhancement"
mkdir "%SYS%\压缩_Archive"

REM 创作空间
mkdir "%CRE%\工具_Tools"
mkdir "%CRE%\项目_Projects"
mkdir "%CRE%\素材库_Assets"
mkdir "%CRE%\世界观_IPUniverse"

REM 游戏
mkdir "%GAM%\工具_Tools"
mkdir "%GAM%\安装_Installed"
mkdir "%GAM%\模组_Mods"
mkdir "%GAM%\存档_Saves"

REM 临时与输出
mkdir "%TMP%\缓存_Cache"
mkdir "%TMP%\下载_Downloads"
mkdir "%OUT%\已发布_Published"

echo ✅ 文件夹结构创建完成。
echo.

REM ==========================================================
REM 2. 创建软件清单文件（如果不存在）
REM ==========================================================
echo [2/4] 检查软件清单文件...
if not exist "%SYS%\备份_Backup\System_Software_List.txt" (
    echo 正在生成 System_Software_List.txt...
    (
        echo ──────────────────────────────
        echo 【CreatorOS Lite 软件清单】
        echo ──────────────────────────────
        echo.
        echo 一、隐私与安全工具
        echo Tor Browser
        echo KeePassXC
        echo VeraCrypt
        echo BleachBit
        echo 7-Zip
        echo Proton VPN / Drive / Pass / Mail
        echo.
        echo 二、系统与辅助工具
        echo Everything
        echo PowerToys
        echo.
        echo 三、创作与开发工具
        echo Obsidian
        echo Notepad++
        echo VSCode
        echo GIMP
        echo Krita
        echo Blender
        echo Audacity
        echo FFmpeg
        echo.
        echo 四、游戏与性能工具
        echo MSI Afterburner
        echo RivaTuner
        echo DXVK
        echo Special K
        echo.
        echo 七、文件管理与归档
        echo TreeSize Free
    ) > "%SYS%\备份_Backup\System_Software_List.txt"
    echo ✅ 软件清单已生成。
) else (
    echo ✅ 已检测到软件清单文件，跳过生成。
)

echo.

REM ==========================================================
REM 3. 检查 GUI 文件是否存在
REM ==========================================================
echo [3/4] 检查 GUI 文件...
if not exist "%BASE%CreatorOS_Project\gui\main.py" (
    echo ⚠️ 未检测到 GUI 程序，请确认 main.py 是否存在。
) else (
    echo ✅ GUI 程序已检测到。
)

echo.

REM ==========================================================
REM 4. 完成提示
REM ==========================================================
echo [4/4] 初始化完成！
echo.
echo 你现在可以执行以下命令启动图形界面：
echo.
echo     python D:\CreatorOS_Project\gui\main.py
echo.
echo 或者手动在资源管理器中双击 main.py。
echo.
pause
exit
