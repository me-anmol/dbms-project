from django.contrib import admin
from .models import destination,userinfo,hotel,registeration,travel

# Register your models here.

admin.site.register(destination)
admin.site.register(userinfo)
admin.site.register(hotel)
admin.site.register(registeration)
admin.site.register(travel)