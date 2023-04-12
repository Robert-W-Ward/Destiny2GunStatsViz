from bs4 import BeautifulSoup as soup
import os
import re

import csv

import requests


htmlDir = 'html\\'

for htmlFile in os.listdir(htmlDir):


    contents = open(os.path.join(htmlDir,htmlFile),'r').read()


    parsed = soup(contents,'html.parser')


    rows = parsed.find_all('tr')

    table_rows_text = []

    row_text_with_icon = ''

    for row in rows:

        tags = row.find_all(lambda tag: tag.has_attr('src'))

        for tag in tags:

            url = tag['src']

            filename = os.path.basename(url)

            row_text_with_icon =  row.text+filename

            filepath = os.path.join('jpg',filename)

            # Create the "jpg" directory if it doesn't exist

            if not os.path.exists("jpg"):
                os.makedirs("jpg")

            with open(filepath,'wb') as jpgFile:

                jpgFile.write(requests.get(url).content)
            

        tmp = row_text_with_icon.replace('\n',' ').replace('\t','')


        table_rows_text.append(re.sub(r"(Legendary|Exotic)\s*|\s+", lambda m: m.group(0).strip() + " ",tmp).strip().replace(' ', ',').replace('%','' ))


    table_rows_text.pop(0)
    csv_filename = os.path.splitext(htmlFile)[0] + ".csv"


    with open(csv_filename,'w') as csvFile:


        for row in table_rows_text:

            csvFile.write(row+'\n')