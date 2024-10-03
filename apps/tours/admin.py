from django.contrib import admin
from apps.tours.models import (Country,
                               Destination,
                               Tour,
                               Category,
                               Food,
                               Hotel,
                               HotelFacility,
                               TourReview)


admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Hotel)
admin.site.register(HotelFacility)
admin.site.register(TourReview)
