from django.contrib import admin

from .models import User, Vehicle, Footprint, Race, Profile

# Register your models here.
admin.site.register(User)
admin.site.register(Footprint)
admin.site.register(Vehicle)
admin.site.register(Profile)
admin.site.register(Race)

