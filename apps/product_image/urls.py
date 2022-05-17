from django.urls import path

from apps.product_image.views import TestView

urlpatterns = [
    path('', TestView.as_view()),
]