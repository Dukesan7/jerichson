import requests
import bs4
import lxml
import time
import re
import os
from bs4 import BeautifulSoup
print ("What do you need to know about?")
topic = input(":")
res = requests.get('https://en.wikipedia.org/wiki/' + (topic))
type(res)
soup = bs4.BeautifulSoup(res.text, 'lxml')
type(soup)
text = soup.select('p')
text[0].getText()
print ("Unformatted text:")
print ((text))
time.sleep(1)
print ("Creating formatted text")
time.sleep(1)
hi = str(text)
import re
clean = re.compile('<.*?>')
hi = re.sub(clean, '', hi)
print ("Check the knowledge file for your knowledge.")
whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ,.:"()')
answer = ''.join(filter(whitelist.__contains__, hi))
file = open ("Knowledge.txt", "w")
file.write(answer)
file.close
os.system('pause')


    


