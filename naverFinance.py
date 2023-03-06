# beautiful soup 이용
import requests
from bs4 import BeautifulSoup

for page in range(1, 8):
    url = f'https://finance.naver.com/sise/theme.naver?&page={page}'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

    s = requests.get(url, headers=headers)

    soup = BeautifulSoup(s.text, 'html.parser')


    # data = {
    #     '테마명' : [],
    #     '전일대비' : [],
    #     '최근3등락률(평균)' : [],
    #     'urls' : []
    # }

    r = soup.find_all(class_='col_type1')
    del r[0]
    updown = soup.find_all(class_='number col_type2')
    updown_average = soup.find_all(attrs={'class': 'number col_type3'})

    for i in range(len(r)):
        rr = r[i].text
        uu = updown[i].text.strip()
        aa = updown_average[i].text.strip()
        urls = r[i].find_all('a')[0]['href']

        url2 = 'https://finance.naver.com' + urls
        s2 = requests.get(url2, headers=headers)
        soup2 = BeautifulSoup(s2.text, 'html.parser')

        print('=============== ' + rr + ' 전일 대비 : ' + uu + ' 최근 3일 등락(평균) : ' + aa + ' url : ' + url2)
        r2 = soup2.find_all(attrs={'onmouseover':'mouseOver(this)'})
        for j in range(len(r2)):
            n = r2[j]('td')[0].text
            ud = r2[j]('td')[4].text.strip()

            print(n)
            print(ud)


        # # pandas에 추가
        # data.get('테마명').append(rr)
        # data.get('전일대비').append(uu)
        # data.get('최근3등락률(평균)').append(aa)
        # data.get('urls').append(url2)

    # df = pd.DataFrame(data) # index추가할 수 있음
    # print(df)
