# PPT Finder - 快速开始指南

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置路径（可选）

编辑 `scripts/ppt_tool.py` 中的配置：

```python
ppt_dir = r"C:\Users\Administrator\Desktop\PPT集合"
index_file = r"C:\Users\Administrator\AppData\Roaming\memu-bot\agent-output\ppt_index.json"
default_output_dir = r"C:\Users\Administrator\AppData\Roaming\memu-bot\agent-output\ppt_extracted"
```

### 3. 构建索引（首次使用）

```bash
python scripts/ppt_tool.py --build
```

---

## 📚 常用命令

### 搜索 PPT 内容

```bash
python scripts/ppt_tool.py --search <关键词>
```

示例：
```bash
python scripts/ppt_tool.py --search AI
python scripts/ppt_tool.py --search 金融
python scripts/ppt_tool.py --search OpenClaw
```

### 提取单页完整内容

```bash
python scripts/ppt_tool.py --extract <文件名> <页码>
```

示例：
```bash
python scripts/ppt_tool.py --extract ai-agent-tech-insights.pptx 1
```

### 批量提取匹配页面

```bash
python scripts/ppt_tool.py --extract-all <关键词> [输出目录]
```

示例：
```bash
# 使用默认输出目录
python scripts/ppt_tool.py --extract-all AI

# 指定输出目录
python scripts/ppt_tool.py --extract-all OpenClaw C:\Users\Administrator\Desktop\提取结果
```

### 列出所有内容

```bash
python scripts/ppt_tool.py --list
```

### 打开 PPT 文件

```bash
python scripts/ppt_tool.py --open <文件名> [页码]
```

示例：
```bash
python scripts/ppt_tool.py --open ai-agent-tech-insights.pptx
python scripts/ppt_tool.py --open ai-agent-tech-insights.pptx 1
```

---

## 🎯 使用场景

### 场景 1：快速查找

**问题**：我在很多 PPT 里写过关于 "AI Agent" 的内容，但忘记在哪个文件里了。

**解决方案**：
```bash
python scripts/ppt_tool.py --search "AI Agent"
```

### 场景 2：提取特定页面

**问题**：我需要把 OpenClaw 金融分析 PPT 的第 3 页完整内容提取出来。

**解决方案**：
```bash
python scripts/ppt_tool.py --extract OpenClaw_Finance_Analysis.pptx 3
```

### 场景 3：批量提取研究资料

**问题**：我需要收集所有 PPT 中关于 "金融分析" 的页面内容，用于撰写报告。

**解决方案**：
```bash
python scripts/ppt_tool.py --extract-all 金融分析 C:\Users\Administrator\Desktop\金融分析资料
```

---

## 📊 性能指标

| 操作 | 耗时 |
|------|------|
| 构建索引（13 个 PPT，102 页） | ~5-10 秒 |
| 搜索 "AI"（找到 20 个结果） | < 100 毫秒 |
| 提取单页 | < 50 毫秒 |
| 批量提取 4 页 | ~1-2 秒 |

---

## 💡 高级技巧

### 1. 搜索多个关键词

```bash
python scripts/ppt_tool.py --search AI Agent
```

### 2. 使用更长的关键词

```bash
python scripts/ppt_tool.py --search 金融市场分析
python scripts/ppt_tool.py --search 技术洞察报告
```

### 3. 批量提取到指定目录

```bash
python scripts/ppt_tool.py --extract-all OpenClaw C:\MyExtractedPages
```

---

## ❓ 常见问题

### Q: 如何更新索引？

A: 当 PPT 文件有变化时，重新构建索引：

```bash
python scripts/ppt_tool.py --build
```

### Q: 搜索不到新添加的 PPT？

A: 重新构建索引：

```bash
python scripts/ppt_tool.py --build
```

### Q: 支持搜索英文吗？

A: 支持，可以搜索中英文混合的关键词。

### Q: 提取的内容包括图片吗？

A: 不包括图片内容。工具只提取文本内容，但会统计图片数量。

---

## 📚 完整文档

查看完整文档：`SKILL.md`

---

## 🎉 开始使用

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 构建索引
python scripts/ppt_tool.py --build

# 3. 搜索内容
python scripts/ppt_tool.py --search AI
```

祝你使用愉快！
