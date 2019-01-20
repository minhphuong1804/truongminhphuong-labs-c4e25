from urllib. request import urlopen
from bs4 import BeautifulSoup
url = "https://www.apple.com/itunes/charts/songs/"
import pyexcel
from collections import OrderedDict

conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
soup = BeautifulSoup(content, "html.parser")
ul_song = soup.find("ul", "")
# print(ul_song.prettify())
li_list = ul_song.find_all("li")
# print(li_list)
songs_list = []

for li in li_list:
    h3 = li.h3
    h4 = li.h4
    name = h3.string
    artist = h4.string
    abc = OrderedDict({
        "name": name,
        "artist": artist
    })
    songs_list.append(abc)
print(songs_list)
pyexcel.save_as(records=songs_list, dest_file_name="iTunes.xlsx")