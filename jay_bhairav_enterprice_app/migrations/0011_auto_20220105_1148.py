# Generated by Django 2.2 on 2022-01-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jay_bhairav_enterprice_app', '0010_auto_20220104_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_details',
            name='Call_For_Price',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='Country_Of_Manufacture',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='img4',
        ),
        migrations.AddField(
            model_name='product_details',
            name='Title',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
