# 测试Python环境
print("Python环境测试")
try:
    import sys
    print(f"Python版本: {sys.version}")
    
    # 测试requests库
    try:
        import requests
        print("requests库可用")
    except ImportError:
        print("requests库不可用，请运行: pip install requests")
    
    # 测试smtplib
    try:
        import smtplib
        print("smtplib库可用")
    except ImportError:
        print("smtplib库不可用")
    
    print("测试完成！")
except Exception as e:
    print(f"测试失败: {e}")