# Generated by Django 5.0.2 on 2024-05-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='1.jpg', upload_to='products/'),
            preserve_default=False,
        ),
    ]
