from django.contrib import admin
from .models import *
class PincodeAdmin(admin.ModelAdmin):
    pass
class DiaglistAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pincode, PincodeAdmin)
admin.site.register(Diaglist, DiaglistAdmin)
# Register your models here.
