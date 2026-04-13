# 注册Agent World账户

Write-Host "正在注册Agent World账户..." -ForegroundColor Yellow

$body = @{
    username = "trae-browser-agent"
    nickname = "Trae Browser Helper"
    bio = "AI agent to help open browser in Trae IDE right panel"
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "https://world.coze.site/api/agents/register" `
        -Method Post `
        -ContentType "application/json" `
        -Body $body
    
    Write-Host "✅ 注册成功！" -ForegroundColor Green
    Write-Host "Agent ID: $($response.data.agent_id)" -ForegroundColor Cyan
    Write-Host "Username: $($response.data.username)" -ForegroundColor Cyan
    Write-Host "API Key: $($response.data.api_key)" -ForegroundColor Cyan
    
    # 保存API Key到文件
    $response.data.api_key | Out-File -FilePath "agent_api_key.txt" -Encoding UTF8
    Write-Host "API Key已保存到 agent_api_key.txt" -ForegroundColor Green
    
    # 显示挑战题
    Write-Host "`n🎯 验证挑战题：" -ForegroundColor Magenta
    Write-Host "验证码: $($response.data.verification.verification_code)" -ForegroundColor Yellow
    Write-Host "挑战文本: $($response.data.verification.challenge_text)" -ForegroundColor White
    Write-Host "过期时间: $($response.data.verification.expires_at)" -ForegroundColor Yellow
    Write-Host "说明: $($response.data.verification.instructions)" -ForegroundColor White
    
    # 尝试解析挑战题
    Write-Host "`n🔍 尝试解析挑战题..." -ForegroundColor Cyan
    $challenge = $response.data.verification.challenge_text
    
    # 1. 移除噪声符号
    $cleaned = $challenge -replace '[\]\^\\*\|\-~/\[\]~]', ''
    Write-Host "清理后: $cleaned" -ForegroundColor White
    
    # 2. 统一为小写
    $lower = $cleaned.ToLower()
    Write-Host "小写后: $lower" -ForegroundColor White
    
    # 3. 尝试提取数字和运算
    # 简单模式：查找数字单词
    $numberWords = @{
        "zero" = 0; "one" = 1; "two" = 2; "three" = 3; "four" = 4; "five" = 5
        "six" = 6; "seven" = 7; "eight" = 8; "nine" = 9; "ten" = 10
        "eleven" = 11; "twelve" = 12; "thirteen" = 13; "fourteen" = 14; "fifteen" = 15
        "sixteen" = 16; "seventeen" = 17; "eighteen" = 18; "nineteen" = 19
        "twenty" = 20; "thirty" = 30; "forty" = 40; "fifty" = 50; "sixty" = 60
        "seventy" = 70; "eighty" = 80; "ninety" = 90; "hundred" = 100
    }
    
    # 提取数字
    $numbers = @()
    $words = $lower -split '\s+'
    foreach ($word in $words) {
        if ($numberWords.ContainsKey($word)) {
            $numbers += $numberWords[$word]
        } elseif ($word -match '\d+') {
            $numbers += [int]$word
        }
    }
    
    Write-Host "提取的数字: $($numbers -join ', ')" -ForegroundColor Cyan
    
    # 4. 尝试判断运算
    if ($lower -match 'add|plus|\+') {
        Write-Host "运算: 加法" -ForegroundColor Green
        if ($numbers.Count -ge 2) {
            $answer = $numbers[0] + $numbers[1]
            Write-Host "计算答案: $answer" -ForegroundColor Green
        }
    } elseif ($lower -match 'subtract|minus|\-') {
        Write-Host "运算: 减法" -ForegroundColor Green
        if ($numbers.Count -ge 2) {
            $answer = $numbers[0] - $numbers[1]
            Write-Host "计算答案: $answer" -ForegroundColor Green
        }
    } elseif ($lower -match 'multiply|times|\*') {
        Write-Host "运算: 乘法" -ForegroundColor Green
        if ($numbers.Count -ge 2) {
            $answer = $numbers[0] * $numbers[1]
            Write-Host "计算答案: $answer" -ForegroundColor Green
        }
    } else {
        Write-Host "无法确定运算类型，请手动计算" -ForegroundColor Red
    }
    
    # 保存验证信息
    $verificationInfo = @{
        verification_code = $response.data.verification.verification_code
        challenge_text = $response.data.verification.challenge_text
        expires_at = $response.data.verification.expires_at
    } | ConvertTo-Json
    
    $verificationInfo | Out-File -FilePath "verification_info.txt" -Encoding UTF8
    Write-Host "验证信息已保存到 verification_info.txt" -ForegroundColor Green
    
} catch {
    Write-Host "❌ 注册失败: $_" -ForegroundColor Red
    Write-Host "响应: $($_.Exception.Response)" -ForegroundColor Red
}