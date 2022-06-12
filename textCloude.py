# import jieba.posseg as pseg
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt 
import random



# jieba 中文 斷句
# words = jieba.cut(text)
# print(jieba.lcut(text)) 

jieba.load_userdict('saveW/save4.txt')  # 保留字

file = 'page/part2.txt'
txt = open(file, 'r', encoding='utf-8').read()



counts = {}


words = jieba.lcut(txt ,cut_all=False)


delt = [] 

# 計算詞語出現次數
for word in words:
    if len(word) == 1:  # 不計算單個詞
        delt.append(word) # 將單一詞彙加入 delt = [] list
        continue
    else:
        counts[word] = counts.get(word, 0 ) +1

# print(delt)


# 刪除字眼

delt1 = ['中國','不要','江明洋','林之晨','張秉霖', '自己','回覆','可以','顯示']
# for deword in delt:
#     del(counts[deword])


# 文字清單，統計數量多到少
item = list(counts.items())
item.sort(key=lambda x: x[1], reverse=True)    # 大到小排序

# 迴圈 顯示清單
for i in range(30):
    word, counts = item[i]
    print("{0:<5}{1:>5}".format(word, counts))


# 設定雲圖函數
img_back = plt.imread('img/AI2.jpg')
wc = WordCloud(background_color= 'black',
                font_path='msyh.ttc',   # 中文設置
                scale=5,  # 比例放大
                mask=img_back,
                max_words=2500,  # 數字量
                max_font_size=100, # 設置字體最大大小
                stopwords = delt + delt1  # 停用詞句
                
                )

# 定義色彩funtion
def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)



resuq =' '.join(words)
# print(resuq)

wc.generate(resuq)
# 產生雲圖
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
plt.axis('off')
plt.savefig("ok.png",dpi=400)  # 存取
plt.show()

