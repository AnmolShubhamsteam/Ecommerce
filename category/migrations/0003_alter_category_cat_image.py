# Generated by Django 5.0.4 on 2024-04-30 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.CharField(max_length=255),
        ),
    ]