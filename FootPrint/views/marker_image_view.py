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


class MarkerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkerImage
        fields = '__all__'
        # fields = "__all__"



class MarkerImageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkerImage
        fields = "__all__"


class MarkerImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MarkerImage.objects.all()
    serializer_class = MarkerImageSerializer
    permission_classes = []
    create_serializer_class = MarkerImageCreateUpdateSerializer
    update_serializer_class = MarkerImageCreateUpdateSerializer
