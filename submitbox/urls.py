from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('post/login', views.login_form, name='login_form'),
    path('post/newuser', views.new_user_add, name='new_user_add'),
    path('post/list', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:name>/list', views.post_list, name='user_list'),
    path('post/<str:name>/new/', views.post_new, name='user_sheet_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
