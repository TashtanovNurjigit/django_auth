from django import forms
from . import models


class OrderCLForm(forms.ModelForm):
	class Meta:
		model = models.OrderCL
		fields = '__all__'
		