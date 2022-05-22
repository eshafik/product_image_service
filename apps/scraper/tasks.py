import re
from celery import shared_task
import requests
from bs4 import BeautifulSoup
from PIL import Image

from apps.product_image.models import ProductImages
from apps.scraper.utils import ScrapManager


@shared_task
def scrap_url_for_images(site_url: str) -> bool:
    scrap_manager = ScrapManager(site_url)
    image_tags = scrap_manager.get_all_image_tags()
    urls = [img['data-src'] if img.get('data-src') else img.get('src') for img in image_tags]
    all_data = []
    for url in urls:
        filename = scrap_manager.get_filename(url)
        if not filename:
            continue
        data = {'url': site_url}
        original_image_path = f'media/original_images/{filename}'
        data['original_image'] = f'/{original_image_path}'
        img_ext = original_image_path.split('.')[-1].upper()

        with open(original_image_path, 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site_url, url)
            response = requests.get(url)
            f.write(response.content)
        img = Image.open(original_image_path)
        original_image_size = img.size
        original_width = original_image_size[0]
        original_height = original_image_size[1]

        print("original image size", original_image_size)
        data['original_image_size'] = f'{original_width}px X {original_height}px'
        if original_width > 256:
            file_path = f'media/small_images/{filename}'
            scrap_manager.resize_image(img, img_ext, file_path, 256, original_width, original_height)
            data['small_image'] = f'/{file_path}'
        if original_width > 1024:
            file_path = f'media/medium_images/{filename}'
            scrap_manager.resize_image(img, img_ext, file_path, 1024, original_width, original_height)
            data['medium_image'] = f'/{file_path}'
        if original_width > 2048:
            file_path = f'media/large_images/{filename}'
            scrap_manager.resize_image(img, img_ext, file_path, 2048, original_width, original_height)
            data['large_image'] = f'/{file_path}'
        all_data.append(data)
    scrap_manager.save_on_database(all_data)
    return True
