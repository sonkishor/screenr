import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
from csv import writer

url = "https://www.screener.in/screens/6994/Low-on-10-year-average-earnings/"

request = requests.get(url)
soup = bs(request.content, 'html.parser')

table = soup.find("table", class_ = "data-table text-nowrap striped")
rows = table.find_all("tr")

headings_raw = rows[0].find_all("th", {"scope" : "colgroup"})
headings = []

with open('Stonks.csv', 'a') as f_object:
    write = writer(f_object)
    for heading in headings_raw:
        head = heading.text
        headings.append(head.replace('\n','').strip().replace("  ", " "))
    write.writerow(headings)

    for row in rows:
        data = []
        raw_data = row.find_all("td")
        for datas in raw_data:
            data.append(datas.text.replace('\n','').strip())
        write.writerow(data)  