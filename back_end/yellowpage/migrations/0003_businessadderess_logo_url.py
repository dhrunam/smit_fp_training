# Generated by Django 5.0.1 on 2024-02-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yellowpage', '0002_businesscategory_category_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessadderess',
            name='logo_url',
            field=models.FileField(blank=True, null=True, upload_to='category/'),
        ),
    ]
