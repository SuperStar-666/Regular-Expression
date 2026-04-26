import re

text = "我的邮箱是abc123@gmail.com，请发送邮件至该地址。其他邮箱地址为hello@outlook.com和test@test.org。"

# 邮箱正则表达式
pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# 使用 finditer 查找所有匹配项，返回一个迭代器
matches = re.finditer(pattern, text)

print("提取到的邮箱地址如下：")
for match in matches:
    print(match.group())
