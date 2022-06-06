from django.shortcuts import redirect

from manage_url.models import UrlBind


def get_host_url(request, divide_word):
    return request.build_absolute_uri().split(divide_word)[0]


def redirect_url(request, short_url):
    try:
        url = UrlBind.objects.get(short_url=request.build_absolute_uri())
    except UrlBind.DoesNotExist:
        url = None

    if url is not None:
        return redirect(url.url)
