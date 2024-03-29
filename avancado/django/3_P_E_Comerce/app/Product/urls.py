from django.urls import path

from . import views
app_name = 'Product'

urlpatterns = [
    path('', views.ListProduct.as_view(), name='list'),
    path('<slug>/', views.DetailProduct.as_view(), name='detail'),
    path('addtocar/', views.AddToCar.as_view(), name='addtocar'),
    path('removetocar/', views.RemoveToCar.as_view(), name='removetocar'),
    path('car/', views.Car.as_view(), name='car'),
    path('resumetoshoop/', views.ResumeToShoop.as_view(), name='resumetoshoop'),
    path('getproduct/', views.GetProduct.as_view(), name='getproduct')
]