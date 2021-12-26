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

sent = '魯蛇有多魯，去吃滷肉飯'

# https://kknews.cc/zh-tw/education/59e9yll.html
# 看文章，看幾個例子


dag = t.get_DAG(sent)
route = {}
max_prob_res = t.calc(sent, dag, route)

display(
    dag,
    max_prob_res,
    list(t._Tokenizer__cut_DAG(sent))
)
# -


