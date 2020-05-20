import re
import requests

f = open('data/weather.csv', 'w', encoding='utf-8')


# url = 'http://www.naver.com'
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
received = requests.get(url)
# print(received.text)

# province = re.findall(r'<province>.+</province>', received.text)
# province = re.findall(r'<province>(.+)</province>', received.text)
# print(province)

locations = re.findall(r'<location wl_ver="3">(.+?)</location>', received.text, re.DOTALL)
# print(locations)
# print(len(locations))


# DOTALL : 개행문자 무시, 대상이 여러 줄에 걸쳐있을 때
# .+ : 탐욕적(greedy)
# .+? : 비탐욕적(non-greedy)


for loc in locations:
    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    # print(prov[0], city[0])

    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    # print(len(data))
    for datum in data:
        mode = re.findall(r'<mode>(.+)</mode>', datum)
        tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        wf = re.findall(r'<wf>(.+)</wf>', datum)
        tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
        tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
        rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)
        # print(mode)
        print(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0],
              file=f, sep=',')

f.close()
# 제주도 제주
# A02 2020-05-23 00:00 구름많음 16 24 30




# T.+A
# T.+?A


# T12A32A56A78T90A
# ^              ^      .+      그리디
# ^  ^        ^  ^      .+?     논-그리디

