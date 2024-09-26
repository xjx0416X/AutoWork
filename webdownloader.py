import requests,os,time
from bs4 import BeautifulSoup as bs4


# url='https://www.qyy158.com/info/12782/2257673.html'
# key_word=input("请输入要下载的资源名：")
# params={"key_word":key_word}

def fetch_all_links(url,key_word,headers):
    params={"key_word":key_word}
    res=requests.get(url,params=params,headers=headers)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    links=[]
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    print(links)
    # for link in links:
    #     if link['href'].startswith('//video/'):
    #         print(link['href'])



# def download_manga(url,params):
#     res=requests.get(url,params=params)
#     soup=bs4.BeautifulSoup(res.text,'html.parser')
#     soup.select('')


# def download_video(url,params):
#     res=requests.get(url,params=params)

url='https://vidhub.tv/'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
key_words=['火影忍者','海贼王','名侦探柯南','一拳超人','钢铁侠','蜘蛛侠']
fetch_all_links(url,headers=headers)