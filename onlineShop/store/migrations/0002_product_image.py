# Generated by Django 3.1.3 on 2020-11-30 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', null=True, upload_to='product_images', verbose_name='Изображение'),
        ),
    ]
