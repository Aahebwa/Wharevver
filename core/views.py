from django.shortcuts import render, redirect
from . import forms
from .models import Uploaded_file
# Create your views here.

def index(request):
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST':
        form = forms.fileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = forms.fileUploadForm()
    return render(request, 'upload.html', {'form':form})

def file_list(request):
    files = Uploaded_file.objects.all()
    return render(request, 'file_list.html', {'files':files})
