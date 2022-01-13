# Generated by Django 2.2 on 2022-01-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_No', models.CharField(max_length=12)),
                ('Message', models.CharField(max_length=800)),
                ('Subject', models.CharField(max_length=100)),
            ],
        ),
    ]
