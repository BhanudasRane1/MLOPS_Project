# Generated by Django 3.2.6 on 2021-08-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='titanic_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_class', models.IntegerField(max_length=10)),
                ('sex', models.IntegerField(max_length=10)),
                ('age', models.IntegerField(max_length=10)),
                ('no_sibling', models.IntegerField(max_length=10)),
                ('parch', models.IntegerField(max_length=10)),
                ('fare_amt', models.IntegerField(max_length=10)),
                ('embarc_c', models.IntegerField(max_length=10)),
                ('embarc_q', models.IntegerField(max_length=10)),
                ('embarc_s', models.IntegerField(max_length=10)),
            ],
        ),
    ]
