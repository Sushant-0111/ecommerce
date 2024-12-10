from rest_framework import routers
from core.views import login,register
from django.urls import path
router = routers.SimpleRouter()
urlpatterns = [
   path('login',login),
   path('register',register)
    ]+router.urls
