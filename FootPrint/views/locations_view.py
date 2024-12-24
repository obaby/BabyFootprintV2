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

from FootPrint.utils.baidu_map_api import get_location_cordinate
from FootPrint.utils.json_response import DetailResponse, ErrorResponse
from FootPrint.utils.request_util import get_request_data
from django.shortcuts import render


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        # fields = "__all__"



class LocationCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = []
    create_serializer_class = LocationCreateUpdateSerializer
    update_serializer_class = LocationCreateUpdateSerializer

    def get_my_locations(self, request):
        '''
        url:
        '''
        # print(Location.objects.all())
        data = self.get_serializer(Location.objects.all(), many=True).data
        return DetailResponse(data)

    def process_location_cordinate(self, request):

        baidu_key_set = MapKey.objects.filter(server_key__isnull=False).last()
        if baidu_key_set is None:
            return ErrorResponse(msg='请先配置百度地图服务端 key')

        locations = Location.objects.all()
        successed = []
        for l in locations:
            if l.latitude is None or l.lontitude is None:
                lng,lat = get_location_cordinate(l.name, baidu_key_set.server_key)
                if lng is not None and lat is not None:
                    l.latitude = lat
                    l.lontitude = lng
                    l.save()
                    print(l)
                    successed.append(l)
        return DetailResponse(self.get_serializer(successed, many=True).data)

    def index_page(self, request):
        # raise PermissionDenied
        # return HttpResponse
        key = ''
        if MapKey.objects.last():
            key = MapKey.objects.last().map_key
        context = {
            'map_key': key,
        }
        return  render(request, 'index.html', context)
