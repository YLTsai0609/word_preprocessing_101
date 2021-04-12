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

# # Contents
# 1. Introduction to regular expressions
# 2. What is a regex pattern and how to compile one?
# 3. How to split a string separated by a regex?
# 4. Finding pattern matches using findall, search and match
# 4.1 What does regex.findall() do?
# 4.2 regex.search() vs regex.match()
# 5. How to substitute one text with another using regex?
# 6. Regex groups
# 7. What is greedy matching in regex?
# 8. Most common regular expression syntax and patterns
# 9. Regular Expressions Examples
# 10. Practice Exercises
# 11. Conclusion
#

import re
regex = re.compile('\s+')
# \s match 任何空白字元
# # + match 一個獲釋多個以上

# +
# 3. How to split a string separated by a regex?
# Let’s consider the following piece of text.

text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""


sol_1 = re.split('\s+', text)
sol_2 = regex.split(text)
print(sol_1, sol_2, sep='\n')

# hint
# 使用re.split 方法 - pattern簡單時
# 把regex物件先設定好, 在call split方法 - pattern複雜時
# split用於分割字串時

# +
# 4. Finding pattern matches using findall, search and match
# Let’s suppose you want to extract all the course numbers, that is, the numbers 101, 205 and 189 alone from the above text. How to do that?

print(text)
print('-' * 60)
regex_num = re.compile('\d+')
regex_num.findall(text)

# hint \d mean digit
# # + means 一個或多個, * means 0個或多個
# findall method 所有發生的情況, 加到list, 用於過濾字串


# +
# 4.2 re.search() vs re.match()
# As the name suggests, regex.search() searches for the pattern in a given text.

# But unlike findall which returns the matched portions of the text as a list, regex.search() returns a particular match object that contains the starting and ending positions of the first occurrence of the pattern.

# Likewise, regex.match() also returns a match object. But the difference is, it requires the pattern to be present at the beginning of the text itself.

text2 = """COM    Computers
205 MAT   Mathematics 189"""

regex_num = re.compile('\d+')
s = regex_num.search(text2)
print('Starting Position: ', s.start())
print('Ending Position: ', s.end())
print(text2[s.start():s.end()])
print(dir(s))
print(s.group())

# hint
# search, 從字串頭搜尋到字串尾, match出205,
# 從group取出
# 並且search物件中有方法可以call
# -

m = regex_num.match(text2)
print(m)

# +
# 5. How to substitute one text with another using regex?
# To replace texts, use the regex.sub().

# Let’s consider the following modified version of the courses text. Here I have added an extra tab after each course code.

text = """101   COM \t  Computers
205   MAT \t  Mathematics
189   ENG  \t  English"""
print(text)


# replace one or more spaces with single space
sol1 = re.sub('\s+', ' ', text)
regex = re.compile('\s+')
sol2 = regex.sub(' ', text)
print(sol1, sol2, sep='\n')
# -

# get rid of all extra spaces except newline
regex = re.compile('(?!\n)\s+')
print(regex.sub(' ', text))
# hint
# ?!\n 遇到\n則保留
# ?! 否定

# +
# 6. Regex groups
# Regular expression groups is a very useful feature that lets you extract the desired match objects as individual items.

# Suppose I want to extract the course number, code and the name as separate items. Without groups, I will have to write something like this.

text = """101   COM   Computers
205   MAT   Mathematics
189   ENG    English"""

# extract all course numbers
print(re.findall('[0-9]+', text))

# extract all course codes
print(re.findall('[A-Z]{3}', text))

# extract all course names

print(re.findall('[A-Za-z]{4,}', text))

# 符合0個以上 *
# 符合1個以上 +
# 符合0個或1個 ?
# 符合特定數目 {n}
# 符合特定數目以上 {n,}
# 符合特定數目以下 {,n}
# 符合特定數目之間 {n,p}

# -

# define the course text pattern groups and extract
course_pattern = '([0-9])\s*([A-Z]{3})\s*([A-Za-z]{4,})'
re.findall(course_pattern, text)
# hint
# 找出pattern, 用\s*切分開, 放在turple,list中。

# +
# 7. What is greedy matching in regex?
# The default behavior of regular expressions is to be greedy. That means it tries to extract as much as possible until it conforms to a pattern even when a smaller part would have been syntactically sufficient.

# Let’s see an example of a piece of HTML, where I want to retrieve the HTML tag.

text = "< body>Regex Greedy Matching Example < /body>"
print(re.findall('<.*>', text))

# hint 預設搜尋為greddy搜尋，能搜尋多少，就搜尋多少
# 原本預期 抓取出 < body>這個tag
# 結果全抓, <body ..........< /body>
# regex . means 任何一個字元, 除了\n


# +
# 只想抓1個, 或是幾個 lazy-matching
re.findall('<.*?>', text)

# 使用regex-group取出第一個

s = re.search('<.*?>', text)
print(type(s), s.group(), sep='\n')
# hint
# reg-group可以抓出其中幾個
# re.search return a SER_Match object
# -

# <img src = './images/regex1.png'>
# <img src = './images/regex2.png'>

# 9.1. Any character except for a new line
text = 'machinelearningplus.com'
print(re.findall('.', text)) # match任何一個字元但不包含\n
print(re.findall('(...)', text))  # match 任何三個字元但不包含\n

# 9.2. A period
text = 'machinelearningplus.com'
text2 = 'abcabcabcabcabc'
print(re.findall('\.', text)) # match 點
print(re.findall('[^\.]', text)) # match 不是點

# 9.3. Any digit
text = '01, Jan 2015'
print(re.findall('[0-9]{2,}', text)) # match 任意數字0-9，兩個以上
print(re.findall('\d+', text)) # match任意數字，1個以上

# 9.4. Anything but a digit
text = '01, Jan 2015'
print(re.findall('\D+', text)) # match任意非數字，1個以上

# 9.5. Any character, including digits
text = '01, Jan 2015'
print(re.findall('[0-9A-Za-z]+', text)) # match任意0-9, A-Z, a-z, 一個以上(不包含空白，所以就被切開了)
print(re.findall('\w+', text)) # match任意字元，(不包含空白，所以就被切開了)

# 9.6. Anything but a character
text = '01, Jan 2015'
print(re.findall('\W+', text)) # match 任意非字元，所以就match到, 空白等

# 9.7. Collection of characters
text = '01, Jan 2015'
print(re.findall('[a-zA-Z]+', text)) # match任意a-zA-Z，以個以上

# 9.8. Match something upto ‘n’ times
text = '01, Jan 2015'
print(re.findall('\d{4}', text)) # match 任意數字，連續出現4個
print(re.findall('\d{2,4}', text)) # match 任意數字，連續出現2~4個

# 9.9. Match 1 or more occurrences
print(re.findall(r'Co+l', 'So Coooooooool'))
# r表示為非轉譯之原始字符，及忽略反斜槓

# 9.10 轉譯符號
# 必須用\轉譯
print(re.findall(r'\section', '\section')) # doesn't work
print(re.findall(r'\\section', '\section')) # will work
print(re.findall('\section', '\section')) # will work


# +
# # 9.12. Match word boundaries
# Word boundaries \b are commonly used to detect and match the beginning or end of a word. That is, one side is a word character and the other side is whitespace and vice versa.

# For example, the regex \btoy will match the ‘toy’ in ‘toy cat’ and not in ‘tolstoy’. In order to match the ‘toy’ in ‘tolstoy’, you should use toy\b

re.findall(r'\btoy\b', 'play toy broke toys') # match toy單詞，前面和後面都以word boundary隔開


# +
# 10. Practice Exercises
# 1. Extract the user id, domain name and suffix from the following email addresses.

emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

# match 任意字元，1個以上，小老鼠@任意字元一個以上，點.，任意A-Za-z，2到4個
pat = re.compile(r'(\w+)@(\w+).([A-Za-z]{2,4})')
re.findall(pat, emails)

# +
# 2. Retrieve all the words starting with ‘b’ or ‘B’ from the following text.

text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""
print(re.findall(r'\bB\w+', text, flags=re.IGNORECASE))

# -

# 3. Split the following irregular sentence into words
sentence = """A, very   very; irregular_sentence"""
" ".join(re.split(r'[;,_\s+]', sentence))
# hint :,_超過一個空白等

# +
# 4. Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''


def cleaning_text_eng(text):
    '''
    英文的清理和中文的清理會不同
    '''
    tweet = re.sub(r'http\S+\s*', '', text)  # URLs http + 非空白一個以上 + 空白0個以上
    tweet = re.sub(r'RT|cc', '', tweet)  # RT and CC
    tweet = re.sub(r'#\S+', '', tweet)  # hashtag # + 非空白字元
    tweet = re.sub(r'@\S+', '', tweet)  # hashtag @ + 非空白字元
    tweet = re.sub(r"""[%s!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]""",
                   '',
                   tweet)  # 標點符號
    tweet = re.sub(r'\s+', ' ', tweet)  # 額外的空白字元
    tweet = tweet.strip()
    return tweet


clean_tweet = cleaning_text_eng(tweet)
clean_tweet
# -

import requests
r = requests.get(
    "https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
print(r.text)  # html text is contained here


def split_from_tag(html_text):
    return re.findall(r'<.*>(.+)</.*>', html_text)


split_from_tag(r.text)

# extract P
r = requests.get(
    "https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
print(r.text)  # html text is contained here


def split_from_tag(html_text):
    return re.findall(r'<P>(.+)</P>', html_text)


split_from_tag(r.text)

text = """python清理數據，僅保留字母，數字，中文，在前面加'ur'
          u的意思是表明後面有Unicode字符，漢字的範圍為'\u4e00-\i9fa5
          這個是用Unicode表示的"""


def remove_punctuation(text):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    result = rule.sub('', text)
    return result


remove_punctuation(text)

# print(text)


# extract img source in html plain text
# https://stackoverflow.com/questions/1028362/how-do-i-extract-html-img-sources-with-a-regular-expression/1028370
# regax 解釋
# 擷取以`<img`
# 開頭配對一個或是多個 []+
# 並且非右鍵號 [^>]+
# 直到遇到src="
# 拿取裡面的
with open('data/webpage_1.txt') as f:
    text = f.read()
# print(text)
# add the other extension(like png, tiff, ...)
text += '<img alt="IMG_5208.png" src="https://pic.pimg.tw/happy78/1528543947-685380499_n.png" title="IMG_5208.png">'
text += '<img alt="IMG_5208.png" src="https://pic.pimg.tw/happy78/1528543947-685380499_n.tiff" title="IMG_5208.png">'
pat = re.compile('<img[^>]+src="([^">]+(jpg|png))"')
pat.findall(text)
# # Prefix
#


# https://blog.csdn.net/u013177568/article/details/62432737
# r for raw
# u for unicode


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
# Unicode - 定義了近乎全世界的字元編碼，也被稱為萬國碼，由於全世界的文字實在太多，該編碼也不是使用數字來編碼，而是用Unicode碼點(Code Point)，例如 : `U+3000`
#
# Unicode分類、文字、區塊
#
# 在

s = "å"
# print(s.encode('utf-8'))
result = re.findall(r"å",s)
result


