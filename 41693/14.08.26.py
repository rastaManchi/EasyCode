import re


text = "Python is a popular programming language!"
pattern = r"Python"
# match = re.search(pattern, text)
# print(match.group())
match = re.match(pattern, text)
print(match)