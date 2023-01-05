from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'users'

urlpatterns = [
	path('register/', views.Registration.as_view(), name='registration'),
	path('login/', views.NewLoginView.as_view(template_name='index.html', authentication_form=LoginForm), name='login'),
	path('users/', views.UserListView.as_view(), name='user_list'),
]