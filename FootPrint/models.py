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
    visit_date = models.DateField(blank=True, null=True, help_text='访问日期')
    leave_date = models.DateField(blank=True, null=True, help_text='离开日期')

    marker_image = models.URLField(blank=True, null=True, help_text='图标 URL')
    picture_url = models.URLField(blank=True, null=True, help_text='图片 URL')
    note = models.TextField(blank=True, null=True, help_text='笔记')
    post_url = models.URLField(blank=True, null=True, help_text='文章 URL')

    # def formatted_datetime(self):
    #     return self.create.strftime("%Y-%m-%d %H:%M")

    class Meta:
        verbose_name = '地点信息'
        verbose_name_plural = '地点信息'

    def __str__(self):
        return "%s(%s)" % (self.name, self.text)


class MarkerImage(models.Model):
    normal_image = models.URLField(blank=False, null=False, help_text='普通图标')
    passed_image = models.URLField(blank=False, null=False, help_text='途径图标')

    place_holder_image_url = models.URLField(blank=True, null=True, help_text='占位图片')
    size_width = models.IntegerField(default=26, help_text='图标宽度')
    size_height = models.IntegerField(default=26, help_text='图标高度')

    blog_url = models.URLField(default='https://oba.by/', help_text='默认连接')

    create = models.DateTimeField(default=timezone.now, help_text='创建时间')
    update = models.DateTimeField(auto_now=True, help_text='更新时间')

    class Meta:
        verbose_name = 'Marker图标'
        verbose_name_plural = 'Marker图标'

    def __str__(self):
        return "%s(%s)" % (self.normal_image, self.passed_image)


class MapSetting(models.Model):
    map_type = models.IntegerField(default=1, help_text='地图类型：1 标准地图 2 地球模式 3 普通卫星地图')
    # 1.标准地图：BMAP_NORMAL_MAP
    # 2.地球模式：BMAP_EARTH_MAP
    # 3.普通卫星地图：BMAP_SATELLITE_MAP
    map_zoom = models.IntegerField(default=5, help_text='地图缩放等级：1-20')
    center_latitude = models.FloatField(blank=True, null=True, help_text='中心纬度')
    center_longitude = models.FloatField(blank=True, null=True, help_text='中心经度')

    is_enable_scroll_wheel_zoom = models.BooleanField(default=True, help_text='是否启用滚轮缩放')
    is_add_control = models.BooleanField(default=True, help_text='是否添加缩放控件')
    is_add_scaleCtrl = models.BooleanField(default=True, help_text='是否添加比例尺控件')

    is_enable_3d = models.BooleanField(default=True, help_text='是否启用3D')
    create = models.DateTimeField(default=timezone.now, help_text='创建时间')
    update = models.DateTimeField(auto_now=True, help_text='更新时间')

    class Meta:
        verbose_name = '地图配置'
        verbose_name_plural = '地图配置'

    def __str__(self):
        return "%s(%s)" % (self.map_type, self.map_zoom)


class MapKey(models.Model):
    map_key = models.CharField(max_length=64, blank=False, null=False, help_text='地图 key')
    create = models.DateTimeField(default=timezone.now, help_text='创建时间')
    update = models.DateTimeField(auto_now=True, help_text='更新时间')

    class Meta:
        verbose_name = '地图Key'
        verbose_name_plural = '地图Key'

    def __str__(self):
        return "%s(%s)" % (self.map_key, self.create)
