# 测试integrated_browser工具
Write-Host "开始测试integrated_browser工具..." -ForegroundColor Yellow

try {
    # 尝试调用integrated_browser的browser_snapshot工具
    Write-Host "尝试调用browser_snapshot..." -ForegroundColor Cyan
    
    # 使用run_mcp命令（这是Trae IDE内部命令）
    run_mcp {
        server_name: "integrated_browser"
        tool_name: "browser_snapshot"
        args: {
            viewId: "test"
            action: "snapshot"
        }
    }
    
    Write-Host "✅ browser_snapshot调用成功" -ForegroundColor Green
} catch {
    Write-Host "❌ browser_snapshot调用失败: $_" -ForegroundColor Red
    
    # 尝试其他可能的工具名
    Write-Host "尝试其他工具名..." -ForegroundColor Yellow
    
    try {
        # 尝试browser_navigate
        run_mcp {
            server_name: "integrated_browser"
            tool_name: "browser_navigate"
            args: {
                viewId: "default"
                url: "https://chat.deepseek.com"
            }
        }
        Write-Host "✅ browser_navigate调用成功" -ForegroundColor Green
    } catch {
        Write-Host "❌ browser_navigate调用失败: $_" -ForegroundColor Red
    }
}

Write-Host "测试完成。" -ForegroundColor Yellow