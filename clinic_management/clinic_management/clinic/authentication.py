from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from django.conf import settings

class OAuth2Authentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        try:
            token = auth_header.split()[1]
            user = User.objects.get(token=token)
            return (user, token)
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

    def authenticate_header(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        try:
            token = auth_header.split()[1]
            user = User.objects.get(token=token)
            return user
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid token')