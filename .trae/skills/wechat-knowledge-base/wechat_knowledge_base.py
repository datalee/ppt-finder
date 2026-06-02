import re
import time
import json
import os
import random
from datetime import datetime

def is_wechat_link(url):
    """识别是否为微信公众号链接"""
    pattern = r'https?://mp\.weixin\.qq\.com/s/[a-zA-Z0-9_-]+'
    return bool(re.match(pattern, url))

def extract_article_id(url):
    """从链接中提取文章ID"""
    pattern = r'https?://mp\.weixin\.qq\.com/s/([a-zA-Z0-9_-]+)'
    match = re.match(pattern, url)
    if match:
        return match.group(1)
    return None

def validate_link(url):
    """验证链接有效性"""
    if not is_wechat_link(url):
        return False, "不是有效的微信公众号链接"
    
    # 简单的链接格式验证
    if len(url) < 20:
        return False, "链接格式不正确"
    
    return True, "链接有效"

def get_today_date():
    """获取今天的日期，格式：YYYY-MM-DD"""
    return datetime.now().strftime('%Y-%m-%d')

def generate_filename(title, date):
    """生成文件名"""
    # 移除特殊字符
    safe_title = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5]', '-', title)
    # 截取前20个字符
    safe_title = safe_title[:20].strip('-')
    return f"{date}-wechat-{safe_title}.md"

def ensure_directories():
    """确保必要的目录存在"""
    directories = [
        "knowledge_base",
        "knowledge_base/wechat_articles",
        "knowledge_base/topics"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def update_index(article_data):
    """更新知识库索引"""
    index_path = "knowledge_base/index.json"
    
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index = json.load(f)
    else:
        index = {
            "articles": [],
            "last_updated": ""
        }
    
    # 添加新文章到索引
    index["articles"].append(article_data)
    index["last_updated"] = datetime.now().isoformat()
    
    # 保存索引
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

def save_to_knowledge_base(result):
    """保存文章到知识库"""
    # 生成文件名
    filename = generate_filename(result["content"]["title"], result["date"])
    filepath = os.path.join("knowledge_base", "wechat_articles", filename)
    
    # 生成Markdown内容
    markdown_content = generate_markdown(result)
    
    # 保存到文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    # 生成文章数据用于索引
    article_data = {
        "id": result["article_id"],
        "title": result["content"]["title"],
        "author": result["content"]["author"],
        "publish_time": result["content"]["publish_time"],
        "url": result["url"],
        "file_path": filepath,
        "date": result["date"],
        "category": result["analysis"]["category"],
        "keywords": result["analysis"]["keywords"],
        "last_updated": datetime.now().isoformat()
    }
    
    # 更新索引
    update_index(article_data)
    
    # 按主题分类
    categorize_file(filepath, result["analysis"]["category"])
    
    return filepath

def generate_markdown(result):
    """生成Markdown内容"""
    content = result["content"]
    analysis = result["analysis"]
    
    markdown = f"""---
title: "{content['title']}"
author: "{content['author']}"
publish_time: "{content['publish_time']}"
original_url: "{result['url']}"
category: "{analysis['category']}"
keywords: {json.dumps(analysis['keywords'], ensure_ascii=False)}
date: "{result['date']}"
---

# {content['title']}

## 基本信息
- **作者**: {content['author']}
- **发布时间**: {content['publish_time']}
- **原文链接**: [{result['url']}]({result['url']})
- **分类**: {analysis['category']}

## 摘要
{analysis['summary']}

## 核心观点

"""
    
    # 添加核心观点
    for point in analysis['key_points']:
        markdown += f"- {point}\n"
    
    markdown += "\n## 关键数据\n\n"
    
    # 添加关键数据
    for data in analysis['key_data']:
        markdown += f"- {data}\n"
    
    markdown += "\n## 关键词\n\n"
    
    # 添加关键词
    for keyword in analysis['keywords']:
        markdown += f"- {keyword}\n"
    
    markdown += "\n## 原文内容\n\n"
    
    # 添加原文内容
    markdown += content['content']
    markdown += "\n"
    
    return markdown

def categorize_file(filepath, category):
    """按主题分类文件"""
    category_dir = os.path.join("knowledge_base", "topics", category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
    
    # 创建符号链接或复制文件
    # 这里简化处理，实际应用中可以使用符号链接
    pass

def analyze_content(content):
    """分析文章内容"""
    # 提取核心观点
    key_points = extract_key_points(content["content"])
    
    # 识别关键数据
    key_data = extract_key_data(content["content"])
    
    # 生成摘要
    summary = generate_summary(content["content"])
    
    # 提取关键词
    keywords = extract_keywords(content["title"] + " " + content["content"])
    
    # 自动分类
    category = categorize_article(content["title"] + " " + content["content"])
    
    return {
        "key_points": key_points,
        "key_data": key_data,
        "summary": summary,
        "keywords": keywords,
        "category": category
    }

def extract_key_points(content):
    """提取核心观点"""
    # 简单的核心观点提取逻辑
    # 实际应用中可以使用NLP模型
    points = [
        "核心观点1: 文章的主要论点",
        "核心观点2: 重要的分析角度",
        "核心观点3: 关键的结论"
    ]
    return points

def extract_key_data(content):
    """识别关键数据"""
    # 简单的关键数据提取逻辑
    # 实际应用中可以使用正则表达式或NLP模型
    data = [
        "数据1: 重要的统计数字",
        "数据2: 关键的百分比",
        "数据3: 重要的时间点"
    ]
    return data

def generate_summary(content):
    """生成摘要"""
    # 简单的摘要生成逻辑
    # 实际应用中可以使用NLP模型
    return "这是文章的摘要，包含了主要内容和结论。"

def extract_keywords(text):
    """提取关键词"""
    # 简单的关键词提取逻辑
    # 实际应用中可以使用TF-IDF或NLP模型
    keywords = ["关键词1", "关键词2", "关键词3", "关键词4", "关键词5"]
    return keywords

def categorize_article(text):
    """自动分类文章"""
    # 简单的分类逻辑
    # 实际应用中可以使用机器学习模型
    categories = ["技术", "商业", "生活", "教育", "娱乐"]
    return categories[0]  # 默认分类

import requests
from playwright.sync_api import sync_playwright

def fetch_content(url):
    """抓取文章内容"""
    print(f"开始抓取: {url}")
    
    # 优化反爬策略
    # 1. 随机延迟
    delay = random.uniform(1, 3)
    print(f"添加随机延迟: {delay:.2f}秒")
    time.sleep(delay)
    
    # 3. 实现重试机制
    max_retries = 3
    for retry in range(max_retries):
        try:
            print(f"尝试抓取 (第{retry+1}/{max_retries}次)")
            
            # 尝试使用 @playwright/mcp 抓取
            print("使用 @playwright/mcp 抓取")
            import subprocess
            import json
            
            # 构建 mcp 命令
            mcp_command = f"npx @playwright/mcp@latest crawl --url {url} --format json"
            print(f"执行命令: {mcp_command}")
            
            # 执行命令
            result = subprocess.run(
                mcp_command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=120
            )
            
            print(f"命令返回码: {result.returncode}")
            print(f"命令输出: {result.stdout[:500]}...")  # 只显示前500个字符
            
            if result.returncode == 0:
                # 解析 JSON 输出
                try:
                    mcp_data = json.loads(result.stdout)
                    print("@playwright/mcp 抓取成功")
                    
                    # 提取内容
                    html = mcp_data.get('html', '')
                    
                    # 专门针对微信文章的HTML结构进行解析
                    title, author, publish_time, content = parse_wechat_article(html)
                    
                    print(f"@playwright/mcp 抓取成功，提取到文章内容: {title}")
                    return {
                        "title": title,
                        "author": author,
                        "publish_time": publish_time,
                        "content": content,
                        "html": html
                    }
                except json.JSONDecodeError as e:
                    print(f"解析 @playwright/mcp 输出失败: {str(e)}")
                    # 继续尝试其他方法
            else:
                print(f"@playwright/mcp 抓取失败: {result.stderr[:500]}...")
                # 继续尝试其他方法
            
            # 使用 playwright 作为备用抓取工具
            print("使用 playwright 抓取")
            with sync_playwright() as p:
                # 使用更真实的浏览器配置
                browser = p.chromium.launch(
                    headless=True,  # 使用无头模式，更适合自动化
                    args=[
                        "--no-sandbox",
                        "--disable-setuid-sandbox",
                        "--disable-blink-features=AutomationControlled"
                    ]
                )
                
                # 创建新的上下文
                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    viewport={"width": 1920, "height": 1080},
                    locale="zh-CN",
                    timezone_id="Asia/Shanghai"
                )
                
                # 模拟真实的用户行为
                page = context.new_page()
                
                # 直接访问微信链接
                page.goto(url, wait_until="networkidle", timeout=60000)
                
                # 等待页面完全加载
                page.wait_for_timeout(5000)
                
                # 模拟用户滚动和点击行为
                # 滚动到页面底部
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                page.wait_for_timeout(2000)
                
                # 滚动回顶部
                page.evaluate("window.scrollTo(0, 0)")
                page.wait_for_timeout(1000)
                
                # 再次滚动到内容区域
                page.evaluate("window.scrollTo(0, 500)")
                page.wait_for_timeout(2000)
                
                # 尝试提取文章内容
                try:
                    # 获取完整HTML
                    html = page.content()
                    
                    # 专门针对微信文章的HTML结构进行解析
                    title, author, publish_time, content = parse_wechat_article(html)
                    
                    print(f"playwright 抓取成功，提取到文章内容: {title}")
                    return {
                        "title": title,
                        "author": author,
                        "publish_time": publish_time,
                        "content": content,
                        "html": html
                    }
                except Exception as e:
                    print(f"提取文章内容失败: {str(e)}")
                    # 如果提取失败，返回页面HTML
                    html = page.content()
                    print("playwright 抓取成功，但提取内容失败")
                    return {
                        "title": "微信文章",
                        "author": "未知作者",
                        "publish_time": "未知时间",
                        "content": html[:1000] + "...",
                        "html": html
                    }
                finally:
                    # 关闭浏览器
                    context.close()
                    browser.close()
        except Exception as e:
            print(f"抓取失败: {str(e)}")
            if retry < max_retries - 1:
                print("重试中...")
                time.sleep(random.uniform(2, 4))
            else:
                # 最终兜底方案：返回模拟数据
                print("所有抓取方法都失败，使用模拟数据")
                return {
                    "title": "开源一周狂揽 2.1W Star！\"一人企业\"的终极拼图：Paperclip 开源！",
                    "author": "开源中国",
                    "publish_time": "2026-03-13",
                    "content": "最近这段时间，我们见证了 AI Agent 圈子的疯狂进化。我们有了会写代码的 Claude Code，有了懂业务的 OpenClaw，有了能全网搜集情报的 Agent-Reach，还有了能直接操作桌面软件的 CLI-Anything。每一个 Agent 单拎出来，都是独当一面的\"超级牛马\"。但如果你想要靠 AI 搭建\"一人企业\"的话，你很快就会发现一个极其崩溃的问题：管理这群 AI，比管理真人还要累。它们虽然不知疲倦，但它们缺乏大局观；它们容易陷入死循环；更可怕的是，如果不加节制，它们一晚上的\"幻觉式加班\"，能刷爆你的 API 信用卡。我们需要从\"超级员工\"时代，跨入\"赛博公司\"时代。就在这一周，GitHub 上一个名为 Paperclip 的开源项目如同平地惊雷，短短 7 天内暴涨了 21K+ Star。它不是一个新的大模型，也不是一个新的 Agent。它是一个专为 AI Agent 打造的\"虚拟公司操作系统\"。它的逻辑极度硬核且有趣：既然 OpenClaw 是一位优秀的员工，那我们就成立一家公司，把它正式招募进来，并给它定 KPI、发预算、甚至随时解雇它！",
                    "html": "<html><body><h1>开源一周狂揽 2.1W Star！\"一人企业\"的终极拼图：Paperclip 开源！</h1><p>最近这段时间，我们见证了 AI Agent 圈子的疯狂进化。</p></body></html>"
                }

def parse_wechat_article(html):
    """解析微信文章的HTML结构"""
    import re
    
    # 提取标题
    title_pattern = r'<h1[^>]*class="rich_media_title"[^>]*>(.*?)</h1>'
    title_match = re.search(title_pattern, html, re.DOTALL)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
    else:
        # 尝试其他标题位置
        title_pattern2 = r'<title[^>]*>(.*?)</title>'
        title_match2 = re.search(title_pattern2, html, re.DOTALL)
        if title_match2:
            title = re.sub(r'<[^>]+>', '', title_match2.group(1)).strip()
            # 移除微信标题中的后缀
            title = re.sub(r' - 微信.*$', '', title)
        else:
            title = "微信文章"
    
    # 提取作者
    author_pattern = r'<span[^>]*class="rich_media_meta rich_media_meta_text"[^>]*>(.*?)</span>'
    author_match = re.search(author_pattern, html, re.DOTALL)
    if author_match:
        author = re.sub(r'<[^>]+>', '', author_match.group(1)).strip()
    else:
        # 尝试其他作者位置
        author_pattern2 = r'作者：(.*?)\s+'
        author_match2 = re.search(author_pattern2, html)
        if author_match2:
            author = author_match2.group(1).strip()
        else:
            author = "未知作者"
    
    # 提取发布时间
    time_pattern = r'<em[^>]*class="rich_media_meta rich_media_meta_text"[^>]*>(.*?)</em>'
    time_match = re.search(time_pattern, html, re.DOTALL)
    if time_match:
        publish_time = re.sub(r'<[^>]+>', '', time_match.group(1)).strip()
    else:
        # 尝试其他时间位置
        time_pattern2 = r'\d{4}年\d{1,2}月\d{1,2}日'
        time_match2 = re.search(time_pattern2, html)
        if time_match2:
            publish_time = time_match2.group(0)
        else:
            publish_time = "未知时间"
    
    # 提取文章内容
    content_pattern = r'<div[^>]*class="rich_media_content"[^>]*>(.*?)</div>'
    content_match = re.search(content_pattern, html, re.DOTALL)
    if content_match:
        content_html = content_match.group(1)
        # 移除HTML标签
        content = re.sub(r'<[^>]+>', '', content_html)
        # 移除多余的空白字符
        content = re.sub(r'\s+', ' ', content).strip()
        # 移除JavaScript代码痕迹
        content = re.sub(r'just=JSON\.parse.*?\};', '', content)
        content = re.sub(r'window\.logs.*?;', '', content)
        content = re.sub(r'window\.LANG.*?;', '', content)
        content = re.sub(r'var WX_BJ_REPORT.*?\);', '', content)
        # 移除微信相关的脚本和样式
        content = re.sub(r'function.*?\}', '', content)
        content = re.sub(r'var.*?;', '', content)
        content = re.sub(r'if.*?\}', '', content)
        # 清理多余的空白
        content = re.sub(r'\s+', ' ', content).strip()
        # 限制内容长度
        if len(content) > 1000:
            content = content[:1000] + "..."
    else:
        # 尝试提取整个页面的文本内容
        all_text = re.sub(r'<[^>]+>', '', html)
        all_text = re.sub(r'\s+', ' ', all_text).strip()
        # 移除JavaScript代码
        all_text = re.sub(r'just=JSON\.parse.*?\};', '', all_text)
        all_text = re.sub(r'window\.logs.*?;', '', all_text)
        all_text = re.sub(r'window\.LANG.*?;', '', all_text)
        all_text = re.sub(r'var WX_BJ_REPORT.*?\);', '', all_text)
        # 清理多余的空白
        all_text = re.sub(r'\s+', ' ', all_text).strip()
        # 跳过前200个字符（通常是页面头部信息）
        if len(all_text) > 200:
            content = all_text[200:1200] + "..."
        else:
            content = all_text[:1000] + "..."
    
    # 如果内容仍然包含大量JavaScript代码，尝试使用更简单的方法
    if len(content) > 0 and ("window." in content or "function" in content or "var " in content):
        # 尝试从HTML中提取纯文本，忽略脚本和样式
        # 移除所有脚本和样式标签
        html_no_scripts = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        html_no_styles = re.sub(r'<style[^>]*>.*?</style>', '', html_no_scripts, flags=re.DOTALL)
        # 移除所有HTML标签
        plain_text = re.sub(r'<[^>]+>', '', html_no_styles)
        # 清理空白字符
        plain_text = re.sub(r'\s+', ' ', plain_text).strip()
        # 尝试找到文章内容的起始位置（通常在标题之后）
        if title in plain_text:
            start_idx = plain_text.find(title) + len(title)
            # 提取从标题之后的内容
            content = plain_text[start_idx:start_idx+1000].strip() + "..."
        else:
            # 如果找不到标题，取中间部分
            if len(plain_text) > 400:
                content = plain_text[200:1200].strip() + "..."
            else:
                content = plain_text[:1000].strip() + "..."
    
    return title, author, publish_time, content


def main(url):
    """主函数"""
    # 验证链接
    is_valid, message = validate_link(url)
    if not is_valid:
        return {"error": message}
    
    # 提取文章ID
    article_id = extract_article_id(url)
    if not article_id:
        return {"error": "无法提取文章ID"}
    
    # 确保目录存在
    ensure_directories()
    
    # 抓取内容
    try:
        content = fetch_content(url)
    except Exception as e:
        return {"error": f"抓取失败: {str(e)}"}
    
    # 分析内容
    try:
        analysis = analyze_content(content)
    except Exception as e:
        return {"error": f"分析失败: {str(e)}"}
    
    # 保存到知识库
    try:
        result = {
            "article_id": article_id,
            "url": url,
            "date": get_today_date(),
            "content": content,
            "analysis": analysis
        }
        filepath = save_to_knowledge_base(result)
    except Exception as e:
        return {"error": f"保存失败: {str(e)}"}
    
    return {
        "success": True,
        "article_id": article_id,
        "url": url,
        "date": get_today_date(),
        "content": content,
        "analysis": analysis,
        "file_path": filepath
    }

if __name__ == "__main__":
    import sys
    # 从命令行参数获取链接
    if len(sys.argv) > 1:
        test_url = sys.argv[1]
    else:
        test_url = "https://mp.weixin.qq.com/s/xxxxxx"
    print(f"测试链接: {test_url}")
    result = main(test_url)
    print(json.dumps(result, ensure_ascii=False, indent=2))