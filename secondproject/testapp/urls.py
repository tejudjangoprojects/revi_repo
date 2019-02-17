from django.conf.urls import url
from . import views

#
urlpatterns=[
url(r'content/',views.display_view)
]
