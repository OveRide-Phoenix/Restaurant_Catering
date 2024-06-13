from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book_catering, name='book_catering'),
    path('add-menu-item/', views.add_menu_item, name='add_menu_item'),
]
