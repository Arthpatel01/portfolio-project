import os

from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import CreateView


# Create your views here.

class IndexView(CreateView):

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home1.html', context)


def download_file(request, file_path):
    # Define the file path on your server
    file_path = ''

    # Extract the file name from the file path
    filename = os.path.basename(file_path)

    # Open the file for reading as binary
    with open(file_path, 'rb') as file:
        response = FileResponse(file)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
