import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
from csv import writer

url = "https://www.screener.in/screens/15310/benjamin-graham-and-warren-buffett/"
request = requests.get(url)
soup = bs(request.content, 'html.parser')

def scrape(page_no):
    url = "https://www.screener.in/screens/15310/benjamin-graham-and-warren-buffett/?page={}".format(page_no)

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
 
page_parent = soup.find("div", class_ = "flex-row flex-gap-8 flex-space-between flex-align-center")   
page_content = page_parent.find("div",  class_ = "sub").text

page_str = str(page_content)

page_count = page_str.strip().split(" ")

print(page_count[-1])

for i in range(1,int(page_count[-1])+1):
    scrape(i)