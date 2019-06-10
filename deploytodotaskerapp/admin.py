from django.contrib import admin

# Register your models here.
from deploytodotaskerapp.models import Registration, Customer, Driver, Meal, Order, OrderDetails

admin.site.register(Registration)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetails)
