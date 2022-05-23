import uuid

from django.db import models
from django.core.validators import RegexValidator


URL_VALIDATOR_MESSAGE = 'Not a valid URL.'
URL_VALIDATOR = RegexValidator(regex='/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/',
                               message=URL_VALIDATOR_MESSAGE)


class ProductImage(models.Model):
    uid = models.UUIDField(unique=True, default=uuid.uuid4)
    url = models.URLField()
    original_image = models.URLField(validators=[URL_VALIDATOR])
    original_image_size = models.CharField(max_length=45)
    small_image = models.URLField(blank=True, null=True, validators=[URL_VALIDATOR])
    medium_image = models.URLField(blank=True, null=True, validators=[URL_VALIDATOR])
    large_image = models.URLField(blank=True, null=True, validators=[URL_VALIDATOR])
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.uid}'

    class Meta:
        db_table = 'product_images'
        indexes = [
            models.Index(fields=['url']),
        ]
        ordering = ['-scraped_at']


