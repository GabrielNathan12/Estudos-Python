from django.urls import path

from . import views

app_name = 'Order'

urlpatterns = [
    path('pay/<int:pk>', views.Pay.as_view(), name='pay'),
    path('saveorder/', views.SaveOrder.as_view(), name='saveorder'),
    path('list/', views.List.as_view(), name='list'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail')
]