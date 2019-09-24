# !/usr/bin/python
# coding:utf-8
import re
import sys


def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[0].partition(b))[0][:]

file = open('/Users/wan/gapminder-api/ettoday.rec','r', encoding = 'utf-8', errors = 'ignore') #開啟檔案,須以r讀模式
paragraph = file.readlines()
#paragraph = str(paragraph)



new_sents = [] #空列表用来儲存body內容
bodyfile = sys.stdout #儲存原始的輸出對象
sys.stdout = open('bodyfile.txt','w', encoding = 'utf-8') #重定向所有的寫入内容到 bodyfile.txt 文件

for p in paragraph:
    sent = get_str_btw(p, '@body:', '@') #到 bodyfile.txt 文件中
    print(sent)
    new_sents.append(sent) #append()方法在列表尾添加新的對象

sys.stdout.close() #關閉bodyfile.txt 文件
sys.stdout = bodyfile #將print命令的結果回傳给控制台

file.close() 