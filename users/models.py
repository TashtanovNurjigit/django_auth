from django.db import models
from django.contrib.auth.models import User

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


class CustomUser(User):
	class Meta:
		verbose_name = 'Пользовтель'
		verbose_name_plural = 'Пользовтели'
	user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя')
	phone_number = models.CharField('Номер телефона', max_length=100)
	age = models.PositiveIntegerField()
	gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Пол')
	type_of_activity = models.IntegerField(choices=TYPE_OF_ACTIVITY, verbose_name='Деятельность')
	hobby = models.IntegerField(choices=HOBBY, verbose_name='Хобби')