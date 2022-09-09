from django.contrib import admin

# Register your models here.
from .models import Departmets, Doctors, Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')


admin.site.register(Departmets)
admin.site.register(Doctors)
admin.site.register(Booking,BookingAdmin)
