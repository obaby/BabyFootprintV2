# Generated by Django 3.2.3 on 2024-11-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FootPrint', '0002_auto_20241119_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='post_url',
            field=models.URLField(blank=True, help_text='文章 URL', null=True),
        ),
    ]