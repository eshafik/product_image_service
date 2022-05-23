### Project Architecture Overview
Its monolithic architecture with celery for doing asynchronous task. Whenever server gets request for scrapping the product 
images, It will pass the request to the celery workers. From the celery tasks, firstly it fetches the images urls,
then it asynchronously requests the image url for downloading the images with multiple threads. So, its 10 times faster 
than regular synchronous call.

### Pre-requirements to run the project
```bash
1. Install postgresql (if not exists in your system)
2. Install redis (if not exists in your system)
```

### Steps to run the project
```bash
    1. Create Virtualenvironment
    2. Install requirements.txt dependency
    3. Create postgresql database for the project
    4. Create .env file and add the environment variable from env.example
    5. Run migrate command
``` 

### Run the Dev server 
```bash
python manage.py runserver
```

### Run Celery Beside Dev server (Make sure redis server is running before celery run)
```bash
celery -A product_image_service worker -l info 
```

### Example of image scrapping API-
```bash
http://localhost:8000/api/v1/scrapers/image-fetcher/?url=https://unsplash.com/s/photos/web-scraping
```

### Example of image list and image filter API -
```bash
http://localhost:8000/api/v1/product-images/images/

Query parameters are:
id, uid, url, size
```