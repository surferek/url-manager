import random

from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_409_CONFLICT

from urler.viewsets import ReadAndCreateViewSet
from .constants import URL_SIGNS, SHORTEN_URL
from .models import UrlBind
from .serializers import UrlBindReadSerializer, UrlBindCreateSerializer
from .utils import get_host_url


class UrlBindViewSet(ReadAndCreateViewSet):
    queryset = UrlBind.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return UrlBindReadSerializer
        return UrlBindCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        url = serializer.validated_data['url']
        suffix = ("".join(random.sample(URL_SIGNS, settings.URL_SUFFIX_SIZE)))
        short_url = get_host_url(request, SHORTEN_URL) + suffix

        try:
            bind = UrlBind.objects.get(url=url)
        except UrlBind.DoesNotExist:
            UrlBind.objects.create(
                url=url,
                short_url=short_url
            )
        else:
            return Response({'url': bind.url, 'short_url': bind.short_url}, HTTP_409_CONFLICT)

        headers = self.get_success_headers(serializer.data)
        return Response({'short_url': short_url}, HTTP_201_CREATED, headers=headers)
