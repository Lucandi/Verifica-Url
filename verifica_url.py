#Verificando se site está online
from urllib.request import urlopen
from urllib.error import *
try:

    site = urlopen('https://www.youtube.com/')
#except HTTPError as erro:
    #print('HTTP Error!', erro)
except URLError as erro:
    print('Ops! Page not Found!', erro)

else:
    print('Site is online ☻')