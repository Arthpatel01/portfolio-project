import os

from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView

from portfolio.models import ContactMe


# Create your views here.

class IndexView(CreateView):

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home1.html', context)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', None)
        msg = ""
        code = ''
        if action == 'contact-me-submit':
            try:
                data = {}
                name = request.POST.get('full-name', None)
                email = request.POST.get('email', None)
                phone = request.POST.get('phone-number', None)
                subject = request.POST.get('subject', None)
                budget = request.POST.get('budget', None)
                message = request.POST.get('message', None)

                if name:
                    data['name'] = name
                if email:
                    data['email'] = email
                if phone:
                    data['phone'] = phone
                if subject:
                    data['subject'] = subject
                if budget:
                    data['budget'] = budget
                if message:
                    data['message'] = message
                if 'file' in request.FILES:
                    attachment = request.FILES['file']
                    if attachment:
                        data['attachment'] = attachment

                if data:
                    ContactMe.objects.create(**data)
                    msg = "Saved Successfully!!"
                    code = "success"
                else:
                    msg = "Please enter required values"
                    code = "error"
            except Exception as e:
                print('E:', e)
                msg = "Something went wrong!!"
                code = "error"
            finally:
                return JsonResponse({'msg': msg, 'code': code}, status=200)


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
