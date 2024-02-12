import requests
from urllib.parse import urljoin
import bs4
import os
import aiogram
request = requests.get("https://gocsgo.net/guides/advice/avatarki-dlya-doty/")



beautifull_soup = bs4.BeautifulSoup(request.text, 'html.parser')

# find_site = beautifull_soup.find("class")

site = (beautifull_soup.find('body', class_ = "post-template-default single single-post postid-14669 single-format-standard custom-background wp-custom-logo boxed-layout")).find('div', class_ = 'hfeed site')
# print(site)
site_content = site.find('div', id = 'content')

site_container_clearfix = site_content.find('div', class_ = 'container clearfix')
# print(site_container_clearfix)
site_primary = site_container_clearfix.find('div', id = 'primary')

site_main = site_primary.find('main', class_ = 'site-main clearfix test')

site_entry_content_clearfix = site_main.find('div', class_ = 'entry-content clearfix')

site_all_photoes = site_entry_content_clearfix.find('tbody')
# h = site_all_photoes.find('td')
# photo = h.find('a').find_all('img')
photo = site_all_photoes.find_all('img')
print(photo)
# img_name = os.path.basename(photo)
# img_path = os.path.join('study/images', img_name)
if request.status_code == 200:
    print('site work normally')
else:
    print("some troubles with site")
print(request)
for img in photo:
        try:
            img_url = img.get('src')  # Get the 'src' attribute of the image tag
            if img_url:
                # Convert relative URLs to absolute URLs
                img_url = urljoin("https://gocsgo.net/guides/advice/avatarki-dlya-doty/", img_url)
                img_name = os.path.basename(img_url)
                img_path = os.path.join('study/images', img_name)

                # Download the image
                img_data = requests.get(img_url).content

                # Save the image
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)
                    print(f"Image '{img_name}' saved successfully.")
        except requests.exceptions.ConnectionError:
            print(f"Connection error occurred while downloading image '{img_url}'. Skipping...")
