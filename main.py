import smtplib
import requests
from email.mime.text import MIMEText
from email.header import Header
import os

def get_news():
    """获取新闻数据"""
    try:
        # 使用60s API获取新闻
        response = requests.get("https://api.60s.cn/v1/news")
        response.raise_for_status()
        data = response.json()
        
        news_list = data.get("news", [])
        daily_word = data.get("word", "")
        
        # 构建HTML内容
        html_content = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>每日新闻简报</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                h1 {{ color: #333; }}
                .news-item {{ margin-bottom: 10px; padding: 5px; border-bottom: 1px solid #eee; }}
                .news-title {{ font-weight: bold; }}
                .daily-word {{ background-color: #f5f5f5; padding: 10px; margin: 20px 0; border-left: 4px solid #4CAF50; }}
            </style>
        </head>
        <body>
            <h1>📰 每日新闻简报</h1>
            <div class="daily-word">
                <strong>每日一语：</strong>{daily_word}
            </div>
            <h2>今日要闻</h2>
        """
        
        for i, news in enumerate(news_list, 1):
            html_content += f"""
            <div class="news-item">
                <span class="news-title">{i}. {news}</span>
            </div>
            """
        
        html_content += """
        </body>
        </html>
        """
        
        return html_content
        
    except Exception as e:
        return f"获取新闻失败: {str(e)}"

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
    message['From'] = Header("每日新闻助手", 'utf-8')
    message['To'] = Header("收件人", 'utf-8')
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
    print("开始获取新闻...")
    news_content = get_news()
    print("获取新闻完成，准备发送邮件...")
    send_email("📰 每日新闻简报", news_content)
    print("任务完成！")