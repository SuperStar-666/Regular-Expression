import re

html = '''<tr>\n<th width="12%">排名</th>\n<th width="36%">品牌</th>\n<th width="18%">1月销量</th>\n<th width="18%">全年销量</th>\n<th width="16%">最佳车型</th>\n</tr>'''

# 正则表达式解析：
# <th       匹配起始标签 <th
# [^>]*     匹配标签内的任意属性（如 width="12%"），[^>] 表示匹配除了 > 以外的任意字符
# >         匹配标签结束符 >
# (.*?)     捕获组：非贪婪模式匹配标签内的文本内容
# </th>     匹配结束标签
pattern = r'<th[^>]*>(.*?)</th>'

# 使用 findall 查找所有符合正则的内容，返回一个列表
results = re.findall(pattern, html)

print("提取到的内容如下：")
for item in results:
    print(item)
