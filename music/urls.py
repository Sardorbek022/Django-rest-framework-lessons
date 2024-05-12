from django.urls import path

from .views import (
    SongsAPIView, 
)


urlpatterns = [
    path('songs', view=SongsAPIView.as_view(), name='songs'),
]
