# app/admin.py
from django.contrib import admin
from .models import Booking
# app/admin.py
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'method', 'check_in', 'check_out', 'payment_status')
    list_filter = ('payment_status', 'check_in', 'check_out')
    search_fields = ('name', 'email', 'method')
    ordering = ('-check_in',)

admin.site.register(Booking, BookingAdmin)



# myapp/admin.py
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'message')
    search_fields = ('name', 'email')
