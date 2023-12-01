from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('category/<int:id>/', views.index_detail, name='index_detail'),
    path('product/<int:id>/', views.product_pge, name='product_page'),
    path('support/', views.support, name='support'),

]