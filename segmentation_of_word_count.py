import re
import sys

def read_file(): # 讀取一個文本，統計文本中單詞的出現次數
    with open('/Users/wan/segmentation_of_word/bodyfile.txt', 'r', encoding='utf-8') as f:
        word = []  # 空陣列用来儲存文本中的單詞
        for word_str in f.readlines():  #分行讀取文本，且返回的是一個列表，每行的值當列表中的一個元素：
            word_str = word_str.replace(',', '') #去除原檔空格
            word_str = word_str.strip() #strip去除每行字符中的空白字符
            word_list = re.split('，|。|；|？',word_str)#對當行字符串通過逗號進行分割，回傳list
            word.extend(word_list) #把分割後的lust内容，加到word陣列裡
        print("Finish readfile() sentence count is {}".format(len(word)))
        return word
 
 
def clear_account(lists):
    count_dict = {} #定義一空字典，用來存放分割後的詞和出現次數
    # count_dict = count_dict.fromkeys(lists) 
    # word_list1 = list(count_dict.keys()) #取出字典中的key，放到word_list1
    word_list1 = lists
    for word in word_list1:
        if word in count_dict :
            count_dict[word] += 1
        else :
            count_dict[word] = 1
    return count_dict

"""
    #計算句子出現的次數,並存入count_dict字典中
    for i in word_list1:
        count_dict[i] = lists.count(i)#使用count計算出現次數
    return count_dict
"""
 
 
def sort_dict(count_dict):
    if '' in count_dict:
        del count_dict[''] #刪除字典中''單字
    my_dict = sorted(count_dict.items(), key=lambda d:d[1], reverse=True)  # 臨時參數d[1]是用value排序
    my_dict = dict(my_dict) #轉成字典
    return my_dict
 
 
def main(my_dict):
    bodyfile = sys.stdout 
    sys.stdout = open('ans_file.txt','w', encoding = 'utf-8') 
    i = 0
    for x, y in my_dict.items():
        print('（%s, %s）' %(x,y) )
        i += 1
    sys.stdout.close()
    sys.stdout = bodyfile
    print("len of dictionary is {}".format(i))
main(sort_dict(clear_account(read_file())))
