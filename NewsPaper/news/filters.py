from django_filters import FilterSet, ModelChoiceFilter,NumberFilter,DateFilter,DateFromToRangeFilter
from .models import Post, Category,Author
from django import forms
from django.db import models
from django_filters.widgets import RangeWidget


class PostFilter(FilterSet):
    postcategory = ModelChoiceFilter(
        field_name= 'catygorys',
        queryset= Category.objects.all()
    )
    #date = DateFilter(label='Дата создания статьи')


    #release_year__lt = DateFilter(field_name='date')
    release_year__lt = DateFromToRangeFilter(label='Дата создания статьи',widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))
    #release_year__lt = DateFilter(field_name='date',label='Дата создания статьи', lookup_expr='date__lt')

    class Meta:
        model = Post
        fields = {
           #'catygorys':['exact'],
           'header': ['contains'],
           'auther': ['exact'],
        }
