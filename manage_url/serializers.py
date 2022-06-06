from rest_framework.serializers import ModelSerializer

from .models import UrlBind


class UrlBindReadSerializer(ModelSerializer):
    class Meta:
        model = UrlBind
        fields = ['id', 'url', 'short_url']


class UrlBindCreateSerializer(ModelSerializer):
    class Meta:
        model = UrlBind
        fields = ['id', 'url']
