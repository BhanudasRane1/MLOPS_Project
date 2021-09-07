# Generated by Django 3.2.6 on 2021-08-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0003_dogcat_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='wine_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alcohol', models.IntegerField(max_length=10)),
                ('malic_acid', models.IntegerField(max_length=10)),
                ('ash', models.IntegerField(max_length=10)),
                ('acl', models.IntegerField(max_length=10)),
                ('mg', models.CharField(blank=True, max_length=36, null=True)),
                ('phenols', models.CharField(blank=True, max_length=36, null=True)),
                ('flavanoids', models.CharField(blank=True, max_length=36, null=True)),
                ('nonflavanoid_phenols', models.CharField(blank=True, max_length=36, null=True)),
                ('proanth', models.CharField(blank=True, max_length=36, null=True)),
                ('color_int', models.CharField(blank=True, max_length=36, null=True)),
                ('hue', models.CharField(blank=True, max_length=36, null=True)),
                ('od', models.CharField(blank=True, max_length=36, null=True)),
                ('proline', models.CharField(blank=True, max_length=36, null=True)),
            ],
        ),
    ]
