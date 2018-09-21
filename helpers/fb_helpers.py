# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Library that helps in various task for facebook"
"""

import requests
from bs4 import BeautifulSoup

def login(username, password):
    _login_url = "https://m.facebook.com/"
    _headers = {'User-Agent':'Mozilla/5.0'}
    r = requests.get(_login_url)

    _soup= BeautifulSoup(r.text,'html.parser')
    _form = _soup.find('form', {'id': 'login_form'})
    _inputs= _form.find_all('input')

    _load={}

    for i in _inputs:
        _load[i.get('name')]=i.get('value')

    _load['email'] = username
    _load['pass'] = password
    s=requests.session()
    r=s.post(_form.get('action'),data=_load,headers=_headers)
    print(r.url) #to verify login
    s.close()