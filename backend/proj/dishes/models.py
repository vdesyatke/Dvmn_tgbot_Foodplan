from django.db import models


class Dishes(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    ingredients = models.TextField(verbose_name='Ingredients')
    recipe = models.TextField(verbose_name='Recipe')
    cooktime = models.IntegerField(verbose_name='Cooktime')
    images = models.FileField(verbose_name='Images', blank=True)
    # bad_for_diets =


    def __str__(self):
        return f'{self.name}, время приготовления {self.cooktime} минут'


