from bs4 import BeautifulSoup
from requests import get

if __name__ == '__main__':
    response = get("https://it-league.lviv.ua/Table")
    content = response.content
    print(content)
    soup = BeautifulSoup(content, "html.parser")

    table = soup.find("div", {"class": "widget-content"})
    for item in table.children:
        print(item)


