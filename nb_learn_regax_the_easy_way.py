# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import re

# +
# https://regex101.com/r/DOc5Nu/1

# 2.7 轉譯符號
# 由於正則表達式中有特殊字元，如果你想要在你的句子中抓出他們，你必須使用
# 轉譯符號
# Why not fat, cat, mat.?
print(re.findall("[f|c|m]at\.?", 'The fat cat sat on the mat.'))
print(re.findall("[f|c|m]at.?", 'The fat cat sat on the mat.'))
# -


