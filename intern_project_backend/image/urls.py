from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$',views.ImageCollection.as_view()),
    re_path('^(?P<pk>[0-9]+)/$',views.ImageDetail.as_view()),
    re_path('^user/(?P<pk>[0-9]+)/$',views.UserImage.as_view()),
]
