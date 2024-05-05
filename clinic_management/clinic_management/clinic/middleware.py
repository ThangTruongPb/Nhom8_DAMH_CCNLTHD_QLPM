from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import get_authorization_header
from clinic.authentication import JWTAuthentication

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization = get_authorization_header(request).split()
        if authorization and len(authorization) == 2:
            token = authorization[1].decode('utf-8')
            try:
                jwt_auth = JWTAuthentication()
                user, _ = jwt_auth.authenticate(request)
                request.user = user
            except exceptions.AuthenticationFailed:
                pass
        response = self.get_response(request)
        return response