from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import State
from .serializers import StateSerializer

# Create your views here.
class StateDataCreate(generics.CreateAPIView):
    """
    Создание или проверка что существует
    """

    queryset = State.objects.all()
    serializer_class = StateSerializer

    def create(self, request, *args, **kwargs):
        try:
            user = State.objects.get(tg_name=request.data['tg_name'])
        except State.DoesNotExist:
            user = State.objects.create(tg_name=request.data['tg_name'])
            return JsonResponse({'user': user.tg_name, 'id': user.pk })
        return JsonResponse({'user': user.tg_name, 'id': user.pk })



class StateData(generics.RetrieveUpdateAPIView):
    """
      Обновление и получение данных
    """

    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'tg_name'

