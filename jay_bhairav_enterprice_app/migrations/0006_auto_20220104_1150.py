# Generated by Django 2.2 on 2022-01-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jay_bhairav_enterprice_app', '0005_auto_20220103_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Title',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default='', null=True, upload_to='Images/'),
        ),
    ]
