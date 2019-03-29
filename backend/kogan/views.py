# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework import status
# Create your views here.
from rest_framework.response import Response

from .utils import KoganFactory


class CategoryViewset(generics.ListAPIView):
    permission_classes = []
    queryset = []

    def list(self, request, category=None, *args, **kwargs):
        if not category:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        avg_cubic_weight, result_list = KoganFactory.get_average_weight_for_a_category(category)
        context = {
            'avg_cubic_weight': avg_cubic_weight,
            'result_list': result_list
        }
        return Response(data=context)
