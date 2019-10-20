from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_1, name='homepage'),
    path('page_1', views.page_1, name='page_1'),
    path('page_2', views.page_2, name='page_2'),
]

