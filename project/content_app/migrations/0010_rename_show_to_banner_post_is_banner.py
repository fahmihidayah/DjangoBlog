# Generated by Django 3.2.10 on 2021-12-24 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0009_post_show_to_banner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='show_to_banner',
            new_name='is_banner',
        ),
    ]
