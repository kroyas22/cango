from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

from django.urls import path
from .views import home, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]