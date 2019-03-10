import requests #导入requests库
from lxml import etree
from lxml import html
import csv

movieUrls =[]
urls=[]
start_url='https://www.dygod.net/html/gndy/dyzz/index.html'
def url_link():                                  #定义函数    
    urls.append(start_url)
    for k in range(1,3):
        url='https://www.dygod.net/html/gndy/dyzz/index_'+str(k)+'.html'
        urls.append(url)
        
def html_heat(urls):                                  #定义函数    
    for index4,index3 in enumerate(urls):
        heat=requests.get(index3)                     #下载网站内容
        heat.encoding =heat.apparent_encoding#解决乱码
        soup1=html.fromstring(heat.text)
        news=soup1.xpath('//*[@class="ulink"]/@href')
        for j in news:
            m='https://www.dygod.net/'+j
            movieUrls.append(m)

def movie(movieUrls):                                  #定义函数
    for index1,index in enumerate(movieUrls):
        heat1=requests.get(index)                     #下载网站内容
        heat1.encoding =heat1.apparent_encoding#解决乱码
        soup2=html.fromstring(heat1.text)
        result2=soup2.xpath('//table[2]//tbody//tr//td//a/@href')
        result3=soup2.xpath('//div/div[3]/div/div[4]/div[1]/h1/text()')
        for link in result2:
            for name in result3:
                item={                          #将获取的结果存储为字典
                    "name":name,
                    "link":link
                }
                save_result(item)               #每次获取一个结果后，存储一次
                item.clear()                    #存储后清空字典，为下次存储做准备

def save_result(item):                      #存储结果
    with open('dytt.csv','a',newline='',encoding='utf-8') as csvfile:   #打开一个csv文件，用于存储
        fieldnames=['name','link']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow(item)

def main():                                          #主程序
    with open('dytt.csv','a',newline='') as csvfile:   #写入表头
        writer=csv.writer(csvfile)            
        writer.writerow(['name','link'])
    headers = {
    'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',}
    url_link()
    html_heat(urls)
    movie (movieUrls)
if __name__ == '__main__':     #运行主程序
    main()