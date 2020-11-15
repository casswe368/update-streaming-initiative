# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 01:14:34 2020

@author: cassw
"""


from src.ao3 import AO3
import cred
from bs4 import BeautifulSoup, Tag
"""
work = api.work(id='7215418')
print('title')
#print(work._html)
print(work.title)
print('text')

work2 = api.work(id='15718194')
print('title')
#print(work2._html)
print(work2.title)

#workList = api.user.catalog_ids()
#print(workList)
#print(work2.summary)


f = open('WorkHTMLTEST.txt', 'w', encoding='utf-8')
html=work2._html
soup=work2._soup
#f.write('html starts here')
#f.write(html)
#f.write('html ends here')
#f.write(' ')
#f.write('soup starts here')
f.write(soup.prettify())
#f.write('soup ends here')
f.close()


#print(work.body)

text=work.body

soup = BeautifulSoup(text, 'html.parser')

print(soup.embed)

for link in soup.find_all('embed'):
    print(link.get('flashvars'))

text2=work2.body

soup2 = BeautifulSoup(text2, 'html.parser')

print(soup2.embed)
"""

def login():
    #log in to AO3 to view restricted works
    api = AO3()
    username=cred.username
    password=cred.password
    api.login(username, password)
    return api
    
def getCatalog(api):
    #pull a list of all ids for the user's catalog of works    
    catalog = api.user.catalog_ids()
    return catalog

def scanWorks(api,catalog):
    #scan through each work in the catalog for embedded audio that will no longer function
    #create a class instance to store information about each work
    for work_id in catalog:
        work = api.work(id=work_id)
        searchText(work)
    return
        
def searchText(work):
    #search through the body of the text for the broken streaming code
    soup=BeautifulSoup(work.body, 'html.parser')
    numBroken=0
    for embed in soup.find_all('embed'):
        report=''
        numBroken+=1
        
        if numBroken == 1:
            report+=startReport(work)
            
        report+=replaceCode(embed)
        
        print(report)

def startReport(work):
    #for each work identified, begin a report on the broken streaming code that needs to be replaced
    intro="\n\nPODFIC: %s\nURL: %s\n\n\n" % (work.title,work.url)
    return intro
    
def replaceCode(embed):
    #replace the broken code with the updated code
    #include the streaming link in the updated code
    url_data=embed.get('flashvars')
    print(url_data)
    if url_data.startswith('audioUrl'):
        link=url_data[9:]
        print(link)
    else:
        if url_data.startswith('mp3'):
            link=url_data[4:]
            print(link)
        else:
            raise Exception('New Code Indentified:',embed)
    
    report='BROKEN CODE:\n\n%s\n\nUPDATED CODE:\n\n<audio src="%s" controls="controls" crossorigin="anonymous" preload="metadata"></audio>\n\n' % (embed, link)
    
    return report        

def main():
    api = login()
    #catalog=getCatalog(api)
    #scanWorks(api,catalog)
    searchText(api.work(id='7215418'))
    return

main()