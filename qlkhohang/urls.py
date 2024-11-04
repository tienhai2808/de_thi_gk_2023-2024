from django.urls import path
from .views import *

urlpatterns = [
    path('' , index),
    path('suahanghoa/<int:id_hang_hoa>/', suahanghoa),
    path('taohanghoa/', suahanghoa),
    path('dshanghoa/', dshanghoa)
]