# Generated by Django 2.2 on 2022-01-02 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jay_bhairav_enterprice_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Subject',
        ),
    ]