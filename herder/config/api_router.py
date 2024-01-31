from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from herder.users.api.views import UserViewSet
from herder.recruiting.api.views import ApplicationListView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("applications", ApplicationListView)



app_name = "api"
urlpatterns = router.urls
