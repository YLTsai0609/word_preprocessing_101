# -*- coding: utf-8 -*-
# # Unicode category
#
# [wiki](https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F#Unicode%E5%A4%84%E7%90%86)
#
# [Unicode與規則表示式](https://www.ithome.com.tw/voice/127180)
#
# 兩種字元編碼，在正則表達式中都稱為預定義字元類(Predefined character class)
#
#
# ASCII - 全世界第一版字元編碼，把數字轉成文字，只有英文(a to z, A to Z, 0 to (, .+-*&^%, ...)
#
# Unicode - 定義了近乎全世界的字元編碼，也被稱為萬國碼，由於全世界的文字實在太多，該編碼也不是使用數字來編碼，而是用**Unicode碼點(Code Point)**，例如 : `U+3000`
#
# # Unicode分類、文字、區塊
#
# 1. 在[Unicode規範中](https://www.unicode.org/reports/tr18/#General_Category_Property)，每個Unicode字元會隸屬於某個分類，例如å是個字母（Letter），可以使用`\pL`比對字母，若不想比對字母，則可以使用`\PL`，也可以進一步指定子屬性，例如，這時候必須加上`{}`，例如`\p{Lu}`表示大寫字母，`\p{Ll}`表示小寫字母
# 也可以加上ls，list的意思，例如`\p{lsL}`，也有冗長的寫法，例如`\p{Letter}`，不過這要看使用的程式語言而定，例如Java就不能寫`p{lsL}`，只能寫`\p{lsLetter}`
#
#
# 2. **有的文本中會使用多種語言來書寫，例如日文中有漢字、平假名、片假名等，然而有的語言只有一種文字，例如泰文**，Unicode將碼點群組為文字，可以使用lsHan，scirpt=Han或是sc=Han的方式來指定特性，例如`林.matches("\\p{lsHan}")`
#
#
# 3. 區塊 - Block
#
# pass
#
# # 規則表示式的一致性
#
# 原始正則表達式的預定義字元類，以ASCII符號為主，例如
#
# 空白 : `\s` -> `\t\n\x0B\f\r` -> 無法比對全型空白
#
# Unicode中提供了[建議相容特性](https://www.unicode.org/reports/tr18/#Compatibility_Properties)
# 在Java中有較好的支援
#
# 如果對JS, Python, Java的正則表達式感興趣，可以看[這裡](https://openhome.cc/Gossip/Regex/)

# +
# env : pixlake
# we focuing on pyspark dataframe processing
# documentation https://spark.apache.org/docs/2.4.0/api/python/pyspark.sql.html#pyspark.sql.DataFrame
# %load_ext autoreload
# %autoreload 2

# make you auto compeletion faster
# https://stackoverflow.com/questions/40536560/ipython-and-jupyter-autocomplete-not-working
# %config Completer.use_jedi = False

# +
import os
import sys
import re
from os.path import join
import pandas as pd
from pyspark.sql import SparkSession as Session
from pyspark.sql import DataFrame
from pyspark import SparkConf as Conf
from pyspark.sql import functions as F, Window as W, types as T
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

C = F.col

os.environ['PYSPARK_PYTHON'] = sys.executable
print(os.environ['PYSPARK_PYTHON'])
# -

conf = (Conf()
    .set('spark.sql.sources.partitionOverwriteMode', 'dynamic')
    .set('spark.driver.memory', '4g')
    .set('spark.driver.maxResultSize', '1g')
   )

spark = (Session
     .builder
     .appName('pyspark-regax-101')
     .master('local[2]')
     .config(conf=conf)
     .getOrCreate())

spark


# +
# s = "林"
# # print(s.encode('utf-8'))
# result = re.findall(r"\\p{Han}", s)
# result
# -


