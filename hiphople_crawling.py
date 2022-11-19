import requests
import urllib
headers = \
        {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
title = []
url_list = []
for page in range(1, 2, 1):
##    print("page ", page)
    url1 = 'https://hiphople.com/kboard?page={0}'.format(page)
    site = requests.get(url1, headers=headers) # 
    source_data = site.text

    
    hot_count = source_data.count('화제의 글</span>')
    for i in range(hot_count):
        url_hot = source_data.find('화제의 글</span>') + len('화제의 글</span>')
        source_data = source_data[url_hot:]

    count = source_data.count('<td class="categoryTD"><span class="category" style="')
       
    for i in range(count):
        url_str3 = source_data.find('<td class="no">') + len('<td class="no">')
        source_data = source_data[url_str3:]

        url_str2 = source_data.find('<a href="/kboard/') + len('<a href="/')
        source_data = source_data[url_str2:]
        
        url_end = source_data.find('">')
        post_url = source_data[:url_end]

        pos0 = url_end + len('">')
        pos1 = source_data.find('</a>')
        extract_data = source_data[pos0:pos1]

##        url_list.append(extract_data)
        url_list.append(post_url)
        title.append(extract_data)

k = 0
for post_id in url_list:
    print(k+1, title[k])
    url2 = 'https://hiphople.com/{0}'.format(post_id)
    print(url2)
    post = requests.get(url2, headers=headers)
    post_data = post.text

    pos5 = post_data.find('id="flagArticle">')
    post_data = post_data[pos5:]

    pos6 = post_data.find('<ul>')
    post_data = post_data[:pos6]
    
    
    img_count = post_data.count('img src="//img.hiphople.com/files/attach/images')
    print('이미지개수 : ', img_count)
    for i in range(img_count):
        post_pos1 = post_data.find('img src="//img.hiphople.com/files/attach/images') + len('img src="//img.hiphople.com/files/attach/images')
        post_data = post_data[post_pos1:]
        post_pos2 = post_data.find('" alt')
        
        post_extract = post_data[:post_pos2]

        img_src = 'http://img.hiphople.com/files/attach/images' + post_extract

        extend = img_src[img_src.rfind('.')+1:]
        print("이미지 링크 :", img_src)
        file_name = '{0}{1}.{2}'.format(title[k], i+1, extend)
        file_name = f'{title[k]}{i+1}.{extend}'
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
