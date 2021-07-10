import requests
import json

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 40)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "抓取失败"

def printUnivList(ulist,html,num):
    """提取 html 网页内容中前 num 名大学信息到 ulist 列表中"""
    data = json.loads(html)  # 	将 JSON 字符串解码为 Python 对象，返回的是列表
    # 提取数据 rankings 包含的内容
    content = data['data']['rankings']

    # 把学校的相关信息放到 ulist 里面
    for i in range(num):
        index = content[i]['rankOverall']
        name = content[i]['univNameCn']
        score = content[i]['score']
        ulist.append([index,name,score])

    # 格式化输出，打印前 num 名的大学
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}" # 生成一个输出模板的变量，{1:{3}^10} 中的 {3} 代表取 format 第三个参数
    print(tplt.format("排名","学校名称","总分",chr(12288))) # chr(12288) 代表中文空格
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

# 定义一个主函数，调用上面定义的函数
def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2021"
    html = getHTMLText(url)
    printUnivList(uinfo, html, 30)

main()

# 本代码参考：https://blog.csdn.net/Dina_p/article/details/115606100