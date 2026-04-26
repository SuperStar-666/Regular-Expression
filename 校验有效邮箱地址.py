import re


def validate_email(email):
    # 邮箱正则表达式
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # 使用 match 函数进行匹配
    result = re.match(pattern, email)

    if result:
        print(f"✅ '{email}' 是一个有效的邮箱地址")
        return True
    else:
        print(f"❌ '{email}' 不是一个有效的邮箱地址")
        return False


# 测试示例
validate_email("user@example.com")  # 有效
validate_email("test.email+tag@domain.co.uk")  # 有效
validate_email("invalid-email@")  # 无效
validate_email("@missing-username.com")  # 无效
