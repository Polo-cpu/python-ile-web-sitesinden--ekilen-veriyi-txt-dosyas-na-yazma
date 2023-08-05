import requests
from bs4 import BeautifulSoup


class EarthquakeWebsiteScript:
    def __init__(self, base_url):
        self.base_url = base_url

    def website_check(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, "lxml")
        else:
            return False

    def find_datas_from_td(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, "html.parser")
        self.datas = soup.find_all("td")
        return self.datas

    def install_datas_to_txt(self):
        with open("C:/Users/atill/Desktop/deprembilgileri.txt", "r+", encoding="utf-8") as file:
            file.write('\n'.join('{} {}'.format(x[0], x[1]) for x in yeni_liste))


if __name__ == '__main__':
    x = 5
    y = 6
    r = []
    t = []
    datas = []
    myDatas = EarthquakeWebsiteScript("https://deprem.afad.gov.tr/last-earthquakes.html")
    if myDatas.website_check:
        for i in myDatas.find_datas_from_td():
            datas.append(i.text)
        while y < 502 and x < 501:
            r.append(datas[x])
            t.append(datas[y])
            x = x + 8
            y = y + 8
        r = list(map(float, r))
        t = list(map(str, t))
        yeni_liste = list(zip(r, t))
        for i, row in yeni_liste:
            if i >= 2.0:
                myDatas.install_datas_to_txt()
            else:
                pass

