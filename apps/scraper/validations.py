from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from app_libs import exceptions
from app_libs.error_codes import ERROR_CODE


def image_scraping_query_params_validation(func):

    def validation(request, *args, **kwargs):
        if not request.query_params.get('url'):
            raise exceptions.ValidationError({**ERROR_CODE.global_codes.KEY_ERROR, 'hints': 'url query parameter is required'})
        validate_url = URLValidator()
        try:
            validate_url(request.query_params['url'])
        except ValidationError as e:
            raise exceptions.ValidationError({**ERROR_CODE.global_codes.VALUE_ERROR, 'hints': 'enter valid url'})
        return func(request, *args, **kwargs)

    return validation
