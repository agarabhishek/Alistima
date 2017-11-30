from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = 'https://www.google.co.in/search?channel=fs&q=what+is+my+ip&ie=utf-8&oe=utf-8&gfe_rd=cr&dcr=0&ei=ED8SWuWYJfDy8AeG6brwBA'
response = http.request('GET', url)
soup = BeautifulSoup(response.data)
# print (soup.prettify()) Complete HTML of page
right=soup.find_all('tbody')
a=[]
for row in right:
    cells = row.findAll('td')
    for qt in cells[1]:
        data=cells[1].findAll('div')
        a.append(data[2].find(text=True))
print("")
print("Your current IP is -")
print(a[0])