@echo off
REM PPT Finder Skill - 快速启动脚本
REM 
REM 使用方法:
REM   ppt_finder <命令> [参数]
REM 
REM 命令:
REM   --build                           构建索引
REM   --search <query>                   搜索内容
REM   --extract <filename>文件名> <page>页码      提取单页
REM   --extract-all <query>关键词         提取所有匹配页面
REM   --list                            列出所有内容
REM   --open <filename>文件名 [page]页码  打开 PPT 文件
REM 
REM 示例:
REM   ppt_finder --build
REM   ppt_finder --search AI
REM   ppt_finder --extract ai-agent-tech-insights.pptx 1
REM   ppt_finder --extract-all OpenClaw

echo PPT Finder Skill - PPT 快速定位工具
echo.

C:\Python314\python.exe "%~dp0scripts\ppt_tool.py" %*

if %errorlevel% neq 0 (
    echo.
    echo 执行出错，请检查命令是否正确。
    echo.
    echo 使用 "ppt_finder" 查看帮助信息。
)
