from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(
        #r'ws/chat/room/(?P<course_id>\d+)/$',
        r'ws/chat/room/$',
        consumers.ChatConsumer.as_asgi()
    ),
]