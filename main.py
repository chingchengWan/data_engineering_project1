from flask import Flask, request, render_template, redirect, url_for
import re
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST': 
        target = request.values['keyword'] 
        file = open('/Users/wan/segmentation_of_word/ans_file.txt','r', encoding = 'utf-8') 
        text = file.readlines()
        #retString = "<h1>Here is the results of {}</h1>".format(target)
        word = []
        for lines in text:
            if target in lines:
                word.append(lines)
        
        # for _i in word:
        #     retString += _i
        #     retString += "<br><br>"
        #return word 
        
        sents = word
        return render_template('hello.html', sents=sents, keyword=target)
    '''
    # SPA, single page application 
    with open("./templates/index.html", "r") as fp:
        retpage = fp.readlines()
    return ''.join(retpage)
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run() 
