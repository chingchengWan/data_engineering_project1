import re
import sys

def read_file(): 
    with open('/Users/wan/segmentation_of_word/bodyfile.txt', 'r', encoding='utf-8') as f:
        word = [] 
        for word_str in f.readlines():  
            word_str = word_str.replace(',', '') 
            word_str = word_str.strip() 
            word_list = re.split('，|。|；|？',word_str)
            word.extend(word_list) 
        print("Finish readfile() sentence count is {}".format(len(word)))
        return word
 
 
def clear_account(lists):
    count_dict = {} 
    # count_dict = count_dict.fromkeys(lists) 
    # word_list1 = list(count_dict.keys()) 
    word_list1 = lists
    for word in word_list1:
        if word in count_dict :
            count_dict[word] += 1
        else :
            count_dict[word] = 1
    return count_dict
 
 
def sort_dict(count_dict):
    if '' in count_dict:
        del count_dict[''] 
    my_dict = sorted(count_dict.items(), key=lambda d:d[1], reverse=True)
    my_dict = dict(my_dict) 
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
