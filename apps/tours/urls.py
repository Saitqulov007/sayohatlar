from django.urls import path

from apps.tours.views import destinations, countries, hotel_detail, tour_detail, TurView

urlpatterns = [
    path('', TurView.as_view(), name='tours'),
    path('destinations/', destinations, name='destinations'),
    path('countries/', countries, name='countries'),
    path('<int:pk>/', tour_detail, name='tour_detail'),
    path('hotel/<int:pk>/', hotel_detail, name='hotel_detail'),
]
