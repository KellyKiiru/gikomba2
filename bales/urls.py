from django.urls import path
from .views import BaleList

urlpatterns =[
    path('bales/',BaleList.as_view()),
    # path('bales/<int:pk>/', views.bale_detail)    
]


