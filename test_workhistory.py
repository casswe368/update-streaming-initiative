# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:01:55 2020

@author: cassw
"""




from src.ao3 import AO3
import cred

api = AO3()
username=cred.username
password=cred.password
api.login(username, password)

work = api.work(id='27194623')
print('title')
#print(work._html)
print(work.title)

work = api.work(id='7215418')
print('title')
#print(work._html)
print(work.title)