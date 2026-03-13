#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PPT Finder Skill 安装脚本
自动配置环境、检查依赖、创建快捷方式
"""
import os
import sys
import json
import shutil
from pathlib import Path

def print_section(title):
    """打印章节标题"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def check_python():
    """检查 Python 环境"""
    print_section("1. 检查 Python 环境")
    
    python_version = sys.version
    print(f"[OK] Python 版本: {python_version}")
    
    if sys.version_info < (3, 7):
        print("[ERROR] Python 版本过低，需要 Python 3.7 或更高版本")
        return False
    
    return True

def check_dependencies():
    """检查和安装依赖"""
    print_section("2. 检查依赖")
    
    required_packages = ['python-pptx']
    
    try:
        # 检查 python-pptx
        import pptx
        print(f"[OK] python-pkt 已安装: pptx.__version__")
        return True
    except ImportError:
        print("[WARNING] python-pptx 未安装")
        print("\n正在安装 python-pptx...")
        
        try:
            os.system(f"{sys.executable} -m pip install python-pptx")
            print("[OK] python-pptx 安装成功")
            return True
        except Exception as e:
            print(f"[ERROR] 安装失败: {e}")
            return False

def check_config():
    """检查配置文件"""
    print_section("3. 检查配置")
    
    skill_dir = Path(__file__).parent
    config_file = skill_dir / "scripts" / "ppt_config.json"
    
    if not config_file.exists():
        print("✗ 配置文件不存在")
        
        # 创建默认配置
        default_config = {
            "ppt_dir": str(Path.home() / "Desktop" / "PPT集合"),
            "index_file": str(Path.home() / "AppData" / "Roaming" / "memu-bot" / "agent-output" / "ppt_index.json"),
            "default_output_dir": str(Path.home() / "AppData" / "Roaming" / "memu-bot" / "agent-output" / "ppt_extracted")
        }
        
        # 确保目录存在
        for key in ['ppt_dir', 'default_output_dir']:
            dir_path = Path(default_config[key])
            if not dir_path.exists():
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"  创建目录: {dir_path}")
        
        # 保存配置
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 创建默认配置文件: {config_file}")
    else:
        print(f"✓ 配置文件存在: {config_file}")
        
        # 显示配置
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
            print(f"\n当前配置:")
            print(f"  PPT 目录: {config.get('ppt_dir', '未设置')}")
            print(f"  索引文件: {config.get('index_file', '未设置')}")
            print(f"  输出目录: {config.get('default_output_dir', '未设置')}")
    
    return True

def create_shortcut():
    """创建桌面快捷方式"""
    print_section("4. 创建桌面快捷方式")
    
    skill_dir = Path(__file__).parent
    desktop = Path.home() / "Desktop"
    
    # 复制批处理文件
    bat_file = skill_dir / "ppt_finder.bat"
    desktop_bat = desktop / "ppt_finder.bat"
    
    if not desktop_bat.exists():
        shutil.copy(bat_file, desktop_bat)
        print(f"✓ 创建桌面快捷方式: {desktop_bat}")
    else:
        print(f"✓ 桌面快捷方式已存在: {desktop_bat}")
    
    return True

def verify_installation():
    """验证安装"""
    print_section("5. 验证安装")
    
    skill_dir = Path(__file__).parent
    
    # 检查必要文件
    required_files = [
        "scripts/ppt_tool.py",
        "scripts/ppt_config.json",
        "requirements.txt",
        "ppt_finder.bat",
        "SKILL.md",
        "README.md"
    ]
    
    all_ok = True
    for file_path in required_files:
        full_path = skill_dir / file_path
        if full_path.exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} 不存在")
            all_ok = False
    
    return all_ok

def main():
    """主函数"""
    print("=" * 70)
    print("  PPT Finder Skill - 安装程序")
    print("=" * 70)
    
    # 1. 检查 Python
    if not check_python():
        print("\n✗ 安装失败: Python 版本不符合要求")
        return 1
    
    # 2. 检查依赖
    if not check_dependencies():
        print("\n✗ 安装失败: 依赖安装失败")
        return 1
    
    # 3. 检查配置
    if not check_config():
        print("\n✗ 安装失败: 配置失败")
        return 1
    
    # 4. 创建快捷方式
    if not create_shortcut():
        print("\n✗ 安装失败: 快捷方式方式创建失败")
        return 1
    
    # 5. 验证安装
    if not verify_installation():
        print("\n✗ 安装失败: 验证失败")
        return 1
    
    # 安装成功
    print_section("安装完成!")
    
    print("\n✓ 所有组件安装成功!")
    print("\n快速开始:")
    print("  1. 打开命令提示符")
    print("  2. 切换到桌面目录: cd %USERPROFILE%\\Desktop")
    print("  3. 构建索引: ppt_finder --build")
    print("  4. 搜索内容: ppt_finder --search AI")
    print("\n或者直接使用桌面快捷方式: ppt_finder.bat")
    
    print("\n详细文档:")
    print("  - SKILL.md: 完整功能文档")
    print("  - README.md: 快速开始指南")
    
    print("\n" + "=" * 70)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
