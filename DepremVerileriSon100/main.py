import requests
from bs4 import BeautifulSoup
class deprem_buyuklugu():
    def __init__(self):
        self.base_url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    def buyuk_depremleri_bul(self,url):
        url = "https://deprem.afad.gov.tr/last-earthquakes.html"
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content,"lxml")
        else:
            return False
    def td_bulma(self):
        url = "https://deprem.afad.gov.tr/last-earthquakes.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        self.veriler = soup.find_all("td")
        return self.veriler

veriler = deprem_buyuklugu()
degerler = veriler.td_bulma()
asil_degerler = []
for i in degerler:
    asil_degerler.append(i.text)
c = list(asil_degerler)
j = 5
k = 6
r = []
t = []
while j < 800 and k<800:
    r.append(c[j])
    t.append(c[k])
    k = k+8
    j = j+8
r = list(map(float,r))
t = list(map(str,t))
yeni_liste = list(zip(r,t))
for i,row in yeni_liste:
    if i >=2.0:
        print(i,row)
    else:
        pass
buyukler = []
with open("C:/Users/atill/Desktop/deprembilgileri.txt","w",encoding="utf-8") as file:
    file.write('\n'.join('{} {}'.format( x[0], x[1]) for x in yeni_liste))


