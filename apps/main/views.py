from django.shortcuts import render

from apps.tours.models import Category, Destination, Tour


def home_view(request):
    destinations = Destination.objects.all()[:2]
    destinations2 = Destination.objects.all()[2:3].first()
    categories = Category.objects.all()[:5]

    tours = Tour.objects.all()[:5]
    return render(request, 'index.html', {'destinations': destinations,
                                          'destinations2': destinations2,
                                          'tours': tours,
                                          'categories': categories})
