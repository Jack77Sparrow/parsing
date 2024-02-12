import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Request the webpage
url = "https://gocsgo.net/guides/advice/avatarki-dlya-doty/"
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all image tags
    images = soup.find_all('img')
    
    # Create a directory to save images if it doesn't exist
    if not os.path.exists('study/images'):
        os.makedirs('study/images')

    # Download and save each image
    for img in images:
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
else:
    print("Failed to retrieve the webpage.")


# print(site_all_photoes)




# def find_uniq(arr):
#     # your code here
#     i = []
#     h = 0
#     for ar in arr:
#         if ar not in i:
#             i.append(ar)
#     return i[-1]
# a= find_uniq([1,1,1,2,1,1])
# print(a)