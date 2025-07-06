from django.contrib import admin
from .models import CarMake, CarModel

# Inline class to show CarModel inside CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra empty forms

# Admin class for CarModel (optional customization)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_type', 'year', 'dealer_id', 'car_make')
    list_filter = ('car_type', 'year')
    search_fields = ('name',)

# Admin class for CarMake with CarModel inline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]

# Register the models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
