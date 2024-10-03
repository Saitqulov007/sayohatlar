from typing import Any
from django.shortcuts import render
from django_filters.views import FilterView
from apps.tours.filters import TourFilter
from apps.tours.models import Country, Destination, Hotel, Tour


def destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'tours/destinations.html', {'destinations': destinations})


def countries(request):
    countries = Country.objects.all()
    return render(request, 'tours/countries.html', {'countries': countries})


def tour_detail(request, pk):
    tour = Tour.objects.get(id=pk)
    tour.hit_count += 1
    tour.save()
    return render(request, 'tours/tour_detail.html', {'tour': tour})


def hotel_detail(request, pk):
    hotel = Hotel.objects.get(id=pk)

    return render(request, 'tours/hotel_detail.html', {'hotel': hotel})


class TurView(FilterView):
    model = Tour
    template_name = 'tours/tours.html'
    context_object_name = 'tours'
    filterset_class = TourFilter
    paginate_by = 6

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset_class
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', None)
        if search:
            qs = qs.filter(name__contains=search)
        return qs
