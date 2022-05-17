"""
    Version: 1.0.0
    Author: MSI Shafik
"""

from django.urls import path, include

# Put here all apps url 
urlpatterns = [
    path('product-images/', include('apps.product_image.urls')),
    path('scrapers/', include('apps.scraper.urls')),
]
