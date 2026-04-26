import re

text = "联系我手机号码是 123-4567-8901，还有一个备用号码是 987-6543-2109。"

# 正则表达式解释：
# \d{3}  -> 匹配 3 个数字
# -      -> 匹配一个连字符
# \d{4}  -> 匹配 4 个数字
# -      -> 匹配一个连字符
# \d{4}  -> 匹配 4 个数字

pattern = r'\d{3}-\d{4}-\d{4}'
# pattern = r'1[3-9]\d{9}'

# 使用 findall 查找所有符合条件的结果
results = re.findall(pattern, text)

print("提取到的手机号码：")
print(results)
