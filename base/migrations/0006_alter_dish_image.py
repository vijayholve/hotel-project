# Generated by Django 5.0.6 on 2024-05-23 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_dish_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/style'),
        ),
    ]