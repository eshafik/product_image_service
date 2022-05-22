from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.scraper.tasks import scrap_url_for_images
from apps.scraper.validations import image_scraping_query_params_validation


class ImageFetcherAPI(APIView):

    @method_decorator(image_scraping_query_params_validation)
    def get(self, request):
        scrap_url_for_images.delay(request.query_params['url'])
        return Response(data={'message': 'Request success'})
