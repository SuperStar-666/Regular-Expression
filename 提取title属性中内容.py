import re

html = '<td><a href="/hangye/qiche/pinpai/36.html" title="大众" target="_blank" class="cty"></td>'

# 正则表达式
pattern = r'title="([^"]*)"'

# 使用 search 查找第一个匹配项
result = re.search(pattern, html)

# 严格限定中文：如果担心 title 中可能混入英文或数字，只想提取纯中文，可以将正则改为：  [\u4e00-\u9fa5] 是 Unicode 中常用汉字的范围。
pattern = r'title="([\u4e00-\u9fa5]+)"'

if result:
    print("提取结果:", result.group(1))
else:
    print("未找到 title 属性")


# 批量提取：如果有一段包含多行类似的 HTML 代码
# 建议将 re.search 替换为 re.findall，它会直接返回所有匹配结果的列表：

# results = re.findall(pattern, html_text)
# print(results)  # 输出: ['大众', '丰田', '本田', ...]
