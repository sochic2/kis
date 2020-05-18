# Day_01_01_re.py

# print("Hello, ML!!")

import re

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

# print(db)

# r : raw
number = re.findall(r'[0-9]', db)
print(number)
print(re.findall(r'[0-9]', db))
print(re.findall(r'\d', db))

# 숫자 묶어서 검색하기
print(re.findall(r'[0-9]+', db))

# 문제
# db에 포함된 숫자 문자열을 추출해서 숫자로 변환하세요.
print(list(int(_) for _ in re.findall(r'[0-9]+', db)))

# 문제
# 이름만 출력하세요.
print(re.findall(r'[A-Z|a-z]+', db))
print(re.findall(r'[A-Za-z]+', db))
print(re.findall(r'[A-Z][a-z]+', db))

# 문제
# T로 시작하는 이름만 출력하세요.
# T로 시작하지 않는 이름만 출력하세요.
print(re.findall(r'T[a-z]+', db))
print(re.findall(r'[ABCDEFGHIJKLMNOPQRSUVWXYZ][a-z]+', db))
print(re.findall(r'[A-SU-Z][a-z]+', db))