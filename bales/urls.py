from django.urls import path
from . import views

urlpatterns =[
    path('bales/',views.bale_list),
    path('bales/<int:pk>/', views.bale_detail)    
]


