from django.urls import path

from .views import (
    home,
    post_detail,
    register,
    profile,
    create_post,
    edit_post,
    delete_post,
)

urlpatterns = [
    path('', home, name='home'),

    path('register/', register, name='register'),

    path('profile/', profile, name='profile'),

    path('create/', create_post, name='create_post'),

    path(
        'edit/<int:post_id>/',
        edit_post,
        name='edit_post'
    ),

    path(
        'delete/<int:post_id>/',
        delete_post,
        name='delete_post'
    ),

    path(
        'post/<int:post_id>/',
        post_detail,
        name='post_detail'
    ),
]