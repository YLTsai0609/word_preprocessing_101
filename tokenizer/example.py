# -*- coding: utf-8 -*-
import os
print(os.listdir('.'))

from jieba_tw import jieba as jieba_tw

# !cat user_defined_dict.txt

# +
# The trie-tree daya structure

# 字典樹(前綴樹 prefix-tree) trie-tree，在 python 中可以以 dict 的方式儲存

#     Root  
#    /  |  \
#   魯 滷   必
#  /   |   /  \
# 蛇  肉  吃   勝
#     |         \
#    飯          客

t = jieba_tw.Tokenizer(dictionary='user_defined_dict.txt')
t.initialize()
print(
    dir(t),
    t.FREQ, # trie-tree
    t.total, # total words
    sep='\n\n'
)

# +
# leaves_total 是幹嘛的?

# 拿來計算機率用，因為斷詞 DAG 要符合最大機率

sent = '魯蛇很魯'

# 兩個 Reference
# https://kknews.cc/zh-tw/education/59e9yll.html
# http://hk.noobyard.com/article/p-pdgwdnep-t.html


# 0     1.     2.    3
# 魯---->蛇---->很---->魯
#  \---/


# {0: [0, 1], 1: [1], 2: [2], 3: [3]}


# route 從兩條路徑中找一條最大機率的路徑

# path 1 魯 / 蛇 / 很 / 魯 (2/5 x 1/5 x 1/5 x 1/5 = 2/625)
# path 2 魯蛇/很/魯 (1/5 x 1/5 x 1/5 = 1/125)
# 基本上有合併在一起的詞，很有機會變成最大路徑的詞

# 計算上如果路徑數過多，計算起來會慢，優化的計算方式是利用動態規劃

# 1. 計算可能句子 (DAG) 最大機率，可以拆成 過往所有字的機率 x 下一個字的機率 - 大問題可拆成重複小問題
# 2. 最大機率的句子，在過往所有字的機率中也必須是最大的 - 小問題存在最佳解

# 滿足1,2 可以用動態規劃來解題，就不用重複計算各個子句的機率結果
# 尚未優化前 Brute Force Time Complexity O(MN) - M為路徑數量，N為每個路徑平均詞數
# 優化過後 動態規劃 Time Complexity O(N) - 只需計算一次全部路徑，N為每個路徑的平均詞數
# 句子越長，時間差異越明顯

dag = t.get_DAG(sent)
route = {}

from math import log

def calc(sentence, dag, route, tokenizer):
    N = len(sentence)
    route[N] = (0, 0)
    logtotal = log(tokenizer.total)
    print(logtotal)
    for idx in range(N - 1, -1, -1):
        route[idx] = max( # 每個 idx 中的不同路徑中找一個最大機率的
        # 機率連乘換成對數 變成連加，因為要算機率，除以 total 變成減掉 logtotal
        # log(tokenizer.FREQ.get(sentence[idx:x + 1]) or 1) --> 取得詞頻，對於DAG中的每一條路，如果字典中沒有就是無機率
            (
                log(tokenizer.FREQ.get(
                    sentence[idx:x + 1])
                    or 1)
                - logtotal + route[x + 1][0], x) 
                for x in dag[idx] # 每個 idx 中的不同路徑
            )

#         route[idx] = max( # 每個 idx 中的不同路徑中找一個最大機率的
#         # 機率連乘換成對數 變成連加，因為要算機率，除以 total 變成減掉 logtotal
#         # log(tokenizer.FREQ.get(sentence[idx:x + 1]) or 1) --> 取得詞頻，對於DAG中的每一條路，如果字典中沒有就是無機率
#             (
#                 tokenizer.FREQ.get(sentence[idx:x + 1]) or 0 / tokenizer.total
#                  * route[x + 1][0], x)
#                 for x in dag[idx] # 每個 idx 中的不同路徑
#             )
    return route

max_prob_res = calc(sent, dag, route, t)

display(
    dag,
    max_prob_res,
    list(t._Tokenizer__cut_DAG_NO_HMM(sent))
)
# -






