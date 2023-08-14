import requests
from bs4 import BeautifulSoup

soup = ""

# The url from which we want to scrape data
url = "https://www.google.com/search?q=scrapping&rlz=1C1CHBF_enIN1034IN1034&oq=scrapping&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABixAxiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIJCAUQABgKGIAEMgkIBhAAGAoYgAQyBggHEEUYPNIBCDIxMjZqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def fetchAndSaveToFile(url,path):
    # Fetch the url. It will return all the html/xml of the page
    r = requests.get(url, headers=headers)
    # In windows it was important to add character encoding otherwise it will throw UnicodeEncodeError
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

fetchAndSaveToFile(url, "data/showcase.html")


# soup = BeautifulSoup(r.text, "html.parser")
# print(soup)
# print("---------------------------------------")
# spans = soup.find_all(class_="jss880")
# print(spans)