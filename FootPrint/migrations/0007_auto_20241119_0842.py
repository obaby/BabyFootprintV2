# Generated by Django 3.2.3 on 2024-11-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FootPrint', '0006_markerimage_place_holder_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='markerimage',
            name='size_height',
            field=models.IntegerField(default=26, help_text='图标高度'),
        ),
        migrations.AddField(
            model_name='markerimage',
            name='size_width',
            field=models.IntegerField(default=26, help_text='图标宽度'),
        ),
    ]