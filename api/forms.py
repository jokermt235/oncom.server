from django import forms
from django.conf import settings
import os

class UploadFileForm(forms.Form):
    file = forms.FileField()
    def handle_uploaded_file(self, request):
        #Creates directories  on memory
        try:
            os.makedirs(settings.MEDIA_PATH + str(request.user.id))
        except Exception as exc:
            #if directory exists simply pass
            pass
        filepath = settings.MEDIA_PATH + str(request.user.id) + "/" + request.FILES["file"].name
        with open( filepath , 'wb+') as destination:
            for chunk in request.FILES["file"].chunks():
                destination.write(chunk)
        return { "name" : request.FILES["file"].name, "size" :  os.stat(filepath).st_size, "mimetype" : request.FILES["file"].content_type, "url" : "document/view/" +  request.FILES["file"].name, "user_id" : request.user.id}
