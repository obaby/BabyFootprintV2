import json
from datetime import datetime, timedelta

from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from FootPrint.models import *

from django.utils.translation import gettext_lazy as _

from FootPrint.utils.json_response import DetailResponse, ErrorResponse
from FootPrint.utils.request_util import get_request_data
from django.shortcuts import render

from FootPrint.views.marker_image_view import MarkerImageSerializer


class MapSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapSetting
        fields = '__all__'
        # fields = "__all__"



class MapSettingCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapSetting
        fields = "__all__"


class MapSettingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MapSetting.objects.all()
    serializer_class = MapSettingSerializer
    permission_classes = []
    create_serializer_class = MapSettingCreateUpdateSerializer
    update_serializer_class = MapSettingCreateUpdateSerializer

    def get_my_settings(self, request):
        '''
        url:
        '''
        marker_settings = None
        if MarkerImage.objects.count()>0:
            marker_settings = MarkerImageSerializer(MarkerImage.objects.last()).data
        map_settings = None
        if MapSetting.objects.count()>0:
            map_settings = self.get_serializer(MapSetting.objects.last()).data
        data = {
            'marker': marker_settings,
            'map_setting': map_settings
        }
        return DetailResponse(data)

    def index_page(self, request):
        # raise PermissionDenied
        # return HttpResponse
        return  render(request, 'index.html')
