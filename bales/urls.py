from django.urls import path
from .views import *

bale_list = BaleViewSet.as_view({
    'get':'list',
    'post':'create'
})

bale_detail = BaleViewSet({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

store_list = StoreViewSet({
    'get':'list'
})

store_detail = StoreViewSet({
    'get':'retrieve'
})

urlpatterns =[
    path('bales/',bale_list,name='bale_list'),
    path('bales/<int:pk>/',bale_detail,name='bale_detail'),
    path('stores/',store_list,name='store_list'),
    path('stores/<int:pk>/',store_detail,name='store_detail'),
]


