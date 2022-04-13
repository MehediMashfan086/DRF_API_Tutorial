from django.conf.urls import url
from firstApp.api.views import *

urlpatterns = [
    url('first', firstFunction)
]
