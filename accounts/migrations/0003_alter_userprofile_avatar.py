# Generated by Django 3.2.7 on 2021-10-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211012_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatar/default.svg', upload_to='avatars/'),
        ),
    ]
