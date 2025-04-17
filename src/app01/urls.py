from rest_framework import routers
from .api import AppViewSet

router =  routers.DefaultRouter()

router.register('api/app', AppViewSet, 'app') #url que se va a usar para acceder a la api

urlpatterns = router.urls #url que se va a usar para acceder a la api
