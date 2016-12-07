#!/usr/bin/python
import socket
from bs4 import BeautifulSoup
import mechanize
import urllib2

# Thank you Professor Odersky and Functional Programming Principles in Scala
# for teaching me about higher-order functions as the function `select_form` returns
# the function `make_select_form`.
#
def select_form(action):
    def make_select_form(form):
        return form.attrs.get('action', None) == action
    return make_select_form

ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
url = 'http://masseria.org'

# set a timeout of 30 seconds in `socket` which will eventually be used by `urllib2`
socket.setdefaulttimeout(30.0)

br = mechanize.Browser()
br.addheaders = [('User-Agent', ua)]
br.set_handle_robots(False)
br.set_debug_http(True)
br.set_debug_responses(True)
br.open(url)

contents = br.response()
#contents = urllib2.urlopen(url).read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
for input in soup.find_all('input'):
    print(input)

action = None

for form in soup.find_all('form'):
    action=form.get('action')
    print(action)

br.select_form(predicate=select_form(action))
br.submit()
