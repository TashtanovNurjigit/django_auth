# Generated by Django 4.1.5 on 2023-01-05 11:23

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.IntegerField(choices=[(1, 'ADMIN'), (2, 'VipClient'), (3, 'CLIENT')], verbose_name='Тип пользователя')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE')], verbose_name='Пол')),
                ('type_of_activity', models.IntegerField(choices=[(1, 'STUDENT'), (2, 'SCHOOLBOY'), (3, 'PENSIONER'), (4, 'WORKER')], verbose_name='Деятельность')),
                ('hobby', models.IntegerField(choices=[(1, 'SPORT'), (2, 'READING'), (3, 'MUSIC'), (4, 'FILM'), (5, 'TRAVEL'), (6, 'OTHER')], verbose_name='Хобби')),
            ],
            options={
                'verbose_name': 'Пользовтель',
                'verbose_name_plural': 'Пользовтели',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
