import re

# 正则表达式
pattern = r'^1[3-9]\d{9}$'

def validate_phone(phone):
    result = re.match(pattern, phone)
    # result = re.fullmatch(r'1[3-9]\d{9}', phone)    #如果想使用更严格的 fullmatch（确保整个字符串完全匹配），也可以这样写：

    if result:
        print(f"✅ '{phone}' 是有效的手机号")
        return True
    else:
        print(f"❌ '{phone}' 不是有效的手机号")
        return False

# 测试用例
validate_phone('13123456789')  # ✅ 有效
validate_phone('19876543210')  # ✅ 有效
validate_phone('12123456789')  # ❌ 第二位不是3-9
validate_phone('1312345678')   # ❌ 只有10位
validate_phone('131234567890') # ❌ 有12位
