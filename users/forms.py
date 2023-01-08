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
	email = forms.EmailField(required=True)
	phone_number = forms.CharField(required=True)
	age = forms.IntegerField(required=True)
	user_type = forms.ChoiceField(choices=USER_TYPE,required=True)
	gender = forms.ChoiceField(choices=GENDER_TYPE,required=True)
	type_of_activity = forms.ChoiceField(choices=TYPE_OF_ACTIVITY,required=True)
	hobby = forms.ChoiceField(choices=HOBBY,required=True)

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
		'class': 'form-control',
		'placeholder': 'username',
		'id': 'hello'
		}
	))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class': 'form-control',
		'placeholder': 'password',
		'id': 'hi'
		}
	))
	