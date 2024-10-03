from django_filters import FilterSet
from django import forms
from apps.tours.models import Tour


class TourFilter(FilterSet):
    class Meta:
        model = Tour
        fields = {'name': ['contains'], 'price': ['lte'],  'categories': [
            'exact'], 'countries': ['exact'], 'destinations': ['exact']}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'countries': forms.Select(attrs={'class': 'form-control'}),
            'destinations': forms.Select(attrs={'class': 'form-control'}),
        }
