# Daily News Email

一个使用GitHub Actions自动发送每日新闻到邮箱的项目。

## 功能特点

- 每天自动获取最新新闻
- 使用60s API获取新闻数据
- 自动发送HTML格式邮件
- 完全免费，使用GitHub Actions

## 配置

1. 在GitHub Secrets中配置`EMAIL_PASSWORD`
2. 邮箱地址已在`main.py`中设置为：867480991@qq.com
3. 启用GitHub Actions

## 使用

- 定时运行：每天UTC时间0点（北京时间8点）
- 手动触发：在Actions页面点击"Run workflow"
- 推送触发：每次推送代码到main分支时自动运行

## 技术栈

- Python
- GitHub Actions
- SMTP邮件发送

## 最新更新

2026-04-14：添加了推送触发功能，方便测试
