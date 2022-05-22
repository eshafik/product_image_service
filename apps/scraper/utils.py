from typing import List, Union
import re
import requests
from bs4 import BeautifulSoup
from PIL import Image

from apps.product_image.models import ProductImage


class ScrapManager(object):
    def __init__(self, site_url: str):
        self.site_url = site_url

    def get_all_image_tags(self) -> List:
        response = requests.get(self.site_url)

        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        return img_tags

    @staticmethod
    def get_filename(url: str) -> Union[str, bool]:
        filename = re.search(r'/([\w_-]+[.](jpg|jpeg|png))$', url)
        if not filename:
            if '?' not in url:
                filename = url.split('/')[-1]
                if len(filename.split('.')) > 1:
                    return False
                filename = f'{filename}.jpeg'
            else:
                filename = url.split('?')[0].split('/')[-1]
                if len(filename.split('.')) > 1:
                    return False
                filename = f'{filename}.jpeg'
        else:
            filename = filename.group(1)
        return filename

    @staticmethod
    def resize_image(img: Image, img_ext: str, file_path: str, required_width: int,
                     original_width: int, original_height: int) -> None:
        w_percent = (required_width / float(original_width))
        rsz_height = int((float(original_height) * float(w_percent)))
        img.thumbnail((required_width, rsz_height), Image.ANTIALIAS)
        img.save(file_path, img_ext)

    @staticmethod
    def save_on_database(all_data: List[dict]) -> None:
        ProductImage.objects.bulk_create([ProductImage(**data) for data in all_data])
        return
