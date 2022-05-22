from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.product_image.models import ProductImage
from apps.product_image.serializers import ImageListSerializer


class ImageFilterAPI(ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ImageListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'uid', 'url']

    def get_serializer_context(self):
        context = super(ImageFilterAPI, self).get_serializer_context()
        context['params'] = self.request.query_params.dict()
        return context
