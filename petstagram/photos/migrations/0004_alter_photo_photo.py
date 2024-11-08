# Generated by Django 5.1.3 on 2024-11-06 16:26

import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[petstagram.photos.validators.FileSizeValidator(5)]),
        ),
    ]
