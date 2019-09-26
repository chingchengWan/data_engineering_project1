# Data Engineering Project1

###### tags: `Data Engineering`



### sys(system)
用來處理Python執行時配置以及資源，從而可以與當前程式之外的系統環境互動，如：Python直譯器。

#### sys函式庫中常見的函式變數
函式           |  說明                        
-----------|:-------------------------------
sys.path  | 查詢所在目錄的目錄名列表 
sys.argv |使用sys.argv可以實現程式在外部傳遞引數   |
sys.stdin/sys.stdout/sys.stderr  | stdin、stdout 以及stderr 變數包含與標準I/O流對應的物件

## open()函式檔案開啟、讀、寫操作
```python=
file = open('/Users/wan/gapminder-api/ettoday.rec','r', encoding = 'utf-8', errors = 'ignore') 
paragraph = file.readlines()
```
利用`open()`開啟檔案，並讀檔，其中'r'讀模式、'w'寫模式、'a'追加模式、'b'二進位制模式、'+'讀/寫模式。
其中`readlines()`函式用於讀取所有行(直到`EOF`)並返回list，該list可以由 Python 的 for... in ... 結構進行處理，如果碰到`EOF` 則返回空字串。


## 獲取兩個字元間的內容
```python=
def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[0].partition(b))[0][:]
    
new_sents = [] 
bodyfile = sys.stdout 
sys.stdout = open('bodyfile.txt','w', encoding = 'utf-8') 

for p in paragraph:
    sent = get_str_btw(p, '@body:', '@') 
    print(sent)
    new_sents.append(sent) 
    
sys.stdout.close() 
sys.stdout = bodyfile 
```
`new_sents = []` 是初始空串列準備用來儲存 *body* 的內容，並建立一個`bodyfile.txt`儲存原始的輸出對象並將所有輸出資料存進該檔案中。
在`for`迴圈中宣告一個變數`p`從`paragraph`裡抓資料，資料範圍是整個 *body* 內容並存進變數`sent`中，利用`append()`函式在列表尾添加新的對象。
`sys.stdout.close()` 關閉`bodyfile.txt` 文件，`sys.stdout = bodyfile` 將print命令的結果回傳給控制台。

如此一來，就能只提取對我們有幫助的內容來進行進一步的斷詞與計算次數。
### 串列(list)

#### 串列(list)_新增
函式          |  說明                        
-----------|:-------------------------------
list.append(item)  | 在串列最後增加項⽬
list.extend(list) |在串列最後增加串列
list.insert(index, item)  | 指定位置插入項目
#### 串列(list)_搜尋與排序
函式           |  說明                        
-----------|:-------------------------------
list.index(value)  | 找出第⼀一次出現的位置 
'value' in list |判斷值是否在串列中(回傳true or false)
list.sort() /  sorted(list) | 根據值的內容來排序


____________________________________
<!--
```python=
import re
import sys
```
-->

### 正規運算式 re
正規運算式 (regular expression) 常用在對文本進行解析，例如做網路爬蟲去爬網路上的 HTML 文件，從中取得所欲取得之資訊，或是針對文件檔案進行處理。 
Python 中做正規運算式的模組為 re ，首先要設定好配對形式 (pattern) 字串 (string) ，然後以該配對形式字串與所欲處理之字串利用 re 中相關功能的函式 (function) 進行處理。

#### re中常用的函式
函式          |  說明                        
---------------|:-------------------------------
match(pattern, string, flags=0)    | 決定re是不是在字串剛開始的位置配對 
search(pattern, string, flags=0) | search函式和match函式很相像，不同之處就是search函式並不是從字符串的開始處進行匹配，而是會查找整個字符串
findall(pattern, string, flags=0)  | 找到re匹配的所有字串，並合成一個list回傳 
compile(pattern, flags=0)|用來將正則表達式轉換爲一個「pattern object」，可以將其保存下來，已備後續之用。

------------------
## 讀取文本並去掉不需要的字符
```python=
def read_file(): 
    with open('/Users/wan/gapminder-api/bodyfile.txt', 'r', encoding='utf-8') as f:
        word = []  
        for word_str in f.readlines():  
            word_str = word_str.replace(',', '') 
            word_str = word_str.strip() 
            word_list = word_str.split('，')
            word.extend(word_list) 
        return word
```
分行讀取文本，且返回的是一個串列，每行的值當串列中的一個元素，利用`replace()`函式去除原檔空格，再利用`strip()`去除每行字符中的空白字符，對當行字符串通過逗號進行分割，回傳list存進`word_list`中，把分割後的list内容，加到`word`串列裡。

-------------
## 創建字典並存放分割後句子的出現次數
```python=
def clear_account(lists):
    count_dict = {} 
    count_dict = count_dict.fromkeys(lists) 
    word_list1 = list(count_dict.keys()) 
    for i in word_list1:
        count_dict[i] = lists.count(i)
    return count_dict
```
先定義一空字典`count_dict`，用來存放分割後的詞和出現次數，再取出字典中的key，放到`word_list1`，利用`count()`函式計算句子出現的次數,並存入`count_dict`字典中

### 字典(Dictionary)
字典的創建是以key-value pair形式儲存的資料結構，且key必須唯一(unique)，若有重複key會⾃動覆蓋原key-value pair 。


#### 獲取字典中的資料
函式           |  說明                        
---------------|:-------------------------------
dictionary.keys()    | 取得所有的key
dictionary.values() | 取得所有的value
dictionary.items()  | 取得所有的key-value pair

-----------
 ## 利用sorted()排序item裡的內容
  
```python=
 
def sort_dict(count_dict):
    del [count_dict['']] 
    my_dict = sorted(count_dict.items(), key=lambda d:d[0], reverse=True) 
    my_dict = dict(my_dict)
    return my_dict
```
把一開始利用`replace()`函式取代的''單字刪除， 並利用sorted()排序item裡的內容，其中`lambda`函式是對元素`d`第一個字段做排序，排序完成後存回`my_dict`中

____
## 將結果依序寫入ans.txt文本中

```python=
def main(my_dict):
    bodyfile = sys.stdout 
    sys.stdout = open('ans.txt','w', encoding = 'utf-8') 
    i = 0
    for x, y in my_dict.items():
        print('（%s, %s）' %(x,y) )
        i += 1
    sys.stdout.close()
    sys.stdout = bodyfile
```



________
## 執行結果
(斷句 , 出現次數)
![](https://i.imgur.com/C10e7TR.png)


______
## 其中碰到的問題
```python=
    #計算句子出現的次數,並存入count_dict字典中
    for i in word_list1:
        count_dict[i] = lists.count(i)#使用count計算出現次數
    return count_dict
```
原本寫的程式碼是如果遇

更改後：

```python=
    for word in word_list1:
        if word in count_dict :
            count_dict[word] += 1
        else :
            count_dict[word] = 1
    return count_dict
```
更改後的程式碼是先見一個字典

