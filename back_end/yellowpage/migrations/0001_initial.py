# Generated by Django 5.0.1 on 2024-02-08 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=128)),
                ('category_details', models.CharField(max_length=128)),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_category', to='yellowpage.businesscategory')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessAdderess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=130)),
                ('contact_number', models.CharField(max_length=50)),
                ('post_office', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('district', models.CharField(max_length=130)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=6)),
                ('business_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yellowpage.businesscategory')),
            ],
        ),
    ]
