from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from pyshorteners import Shortener
from .validators import is_url


@api_view(['POST'])
@permission_classes([AllowAny])
def shorten_url(request):
    url = request.data['url']
    if not is_url(url):
        return Response("Please provide valid url", HTTP_400_BAD_REQUEST)

    shortener = Shortener()
    short_url = shortener.tinyurl.short(url)

    response = {
        "short_url": short_url
    }
    return Response(response, HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def expand_url(request):
    url = request.data['url']
    if not is_url(url):
        return Response("Please provide valid url", HTTP_400_BAD_REQUEST)

    shortener = Shortener()
    long_url = shortener.tinyurl.expand(url)

    response = {
        "long_url": long_url
    }
    return Response(response, HTTP_200_OK)
