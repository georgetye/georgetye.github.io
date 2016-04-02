from bs4 import BeautifulSoup
from urllib2 import urlopen

url = "https://www.khanacademy.org/test-prep/mcat/social-sciences-practice/social-science-practice-tut/e/is-obesity-contagious-"

html = urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
passageText = soup.find("div", "passagearea")

print(passageText)

import urllib

URL = "https://www.khanacademy.org/test-prep/mcat/social-sciences-practice/social-science-practice-tut/e/is-obesity-contagious-"

html = urllib.urlopen(URL).read()

soup = BeautifulSoup(html)

print (soup.findAll(div).get_text())