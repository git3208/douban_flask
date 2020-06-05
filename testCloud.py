#-*- codeing = utf-8 -*-
#@Time: 2020/6/3 15:59
#@Author: Hiwsi
#@File: testCloud.py
#@Software: PyCharm

import jieba #分词
from matplotlib import pyplot as plt #绘图，数据可视化
from wordcloud import WordCloud      #词云
from PIL import Image        #图片处理
import numpy as np                   #矩阵运算
import sqlite3                       #数据库


conn=sqlite3.connect('movie.db')
cur=conn.cursor()

sql='select about from movie250'

data=cur.execute(sql)
text=""
for item in data:
    text+=item[0]
word = jieba.cut(text)
data = " ".join(word)
print(data)

image=Image.open('./static/assets/img/mask.png') #打开一张图片

image_array=np.array(image) #将图片转为图片数组

#构建词云
wc = WordCloud(
    background_color='white',
    mask=image_array,
    font_path='msyh.ttc'
)
wc.generate_from_text(data)

fig=plt.figure(1)

plt.imshow(wc)
plt.show()

wc.to_file('./static/assets/img/word.jpg')



