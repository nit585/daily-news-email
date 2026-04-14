import smtplib
import requests
from email.mime.text import MIMEText
from email.header import Header
import os

def translate_text(text, from_lang='en', to_lang='zh'):
    """简单的翻译功能，使用免费翻译API"""
    try:
        # 使用MyMemory免费翻译API
        url = f"https://api.mymemory.translated.net/get?q={text}&langpair={from_lang}|{to_lang}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('responseStatus') == 200:
            return data['responseData']['translatedText']
        else:
            return text
    except Exception as e:
        print(f"翻译失败: {e}")
        return text

def get_news_from_newsapi():
    """从NewsAPI.org获取国际新闻"""
    try:
        api_key = os.environ.get("NEWS_API_KEY", "")
        if not api_key:
            return "⚠️ 未设置NEWS_API_KEY环境变量，请先获取API Key\n\n获取方式：访问 https://newsapi.org/ 注册免费账户"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        # 获取国际头条新闻（使用英语，country=us）
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=10&apiKey={api_key}"
        
        print("正在请求NewsAPI.org...")
        response = requests.get(url, headers=headers, timeout=10)
        print(f"NewsAPI.org响应状态码: {response.status_code}")
        print(f"NewsAPI.org响应内容预览: {response.text[:200]}")
        
        response.raise_for_status()
        data = response.json()
        print(f"NewsAPI.org解析后的JSON数据: {data}")
        
        articles = data.get("articles", [])
        
        # 构建HTML内容
        html_content = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>NewsAPI.org - 国际新闻</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                h1 {{ color: #333; }}
                .news-item {{ margin-bottom: 15px; padding: 10px; border-bottom: 1px solid #eee; }}
                .news-title {{ font-weight: bold; color: #1a73e8; }}
                .news-source {{ color: #666; font-size: 0.9em; }}
                .news-desc {{ margin-top: 5px; color: #333; }}
            </style>
        </head>
        <body>
            <h1>🌐 NewsAPI.org 国际新闻</h1>
            <h2>今日头条</h2>
        """
        
        for i, article in enumerate(articles, 1):
            title = article.get("title", "无标题")
            source = article.get("source", {}).get("name", "未知来源")
            description = article.get("description", "")
            url = article.get("url", "")
            
            html_content += f"""
            <div class="news-item">
                <div class="news-title">{i}. <a href="{url}" target="_blank">{title}</a></div>
                <div class="news-source">来源: {source}</div>
                <div class="news-desc">{description}</div>
            </div>
            """
        
        html_content += """
        </body>
        </html>
        """
        
        return html_content
        
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"NewsAPI.org获取新闻失败: {str(e)}")
        print(f"详细错误: {error_details}")
        return f"NewsAPI.org获取新闻失败: {str(e)}\n\n详细错误信息:\n{error_details}"

def get_news_from_gnews():
    """从GNews API获取国际新闻（方案三）"""
    try:
        api_key = os.environ.get("GNEWS_API_KEY", "")
        if not api_key:
            return "⚠️ 未设置GNEWS_API_KEY环境变量，请先获取API Key\n\n获取方式：访问 https://gnews.io/ 注册免费账户"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        # 获取中文国际新闻（使用language=zh和country=cn）
        url = f"https://gnews.io/api/v4/top-headlines?lang=zh&country=cn&max=10&apikey={api_key}"
        
        print("正在请求GNews API...")
        response = requests.get(url, headers=headers, timeout=10)
        print(f"GNews API响应状态码: {response.status_code}")
        print(f"GNews API响应内容预览: {response.text[:200]}")
        
        response.raise_for_status()
        data = response.json()
        print(f"GNews API解析后的JSON数据: {data}")
        
        articles = data.get("articles", [])
        
        # 构建HTML内容
        html_content = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>GNews - 国际新闻</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                h1 {{ color: #333; }}
                .news-item {{ margin-bottom: 15px; padding: 10px; border-bottom: 1px solid #eee; }}
                .news-title {{ font-weight: bold; color: #1a73e8; }}
                .news-source {{ color: #666; font-size: 0.9em; }}
                .news-desc {{ margin-top: 5px; color: #333; }}
            </style>
        </head>
        <body>
            <h1>🌍 GNews 国际新闻</h1>
            <h2>今日头条</h2>
        """
        
        for i, article in enumerate(articles, 1):
            title = article.get("title", "无标题")
            source = article.get("source", {}).get("name", "未知来源")
            description = article.get("description", "")
            url = article.get("url", "")
            
            html_content += f"""
            <div class="news-item">
                <div class="news-title">{i}. <a href="{url}" target="_blank">{title}</a></div>
                <div class="news-source">来源: {source}</div>
                <div class="news-desc">{description}</div>
            </div>
            """
        
        html_content += """
        </body>
        </html>
        """
        
        return html_content
        
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"GNews API获取新闻失败: {str(e)}")
        print(f"详细错误: {error_details}")
        return f"GNews API获取新闻失败: {str(e)}\n\n详细错误信息:\n{error_details}"

def send_email(subject, html_content):
    """发送邮件"""
    # QQ邮箱的SMTP服务器和端口
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    
    # 发件人邮箱（你的QQ邮箱）
    sender_email = "867480991@qq.com"
    
    # 收件人邮箱
    receiver_email = "867480991@qq.com"
    
    # 从环境变量获取授权码
    password = os.environ.get("EMAIL_PASSWORD", "")
    if not password:
        raise Exception("未设置EMAIL_PASSWORD环境变量")
    
    # 创建邮件
    message = MIMEText(html_content, 'html', 'utf-8')
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        # 连接SMTP服务器并发送邮件
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 启用TLS加密
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()
        print("邮件发送成功！")
        return True
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("开始获取NewsAPI.org新闻...")
    news_newsapi = get_news_from_newsapi()
    print("NewsAPI.org新闻获取完成，准备发送邮件...")
    send_email("🌐 NewsAPI.org 国际新闻", news_newsapi)
    
    print("\n" + "=" * 50)
    print("开始获取GNews国际新闻...")
    news_gnews = get_news_from_gnews()
    print("GNews新闻获取完成，准备发送邮件...")
    send_email("🌍 GNews 国际新闻", news_gnews)
    
    print("\n" + "=" * 50)
    print("所有任务完成！")
