# from wordcloud import WordCloud #导入词云模块
# words = open('result.txt',encoding='utf-8').read()#打开歌词文件，获取到歌词
# wordcloud = WordCloud(width=1000, #图片的宽度
#                       height=860,  #高度
#                       margin=2, #边距
#                       background_color='black',#指定背景颜色
#                       font_path='C:\Windows\Fonts\Sitka Banner\msyh.ttc'#指定字体文件，要有这个字体文件，自己随便想用什么字体，就下载一个，然后指定路径就ok了
#                       )
# wordcloud.generate(words) #分词
# wordcloud.to_file('cloud.jpg')#保存到图片

# coding:utf-8

import jieba
import matplotlib.pyplot as plt
#from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
text_from_file=open('result(translated and simplified).txt','r').read()
Word_spilt_jieba = jieba.cut(text_from_file,cut_all = False)
word_space = ' '.join(Word_spilt_jieba)
my_wordcloud = WordCloud(
    background_color='white', #设置背景颜色
    #mask=img,  #背景图片
    max_words = 200, #设置最大显示的词数
    stopwords = STOPWORDS, #设置停用词
    #设置字体格式，字体格式 .ttf文件需自己网上下载，最好将名字改为英文，中文名路径加载会出现问题。
    font_path = 'simkai.ttf',
    max_font_size = 100, #设置字体最大值
    random_state=50, #设置随机生成状态，即多少种配色方案
    ).generate(word_space)
#iamge_colors = ImageColorGenerator(img)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
my_wordcloud.to_file('cloud(Chinese_ver).jpg')