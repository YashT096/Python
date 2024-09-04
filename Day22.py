#hello Hellooo
#Today we are going to learn web scraping
#intially install pip requests on terminal , then install the beautifulsoup4 
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/")

soup= BeautifulSoup(req.content, "html.parser")

print(soup.prettify())
 #to Run the following code you have to type : python "Your FIle name "
 #as in my case i wrote :python day22.py on terminal 

#to Get text directly

import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/")

soup= BeautifulSoup(req.content, "html.parser")

print(soup.get_text())