from docx import Document
import os
import pandas as pd

d1="./20211231/班级1/"
d2="./20211231/班级2/"
today="2022-01-01"

os.mkdir("./20220101/")
os.mkdir("./20220101/班级1")
os.mkdir("./20220101/班级2")

for d in [d1,d2]:
    for file in os.listdir(d):
        name=file.split("班")[1].split(".")[0]
        document = Document(d+file)
        table=document.tables[0]
        if table.rows[0].cells[0].text!='辅导员：某某某':
            print("出问题了，表格第一行不对")
            print(name)
            break
        rows=table.rows
        rows[0].cells[10].text='分包系领导：某某某'
        rows[0].cells[18].text='联系电话：12345678910'
        for i in range(8,len(rows)):
            r=rows[8]
            r._element.getparent().remove(r._element)
        if d==d1:
            document.save("./20220101/班级1/"+file)
        else:
            document.save("./20220101/班级2/"+file)
