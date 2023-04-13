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
        
        tmp = re.sub(r'\s+',' ', row_text_with_icon)
        tmp = re.sub(r'%','',tmp)
        tmp = tmp.strip()
        tmp = re.sub(r'(Legendary|Exotic)([A-Z])',r'\1 \2',tmp)
        tmp = re.sub(r'(Submachine|Grenade|Auto) ',r'\1',tmp)
        tmp = tmp.replace(' ', '',1)
        tmp = re.sub(r'(?<=\w)(Legendary|Exotic)', r' \1', tmp)
        tmp = tmp.replace(' ', ',')
        table_rows_text.append(tmp)


    table_rows_text.pop(0)
    csv_filename = os.path.splitext(htmlFile)[0] + ".csv"


    with open(csv_filename,'w') as csvFile:


        for row in table_rows_text:

            csvFile.write(row+'\n')