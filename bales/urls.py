from django.urls import path
from .views import *

urlpatterns =[
    path('bales/',BaleList.as_view()),
    path('bales/<int:pk>/',BaleDetail.as_view()),
    path('stores/',StoreList.as_view()),
    path('stores/<int:pk>/',StoreDetail.as_view()),
]


