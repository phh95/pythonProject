import requests
from bs4 import BeautifulSoup
import bs4   # 这里直接引入 bs4 库，是为了判断后面返回的标签是不是 bs4 库定义的 tag 类型

# 我们还没有对函数的内部功能进行设计和实现，先写出函数的定义就可以

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"  # 异常的话，返回爬取失败的提示

# 提取 html 页面的关键数据，并填充到名为 ulist 的列表中
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        # 遍历 tbody 标签的儿子节点，不仅会返回标签节点，还会返回字符串节点
        # 为过滤掉字符串节点，我们要在这里做个判断
        # 如果 tr 标签不是 bs4 库定义的 tag 类型，就把它过滤掉
        if isinstance(tr, bs4.element.Tag):
            a = tr('a')  # 额外增加的一行代码，将所有的 a 标签存为一个列表类型
            tds = tr('td') # 将所有的 td 标签存为一个列表类型
            # ulist.append([tds[0].string,tds[1].string,tds[4].string])
            ulist.append([tds[0].text.strip(),a[0].string.strip(),tds[4].string.strip()])

def printUnivList(ulist, num):
    # 格式化输出
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))

# 定义了三个基本函数之后，书写主函数
def main():
    # 将大学信息放在一个列表中
    uninfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2021'

    # 分别调取三个步骤对应的函数
    html = getHTMLText(url)
    # 将提取后的信息放在 uninfo 变量中
    fillUnivList(uninfo, html)
    # 打印大学信息，只先列出 20 所学校的相关信息
    printUnivList(uninfo, 20)

main()