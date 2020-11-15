# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:01:55 2020

@author: cassw
"""

#Goal: get a list of all ids in the user's catalog of works
#search each work for "shockwave-flash" to flag works that need to be updated after flash plug-in decommission
#hopeful later goal: replace outdated code with new html5 version


from src.ao3 import AO3
import cred

api = AO3()
username=cred.username
password=cred.password
api.login(username, password)

work = api.work(id='7215418')
print('title')
#print(work._html)
print(work.title)
print('text')

work2 = api.work(id='25717039')
print('title')
#print(work2._html)
print(work2.title)

#workList = api.user.catalog_ids()
#print(workList)
#print(work2.summary)

"""
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
"""

print(work2.body)