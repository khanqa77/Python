import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    firoj_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, firoj_name)

download_web_image("https://www.thenewboston.com/images/homepage_images/main_homepage_01.png")