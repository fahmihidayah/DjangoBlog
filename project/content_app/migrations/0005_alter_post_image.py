# Generated by Django 3.2.10 on 2021-12-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='img_placeholder.png', upload_to='post/%Y/%m/%d/'),
        ),
    ]
