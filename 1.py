import jieba
import pandas as pd

 # 保留字
jieba.load_userdict('saveW/save4.txt')  # 保留字

# 文字檔
file = 'page/part4.txt'
txt = open(file, 'r', encoding='utf-8').read()

words = jieba.lcut(txt ,cut_all=False)


counts = {}
delt = [] 
for word in words:
    if len(word) == 1:  # 不計算單個詞
        delt.append(word) # 將單一詞彙加入 delt = [] list
        continue
    else:
        counts[word] = counts.get(word, 0 ) +1

# 查看字典
# print(counts)
# 查看鍵質
# print(counts.keys())


delt = ['中國','不要','江明洋','林之晨','張秉霖', '自己','可以','Umbo','CV','校友','10','470','12','100']
for deword in delt:
    del(counts[deword])

# 文字清單，統計數量多到少
item = list(counts.items())
item.sort(key=lambda x: x[1], reverse=True)    # 大到小排序

print(len(item))

pan_1 = {
    "word_name" : [],
    "use_num" : []
}

for words in counts:
    pan_1['word_name'] = counts.keys()
    pan_1['use_num'] = counts.values()

df_1 = pd.DataFrame(pan_1)

df_1 = df_1.sort_values(
       by="use_num",
       ascending=False)

# print(pan_1)

df_1.to_csv("part.csv",encoding='utf_8_sig') # utf_8_sig

# print(word)
# print('/'.join(words))
