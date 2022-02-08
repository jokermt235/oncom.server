from django.contrib import admin
from .models import *
class PincodeAdmin(admin.ModelAdmin):
    pass
class DiaglistAdmin(admin.ModelAdmin):
    pass
class QuestionAdmin(admin.ModelAdmin):
    pass
class ResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pincode, PincodeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Diaglist, DiaglistAdmin)
admin.site.register(Result, ResultAdmin)
# Register your models here.
