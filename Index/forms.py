from .models import Upload
from django import forms
from Index.models import *

class UploadForm(forms.ModelForm):
 class Meta:
  model = Upload
  fields = '__all__'
  labels = {'Image':'Thumbnail','name':'Club Name','link':'Please enter last 11 digits of your youtube hyperlink'}
