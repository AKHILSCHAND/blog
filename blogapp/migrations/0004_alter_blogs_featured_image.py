# Generated by Django 4.2.4 on 2023-09-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blogs_options_alter_blogs_featured_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='featured_image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d'),
        ),
    ]
