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
class ProfileAdmin(admin.ModelAdmin):
    pass
class DocumentAdmin(admin.ModelAdmin):
    pass
class LogAdmin(admin.ModelAdmin):
    pass

#User proposal to update data from mobile application

class ProposalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Pincode, PincodeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Diaglist, DiaglistAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(LogItem, LogAdmin)
# Register your models here.
