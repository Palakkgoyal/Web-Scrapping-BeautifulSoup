import requests

def fetchAndSaveToFile(url,path):
    # Fetch the url. It will return all the html/xml of the page
    r = requests.get(url)
    # In windows it was important to add character encoding otherwise it will throw UnicodeEncodeError
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

# The url from which we want to scrape data
url = "https://timesofindia.indiatimes.com/international-home"

fetchAndSaveToFile(url, "data/times.html")