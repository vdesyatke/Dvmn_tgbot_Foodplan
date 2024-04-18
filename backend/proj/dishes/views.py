from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound
from random import choice
from . import models


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dishes
        fields = ['pk', 'name', 'ingredients', 'recipe', 'cooktime', 'images']


class RandomDish(APIView):
    def get(self, *args, **kwargs):
        all_dishes = models.Dishes.objects.all()
        random_dish = choice(all_dishes)
        serialized_random_dish = DishSerializer(random_dish, many=False)
        return Response(serialized_random_dish.data)


class AnotherRandomDish(APIView):
    def get(self, request, pk, format=None):
        other_dishes = models.Dishes.objects.exclude(pk=pk)
        another_random_dish = choice(other_dishes)
        if not another_random_dish:
            return HttpResponseNotFound
        serialized_dish = DishSerializer(another_random_dish, many=False)
        return Response(serialized_dish.data)

