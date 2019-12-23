import os
import json

from lxml import html
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))
download_path = os.path.join(dir_path,'downloads')

os.makedirs(download_path,exist_ok=True)

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }

class GoogleImageScraper:
    def __init__(self, url, download_path, query_search):
        self.url = url
        self.download_path = download_path
        self.query_search = query_search
        self.session = requests.session()

    def get_all_images(self):
        response = self.session.get(self.url,headers=REQUEST_HEADER)
        response = response.content
        html_tree = html.fromstring(response)

        image_div = html_tree.xpath("//div[contains(@class, 'rg_meta')]")
        image_dict_list = [json.loads(i.xpath("text()")[0]) for i in image_div]
        # ity is image type, ou: image_url, pt: image_name

        # print(len(image_dict_list)) # total are 100 images
        for image_dict in image_dict_list:
            image_type = image_dict.get('ity','')
            image_no = (image_dict_list.index(image_dict) +1)
            if image_type == '':
                image_type = 'jpeg'
            self.save_image(f'{self.query_search}_{image_no}.{image_type}',image_dict['ou'])
            print(f"Done no. {image_no}")
        print("Done all")

    def save_image(self, file_name, image_link):
        response = self.session.get(image_link, stream=False)

        if response.status_code == 200:
            with open(os.path.join(self.download_path, file_name), 'wb') as image_file:
                for chunk in response.iter_content(1024):
                    image_file.write(chunk)


if __name__ == '__main__':
    query_search = 'Goku'
    image_scraper = GoogleImageScraper(f"https://www.google.co.in/search?q={query_search}&source=lnms&tbm=isch", download_path, query_search)
    image_scraper.get_all_images()
