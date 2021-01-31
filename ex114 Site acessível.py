import urllib.request
from urllib.error import URLError

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except URLError:
    print('Deu erro')
else:
    print('Tudo Ok')
