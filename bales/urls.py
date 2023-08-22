from django.urls import path
from .views import *

bale_list = BaleViewSet.as_view({
    'get':'list',
    'post':'create'
})

urlpatterns =[
    path('bales/',bale_list),
    path('bales/<int:pk>/',BaleDetail.as_view()),
    path('stores/',StoreList.as_view()),
    path('stores/<int:pk>/',StoreDetail.as_view()),
]


