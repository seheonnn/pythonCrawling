
# 별이삼샵 = 737628

import requests
import urllib
import os

headers = \
        {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
title = []
url_list = []

for page in range(1, 2, 1):
    url1 = 'https://comic.naver.com/webtoon/list?titleId=737628&weekday=sun&page={0}'.format(page)
    site = requests.get(url1, headers=headers) # headers 붙여서 요청(chrome headers)
    source_data = site.text


    count = source_data.count('onclick="nclk_v2(event,\'lst.title\',\'737628\',')

    for i in range(count):

        pos0 = source_data.find('onclick="nclk_v2(event,\'lst.title\',\'737628\',\'') + len('onclick="nclk_v2(event,\'lst.title\',\'737628\',\'')
        source_data = source_data[pos0:]

        post_pos0 = source_data.find('\')')
     
        post_url = source_data[:post_pos0] # post_url = 회차 번

        print(post_url) 
        
        pos1 = source_data.find('">') + len('">')
        pos2 = source_data.find('</a>')

        extract_data = source_data[pos1:pos2]
        source_data = source_data[pos2:]
        
        print(i+1, extract_data)

        title.append(extract_data)
        url_list.append(post_url)
        
k = 0        
for post_id in url_list:
    url2 = 'https://comic.naver.com/webtoon/detail?titleId=737628&no={0}&weekday=sun'.format(post_id)
##    print(url2)
    post = requests.get(url2, headers=headers)

    post_data = post.text
    img_pos0 = post_data.find('<div class="wt_viewer" style="background:#FFFFFF">') + len('<div class="wt_viewer" style="background:#FFFFFF">')
    post_data = post_data[img_pos0:]
    img_pos1 = post_data.find('</div>')
    post_data = post_data[:img_pos1]

    ##print(post_data)

    print(os.getcwd()) # 현재 경로 
    os.makedirs(f'/Users/hoseheon/Desktop/python_study/웹툰/{title[k]}') # 해당 경로에 폴더 생성

    img_count = post_data.count('<img src="')

    print('이미지 개수: ', img_count)
    for i in range(img_count):
        img_pos0 = post_data.find('<img src="') + len('<img src="')
        post_data = post_data[img_pos0:]
        
        img_pos1 = post_data.find('" title=""')
        img_src = post_data[:img_pos1]

        extend = img_src[img_src.rfind('.')+1:]
        print("이미지 링크 :", img_src)
        # file_name = '{0}{1}.{2}'.format(title[k], i+1, extend)
        file_name = f'./웹툰/{title[k]}/{title[k]}{i+1}.{extend}'
        
        try:
            #urllib.request.urlretrieve(img_src, file_name) # headers 없이 이미지 다운
            #headers 붙여서 이미지 다운
            ss = requests.get(img_src, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)
            file.close()
            
        except Exception as e:
            print('에러', e)
            

            
    print("\n")
    k+=1
