import pandas as pd
import codecs
xd = pd.ExcelFile('样表.xlsx')
df = xd.parse()
with codecs.open('test.html','w','utf-8') as html_file:
    html_file.write(df.to_html(header = True,index = False))