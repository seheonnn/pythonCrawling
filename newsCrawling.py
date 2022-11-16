import requests

headers = \
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

for date in range(20221022, 20221015, -1):
    pre_site = 'wwww' #이전 사이트 내용
    print(date)
    for page in range(1, 10, 1):
        url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=731&mid=shm&sid1=105&date={0}&page={1}'.format(date, page)
        site = requests.get(url, headers=headers)
        source_data = site.text

        if pre_site == site.text:
            break

        pre_site = site.text

        count = source_data.count('height="72" alt="')

        print("page ", page)
        for i in range(count):
            pos1 = source_data.find('height="72" alt="')+len('height="72" alt="')
            source_data = source_data[pos1 : ]

            pos2 = source_data.find('"')
            extract_data = source_data[ : pos2]

            source_data = source_data[pos2+1 : ]
            print(i+1, extract_data)
    
