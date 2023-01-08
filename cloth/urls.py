from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
	path('product/', views.ProductListView.as_view(), name='product_list'),
	path('product/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
	path('product_male/', views.ProductMaleView.as_view(), name='product_male'),
	path('product_female/', views.ProductFemaleView.as_view(), name='product_female'),
	path('product_baby/', views.ProductBabyView.as_view(), name='product_baby'),
	path('product_teenager/', views.ProductTeenagerView.as_view(), name='product_teenager'),
	path('add-order/', views.OrderCreateView.as_view(), name='add-order'),
]
