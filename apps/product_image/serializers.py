from rest_framework import serializers

from apps.product_image.models import ProductImage


class ImageListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    meta_data = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ('id', 'uid', 'image', 'scraped_at', 'meta_data')

    def get_image(self, obj: ProductImage):
        params = self.context.get('params', {})
        if not params.get('size'):
            return obj.original_image
        if params['size'] == 'small':
            return obj.small_image or obj.original_image
        elif params['size'] == 'medium':
            return obj.medium_image or obj.original_image
        elif params['size'] == 'large':
            return obj.large_image or obj.original_image
        return obj.original_image

    def get_meta_data(self, obj: ProductImage):
        return {'original_image_size': obj.original_image_size, 'scrapped_at': obj.scraped_at}
