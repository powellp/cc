# Generated by Django 2.2.2 on 2019-07-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='portfolio_image'),
        ),
    ]
