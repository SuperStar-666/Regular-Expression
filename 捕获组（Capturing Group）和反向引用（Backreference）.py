import re

# 定义正则表达式
pattern = r'^([A-Z])([A-Z])\2\1$'

def validate_pattern(text):
    """验证字符串是否符合要求"""
    if re.match(pattern, text):
        print(f"✅ '{text}' 匹配成功")
    else:
        print(f"❌ '{text}' 匹配失败")

print("=== 符合要求的测试用例 ===")
validate_pattern("ABBA")  # 标准对称
validate_pattern("XYYX")  # 不同字母组合
validate_pattern("ANNA")  # 实际单词
validate_pattern("TOOT")  # 实际单词
validate_pattern("ZZZZ")  # 四个相同字母也符合逻辑

print("\n=== 不符合要求的测试用例 ===")
validate_pattern("ABCD")  # 不对称
validate_pattern("AABB")  # 前两个相同，后两个相同，但不是回文结构
validate_pattern("abba")  # 小写字母不符合 [A-Z]
validate_pattern("ABC")   # 长度不足4位
validate_pattern("ABBA ") # 尾部带空格
validate_pattern("1ABB1") # 包含数字
