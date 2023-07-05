from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(Enrollment)
admin.site.register(Blog)
admin.site.register(Review)
