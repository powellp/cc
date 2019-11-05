from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$',views.UserCollection.as_view()),
    re_path('^(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
    re_path('^auth/$',views.UserAuth.as_view()),
    re_path('^search/$',views.UserSearch.as_view()),
]
