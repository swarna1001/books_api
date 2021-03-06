# Generated by Django 3.1.7 on 2021-09-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210908_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='book_images'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
