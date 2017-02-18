# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import SinaNews




def main():
    #主函数,抓取新浪新闻
    url='http://news.sina.com.cn/china/'
    ct=requests.get(url)
    ct.encoding="UTF-8"
    #构建soup对象
    manSoup=BeautifulSoup(ct.text,"html.parser")
    #获取新闻列表
    newsItems=manSoup.select(".news-item")
    #遍历新闻
    for item in newsItems:
        h2=item.select("h2")
        if(len(h2)>0):
            a=h2[0].select("a")[0]
            a_text=a.text;
            a_href=a["href"];
            print("标题：",a_text,"\r\n链接：",a_href,"\r\n")
            #抓取内容详情
            print("抓取内容详情\r\n")
            newinstance=SinaNews.getnews(a_href)
            print("标题：",newinstance.title,"\r\n发布时间：",newinstance.publishtime,"\r\n内容：",newinstance.content)





main()


