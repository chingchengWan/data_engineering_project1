# !/usr/bin/python
# coding:utf-8
import re
import sys


def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[0].partition(b))[0][:]

file = open('/Users/wan/segmentation_of_word/ettoday.rec','r', encoding = 'utf-8', errors = 'ignore')
paragraph = file.readlines()

new_sents = [] 
bodyfile = sys.stdout 
sys.stdout = open('body_file.txt','w', encoding = 'utf-8') 

for p in paragraph:
    sent = get_str_btw(p, '@body:', '@') 
    print(sent)
    new_sents.append(sent) 

sys.stdout.close() 
sys.stdout = bodyfile 

file.close() 
