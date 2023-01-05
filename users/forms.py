from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
VipClient = 2
CLIENT = 3

USER_TYPE = (
	(ADMIN, 'ADMIN'),
	(VipClient, 'VipClient'),
	(CLIENT, 'CLIENT')
	)

MALE = 1
FEMALE = 2

GENDER_TYPE = (
	(MALE, 'MALE'),
	(FEMALE, 'FEMALE')
	)

STUDENT = 1
SCHOOLBOY = 2
PENSIONER = 3
WORKER = 4

TYPE_OF_ACTIVITY = (
	(STUDENT, 'STUDENT'),
	(SCHOOLBOY, 'SCHOOLBOY'),
	(PENSIONER, 'PENSIONER'),
	(WORKER, 'WORKER')
	)

SPORT = 1
READING = 2
MUSIC = 3
FILM = 4
TRAVEL = 5
OTHER = 6

HOBBY = (
	(SPORT, 'SPORT'),
	(READING, 'READING'),
	(MUSIC, 'MUSIC'),
	(FILM, 'FILM'),
	(TRAVEL, 'TRAVEL'),
	(OTHER, 'OTHER')
	)


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email', 'id': 'hi'}))
	phone_number = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Phone number', 'id': 'hi'}))
	age = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Age', 'id': 'hi'}))
	user_type = forms.ChoiceField(choices=USER_TYPE,required=True, widget=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'User Type', 'id': 'hi'}))
	gender = forms.ChoiceField(choices=GENDER_TYPE,required=True,  widget=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'Gender', 'id': 'hi'}))
	type_of_activity = forms.ChoiceField(choices=TYPE_OF_ACTIVITY,required=True,  widget=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'Activity', 'id': 'hi'}))
	hobby = forms.ChoiceField(choices=HOBBY,required=True,  widget=forms.RadioSelect(attrs={'class': 'input', 'placeholder': 'Hobby', 'id': 'hi'}))

	class Meta:
		model = models.CustomUser
		fields = (
			'username',
			'email',
			'password1',
			'password2',
			'first_name',
			'last_name',
			'age',
			'user_type',
			'gender',
			'type_of_activity',
			'hobby'
			)

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'input'
		self.fields['password1'].widget.attrs['class'] = 'input'
		self.fields['password2'].widget.attrs['class'] = 'input'
		self.fields['first_name'].widget.attrs['class'] = 'input'
		self.fields['last_name'].widget.attrs['class'] = 'input'

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

	username = UsernameField(widget=forms.TextInput(
		attrs={
		'class': 'input',
		'placeholder': 'Username',
		'id': 'hello',
		'data-type': 'username'
		}
	))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class': 'input',
		'placeholder': 'Password',
		'id': 'hi'
		}
	))
	