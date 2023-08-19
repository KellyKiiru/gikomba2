from django.urls import path
from .views import BaleList, BaleDetail

urlpatterns =[
    path('bales/',BaleList.as_view()),
    path('bales/<int:pk>/',BaleDetail.as_view())    
]


