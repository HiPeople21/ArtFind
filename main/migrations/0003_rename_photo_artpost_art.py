# Generated by Django 3.2.7 on 2021-09-19 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_artpost_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artpost',
            old_name='photo',
            new_name='art',
        ),
    ]