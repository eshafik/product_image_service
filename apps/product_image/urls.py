from django.urls import path

from apps.product_image.views import ImageFilterAPI

urlpatterns = [
    path('images/', ImageFilterAPI.as_view(), name='image-filter-api'),
]
