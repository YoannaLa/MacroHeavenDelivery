from . import views
from django.urls import path

urlpatterns = [
    path('', views.products, name='products'),
    path('details/', views.product_details, name='details'),
    path('add/', views.product_add, name='add'),
    path('edit/<int:product_id>/', views.product_edit, name='edit'),
    path('delete/<int:product_id>/', views.product_delete, name='delete'),
]