from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Location(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, help_text='名称')
    text = models.TextField(max_length=64, blank=False, null=False, help_text='文本')
    mark = models.TextField(max_length=64, blank=False, null=False, help_text='备注')
    lontitude = models.FloatField(blank=True, null=True, help_text='经度')
    latitude = models.FloatField(blank=True, null=True, help_text='纬度')

    is_passed = models.BooleanField(default=False, help_text='是否途径点')

    create = models.DateTimeField(default=timezone.now, help_text='创建时间')
    update = models.DateTimeField(auto_now=True, help_text='更新时间')

    marker_image = models.URLField(blank=True, null=True, help_text='图标 URL')


    # def formatted_datetime(self):
    #     return self.create.strftime("%Y-%m-%d %H:%M")

    class Meta:
        verbose_name = '地点信息'
        verbose_name_plural = '地点信息'

    def __str__(self):
        return "%s(%s)" % (self.name, self.text)


class MarkerImage(models.Model):
    normal_image = models.URLField(blank=False, null=False,help_text='普通图标')
    passed_image = models.URLField(blank=False, null=False, help_text='途径图标')

    create = models.DateTimeField(default=timezone.now, help_text='创建时间')
    update = models.DateTimeField(auto_now=True, help_text='更新时间')

    class Meta:
        verbose_name = 'Marker图标'
        verbose_name_plural = 'Marker图标'

    def __str__(self):
        return "%s(%s)" % (self.normal_image, self.passed_image)