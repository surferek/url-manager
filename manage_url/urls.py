from rest_framework import routers

from .views import UrlBindViewSet

router = routers.DefaultRouter()
router.register(r"shorten", UrlBindViewSet)
