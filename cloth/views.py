from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms


class ProductListView(ListView):
	queryset = models.ProductCL.objects.filter().order_by('-id')
	template_name = 'product_list.html'

	def get_queryset(self):
		return models.ProductCL.objects.filter().order_by('-id')


class ProductMaleView(ListView):
	queryset = models.ProductCL.objects.filter(tags__name='Male').order_by('-id')
	template_name = 'product_male.html'

	def get_queryset(self):
		return models.ProductCL.objects.filter(tags__name='Male').order_by('-id')


class ProductFemaleView(ListView):
	queryset = models.ProductCL.objects.filter(tags__name='Female').order_by('-id')
	template_name = 'product_female.html'

	def get_queryset(self):
		return models.ProductCL.objects.filter(tags__name='Female').order_by('-id')


class ProductBabyView(ListView):
	queryset = models.ProductCL.objects.filter(tags__name='Baby').order_by('-id')
	template_name = 'product_baby.html'

	def get_queryset(self):
		return models.ProductCL.objects.filter(tags__name='Baby').order_by('-id')


class ProductTeenagerView(ListView):
	queryset = models.ProductCL.objects.filter(tags__name='Teenager').order_by('-id')
	template_name = 'product_teenager.html'

	def get_queryset(self):
		return models.ProductCL.objects.filter(tags__name='Teenager').order_by('-id')


class ProductDetailView(DetailView):
	template_name = 'product_detail.html'

	def get_object(self, **kwargs):
		product_id = self.kwargs.get('id')
		return get_object_or_404(models.ProductCL, id=product_id)


class OrderCreateView(CreateView):
	template_name = 'add_order.html'
	form_class = forms.OrderCLForm
	success_url = '/product/'
	queryset = models.OrderCL.objects.all()

	def form_valid(self, form):
		return super(OrderCreateView, self).form_valid(form=form)