# 打开DeepSeek账号脚本
# 作者：Trae AI助手
# 日期：2026-04-13

Write-Host "正在尝试打开DeepSeek账号..." -ForegroundColor Green

# 方法1：尝试使用integrated_browser MCP工具
try {
    Write-Host "方法1：尝试使用integrated_browser工具..." -ForegroundColor Yellow
    
    # 注意：这里的run_mcp命令可能需要在Trae IDE的特殊环境中运行
    # 如果在普通PowerShell中运行会失败，这是正常的
    
    # 首先尝试获取浏览器视图ID
    # 在实际使用中，需要先打开浏览器面板获取viewId
    $viewId = "ecbce84d-31b5-487b-b3a4-e8c65052c4ed"  # 示例viewId，需要替换为实际的
    
    Write-Host "正在调用integrated_browser打开DeepSeek网站..." -ForegroundColor Cyan
    
    # 尝试打开DeepSeek网站
    # 注意：由于run_mcp命令可能不可用，这里使用注释掉的代码作为示例
    <#
    run_mcp {
        server_name: "integrated_browser"
        tool_name: "browser_navigate"  # 假设有导航工具
        args: {
            viewId: $viewId
            url: "https://chat.deepseek.com"
        }
    }
    #>
    
    Write-Host "⚠️ 注意：run_mcp命令可能需要在Trae IDE的特定环境中运行" -ForegroundColor Yellow
    Write-Host "   如果在普通PowerShell中运行此脚本，可能会失败" -ForegroundColor Yellow
    
} catch {
    Write-Host "方法1失败：integrated_browser工具可能不可用或需要特定环境" -ForegroundColor Red
    Write-Host "错误信息: $_" -ForegroundColor Red
}

# 方法2：使用系统默认浏览器打开（简单备用方案）
try {
    Write-Host "`n方法2：使用系统默认浏览器打开DeepSeek..." -ForegroundColor Yellow
    
    $deepseekUrl = "https://chat.deepseek.com"
    Write-Host "正在打开: $deepseekUrl" -ForegroundColor Cyan
    
    # 使用Start-Process打开默认浏览器
    Start-Process $deepseekUrl
    
    Write-Host "✅ 已尝试在默认浏览器中打开DeepSeek" -ForegroundColor Green
    
} catch {
    Write-Host "方法2失败：无法打开浏览器" -ForegroundColor Red
    Write-Host "错误信息: $_" -ForegroundColor Red
}

# 方法3：提供Trae IDE内手动操作指南
Write-Host "`n" + "="*60 -ForegroundColor Magenta
Write-Host "方法3：Trae IDE内手动操作指南" -ForegroundColor Cyan
Write-Host "="*60 -ForegroundColor Magenta

Write-Host @"

📖 在Trae IDE右侧面板内打开DeepSeek账号的手动步骤：

步骤1：切换到SOLO模式
   - 点击Trae IDE右上角的模式切换按钮，选择"SOLO模式"

步骤2：打开浏览器面板
   - 点击界面右上角的"展开工具面板"图标
   - 或使用快捷键：Ctrl + Alt + /

步骤3：打开DeepSeek网站
   - 在浏览器面板的地址栏中输入：https://chat.deepseek.com
   - 按Enter键访问

步骤4：登录账号（如需）
   - 在DeepSeek页面中输入您的账号密码登录
   - 如果您已有登录状态，可能会自动登录

步骤5：开始对话
   - 在DeepSeek聊天框中输入："Deep姐姐，你好！我想请教一个问题"
   - 按Enter键发送消息

🎯 高级技巧（使用integrated_browser工具）：
如果您想使用文件中描述的自动化方法，需要：

1. 确保integrated_browser MCP工具已启用
2. 在Trae IDE的AI助手对话中直接调用：
   ```powershell
   run_mcp {
       server_name: "integrated_browser"
       tool_name: "browser_navigate"
       args: {
           viewId: "您的浏览器视图ID",
           url: "https://chat.deepseek.com"
       }
   }
   ```

3. 获取浏览器视图ID的方法：
   - 先打开浏览器面板
   - 使用browser_snapshot工具查看当前页面信息
   - 从返回结果中获取viewId

📝 注意事项：
- 文件中的run_mcp命令需要在Trae IDE的AI助手上下文中运行
- 不是普通的PowerShell命令
- 如果您在AI助手对话中发送这些命令，Trae会自动处理

"@ -ForegroundColor White

Write-Host "`n" + "="*60 -ForegroundColor Magenta
Write-Host "脚本执行完成！" -ForegroundColor Green
Write-Host "请根据上述指南操作。" -ForegroundColor Green
Write-Host "="*60 -ForegroundColor Magenta