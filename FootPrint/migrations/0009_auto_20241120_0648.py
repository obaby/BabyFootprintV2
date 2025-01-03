# Generated by Django 3.2.3 on 2024-11-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FootPrint', '0008_markerimage_blog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapsetting',
            name='is_enabel_3d',
            field=models.BooleanField(default=True, help_text='是否启用3D'),
        ),
        migrations.AlterField(
            model_name='mapsetting',
            name='map_zoom',
            field=models.IntegerField(default=5, help_text='地图缩放等级：1-20'),
        ),
    ]
