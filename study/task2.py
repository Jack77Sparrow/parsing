import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_photo_urls():
    photo_urls = []
    url = "https://gocsgo.net/guides/advice/avatarki-dlya-doty/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            img_url = img.get('src')
            if img_url:
                img_url = urljoin("https://gocsgo.net/guides/advice/avatarki-dlya-doty/", img_url)
                photo_urls.append(img_url)
    print(photo_urls)
    return photo_urls

get_photo_urls()
