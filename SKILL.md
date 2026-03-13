---
name: ppt-finder
description: PPT 快速定位、搜索和完整内容提取工具。通过纯文本索引快速搜索 PPT 内容，支持提取单页或批量提取匹配页面，毫秒级响应。
metadata:
  author: memu-bot
  version: "1.0.0"
  license: MIT
  tags:
    - ppt
    - document-search
    - content-extraction
    - productivity
    - windows
---

# PPT Finder Skill

## 描述

PPT 快速定位、搜索和完整内容提取页面工具。不使用向量库，通过纯文本索引快速搜索 PPT 内容，支持提取单页或批量提取匹配页面。

---

## 使用场景

当用户请求：
- "搜索 PPT 内容"
- "查找 PPT 中的关键词"
- "提取 PPT 页面内容"
- "批量提取 PPT"
- "打开 PPT 文件"

---

## 核心功能

### 1. 快速搜索
- 毫秒级搜索 PPT 内容
- 支持中英文关键词
- 显示匹配位置和预览

### 2. 完整页面提取
- 提取指定页面的完整文本
- 统计形状和图片数量
- 支持保存到文件

### 3. 批量提取
- 搜索关键词并批量提取
- 自动保存到指定目录
- 生成结构化的文本文件

### 4. PPT 管理
- 列出所有 PPT 内容
- 打开 PPT 文件
- 重建索引

---

## 使用方法

### 首次使用：构建索引

```bash
python scripts/ppt_tool.py --build
```

### 搜索 PPT 内容

```bash
# 搜索关键词
python scripts/ppt_tool.py --search AI
python scripts/ppt_tool.py --search 金融
python scripts/ppt_tool.py --search OpenClaw
```

### 提取单页完整内容

```bash
# 提取指定 PPT 的指定页面
python scripts/ppt_tool.py --extract ai-agent-tech-insights.pptx 1
python scripts/ppt_tool.py --extract OpenClaw_Finance_Analysis.pptx 3
```

### 批量提取匹配页面

```bash
# 提取所有匹配 "AI" 的页面到默认目录
python scripts/ppt_tool.py --extract-all AI

# 提取到指定目录
python scripts/ppt_tool.py --extract-all OpenClaw C:\Users\Administrator\Desktop\提取结果
```

### 列出所有内容

```bash
python scripts/ppt_tool.py --list
```

### 打开 PPT 文件

```bash
# 打开 PPT
python scripts/ppt_tool.py --open ai-agent-tech-insights.pptx

# 打开并提示跳转到指定页面
python scripts/ppt_tool.py --open ai-agent-tech-insights.pptx 1
```

---

## 配置说明

### 路径配置

编辑 `scripts/ppt_tool.py` 中的配置：

```python
# PPT 文件目录
ppt_dir = r"C:\Users\Administrator\Desktop\PPT集合"

# 索引文件路径
index_file = r"C:\Users\Administrator\AppData\Roaming\memu-bot\agent-output\ppt_index.json"

# 默认提取输出目录
default_output_dir = r"C:\Users\Administrator\AppData\Roaming\memu-bot\agent-output\ppt_extracted"
```

---

## 工作流程

### 索引构建流程

```
[所有 PPT 文件]
    ↓
[打开 PPT]
    ↓
[遍历每一页]
    ↓
[提取文本、统计形状和图片]
    ↓
[保存到 JSON 索引]
    ↓
[索引构建完成]
```

### 搜索流程

```
[用户输入关键词]
    ↓
[加载 JSON 索引]
    ↓
[遍历所有 PPT 和页面]
    ↓
[字符串匹配]
    ↓
[显示匹配结果]
```

### 提取流程

```
[打开 PPT 文件]
    ↓
[跳转到指定页面]
    ↓
[提取所有文本块]
    ↓
[统计形状和图片数量]
    ↓
[保存到文件/显示]
```

---

## 索引数据结构

```json
[
  {
    "file": "ai-agent-tech-insights.pptx",
    "path": "C:\\Users\\Administrator\\Desktop\\PPT集合\\ai-agent-tech-insights.pptx",
    "total_slides": 12,
    "slides": [
      {
        "page": 1,
        "title": "AI Agent 技术研发与迭代",
        "text": "AI Agent 技术研发与迭代 技术洞察报告..."
      },
      ...
    ]
  },
  ...
]
```

---

## 输出文件格式

### 提取的文本文件

```
======================================================================
PPT Page Extract: <文件名>
======================================================================

Page: <页码>
Path: <完整路径>
Shapes: <形状数量>
Images: <图片数量>
Title: <标题>

----------------------------------------------------------------------
Full Text:
----------------------------------------------------------------------

<完整文本内容>
```

---

## 性能指标

| 操作 | 耗时 |
|------|------|
| 构建索引（13 个 PPT，102 页） | ~5-10 秒 |
| 搜索 "AI"（找到 20 个结果） | < 100 毫秒 |
| 提取单页 | < 50 毫秒 |
| 批量提取 4 页 | ~1-2 秒 |

---

## 依赖项

安装依赖：

```bash
pip install -r requirements.txt
```

或手动安装：

```bash
pip install python-pptx
```

---

## 技术栈

- **Python 3.7+**
- **python-pptx** - PPT 文件读取
- **JSON** - 索引存储

---

## 使用示例

### 示例 1：快速查找

```bash
python scripts/ppt_tool.py --search "AI Agent"
```

### 示例 2：提取特定页面

```bash
python scripts/ppt_tool.py --extract OpenClaw_Finance_Analysis.pptx 3
```

### 示例 3：批量提取研究资料

```bash
python scripts/ppt_tool.py --extract-all 金融分析 C:\Users\Administrator\Desktop\金融分析资料
```

---

## 常见问题

### Q: 为什么需要先构建索引？

A: 构建索引是为了提取 PPT 每一页的文本内容并保存到 JSON 文件，这样搜索时就不需要打开每个 PPT 文件，速度会快很多。

### Q: 如何更新索引？

A: 当 PPT 文件有变化时，重新运行构建索引命令：

```bash
python scripts/ppt_tool.py --build
```

### Q: 提取的内容包括图片吗？

A: 不包括图片内容。工具只提取文本内容，但会统计图片数量。

### Q: 可以提取 PPT 中的表格数据吗？

A: 可以。表格中的文本也会被提取出来。

---

## 文件结构

```
ppt-finder/
├── SKILL.md              # 技能文档（当前文件）
├── README.md             # 快速开始指南
├── requirements.txt      # Python 依赖
└── scripts/
    ├── ppt_tool.py       # 主工具脚本
    ├── ppt_search.py     # 搜索功能
    └── ppt_extract.py    # 提取功能
```

---

## 下一步优化方向

1. **模糊搜索**：支持相似词匹配
2. **多关键词逻辑**：支持 AND / OR / NOT 逻辑
3. **正则表达式**：支持正则表达式匹配
4. **GUI 界面**：提供图形化搜索界面
5. **自动更新索引**：检测 PPT 文件变化时自动更新

---

## 作者

memu-bot

---

## 许可证

MIT License
