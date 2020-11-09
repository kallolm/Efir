from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django_pandas.io import read_frame
import pandas as pd
from django.conf import settings


@login_required
def upload(request):
    print("in here ")

    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            handle_uploaded_file(request.FILES['file'])
            df = readcsv()

            # return HttpResponse(df.to_html())
        return TemplateResponse(request, 'upload.html', {"tables": df.to_html()})
    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})


@login_required
def checkfile(request):
    print("in here checklist")
    return render(request, "uploadfile.html")


def handle_uploaded_file(f):
    with open('name.txt', 'wb+') as destination:
        print(destination)
        for chunk in f.chunks():
            destination.write(chunk)


def readcsv():
    file_ = open('name.txt')
    return pd.read_csv(file_)
