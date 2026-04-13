# Daily News Email

一个使用GitHub Actions自动发送每日新闻到邮箱的项目。

## 功能特点

- 每天自动获取最新新闻
- 使用60s API获取新闻数据
- 自动发送HTML格式邮件
- 完全免费，使用GitHub Actions

## 配置

1. 在GitHub Secrets中配置`EMAIL_PASSWORD`
2. 修改`main.py`中的邮箱地址
3. 启用GitHub Actions

## 使用

- 定时运行：每天UTC时间0点（北京时间8点）
- 手动触发：在Actions页面点击"Run workflow"

## 技术栈

- Python
- GitHub Actions
- SMTP邮件发送
