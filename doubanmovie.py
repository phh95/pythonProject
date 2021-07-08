# 引入三个库

import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint

# 构造分页数字列表
page_indexs = range(0,250,25)
print(list(page_indexs))

def download_all_htmls():
    """下载所有列表页面的HTML"""
    htmls = []
    for idx in page_indexs:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91',
            'cookie': ''
        }
        print("craw html:", url)
        r = requests.get(url,headers=headers,timeout=10)
        if r.status_code != 200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls

# 执行爬取
htmls = download_all_htmls()
print(htmls[0])

# 解析 HTML 得到数据
def parse_single_html(html):
    """解析单个HTML，得到数据"""
    soup = BeautifulSoup(html,'lxml')  # html.parser
    article_items = (
        soup.find("div",class_= "article")
            .find("ol",class_= "grid_view")
            .findall("div",class_= "item")
    )
    datas = []
    for article_item in article_items:
        rank = article_item.find("div",class_="pic").find("em").get_text()
        info = article_item.find("div",class_="info") #下面提取的信息比较多
        title = info.find("div",class_="hd").find("span",class_="title").get_text()
        stars = (
            info.find("div",class_="bd")
                .find("div",class_="star")
                .findall("span")
        )
        rating_star = stars[0]["class"][0]  # 几颗星
        rating_num = stars[1].get_text()  # 打几分
        comments = stars[3].get_text()  # 有多少人参与评分

        datas.append({
            "rank": rank,
            "title": title,
            "rating_star": rating_star.replace("rating","").replace("-t",""),
            "rating_num": rating_num,
            "comments": comments.replace("人评价","") # 把网页带有的"人评价"替换成空白的
        })
    return datas

# 执行所有的 HTML 页面的解析

all_datas = []
for html in htmls:
    all_datas.extend(parse_single_html(html))




