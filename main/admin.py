from django.contrib import admin
from .models import destination,userinfo,hotel,registerations,travel,review

# Register your models here.

admin.site.register(destination)
admin.site.register(userinfo)
admin.site.register(hotel)
admin.site.register(registerations)
admin.site.register(travel)
admin.site.register(review)
