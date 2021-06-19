import jieba  # 分词模块
import wordcloud
# import imageio
# py = imageio.imread('xx.png') # 自定义词云图的形状

f = open('弹幕.txt',encoding='utf-8')
txt = f.read()  # 读取文件
# print(txt)

txt_list = jieba.lcut(txt)  # 使用 jieba 分词得到的结果为列表
print(txt_list)

# 列表转换为字符串，用到 join 方法

string = ' '.join(txt_list)
print(string)

# 词云图设置

wc = wordcloud.WordCloud(
    width = 1000,
    height = 700,
    background_color = 'white',
    # mask = py,
    font_path = 'msyh.ttc',  # 字体为微软雅黑，Windows 系统使用这个字体
    # font_path= 'PingFang.ttc',  # 字体为苹方，苹果系统使用这个字体
    scale = 15,
    stopwords = {'Microsoft YaHei'},  # 设定停止词
    # contour_width = 5,  # 轮廓的宽度
    # contour_color = 'red',  # 轮廓的颜色
)

# 输入文字内容

wc.generate(string)

# 导出图片

wc.to_file('danmu_cloud02.png')