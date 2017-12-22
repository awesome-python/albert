from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/$', views.UserDetail.as_view()),
]

