#1. Download the page
from urllib. request import urlopen
from bs4 import BeautifulSoup
url = "https://dantri.com.vn/"
import pyexcel
from collections import OrderedDict

#1.1 Open connection
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode date
content = raw_data.decode("utf8")

# print(content)
# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()

#2. Find ROI
soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())
ul_news = soup.find("ul","ul1 ulnew")
print(ul_news.prettify())

#3. Copy and Save
li_list = ul_news.find_all("li")
print(li_list)
li = li_list[0]
# walking
new_list = []
for li in li_list:
    h4 = li.h4
    a = h4.a
    link = url + a["href"]
    title = a.string
    news = OrderedDict({
        "title": title,
        "link": link
    })
    new_list.append(news)
    print(new_list)

pyexcel.save_as(records=new_list, dest_file_name="dantri.xls")