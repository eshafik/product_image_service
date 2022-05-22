from django.urls import path
from apps.scraper.views import ImageFetcherAPI


urlpatterns = [
    path('image-fetcher/', ImageFetcherAPI.as_view(), name='image-fetcher-api'),
]