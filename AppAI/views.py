from django.shortcuts import render

# Create your views here.
import openai
from PIL import Image
import requests
from django.shortcuts import render

from portfolio_project.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_image(request):
    if request.method == "POST":
        text_input = request.POST.get('text_input')
        image_url = None
        prompt = None
        if text_input is not None:
            if '\n' in text_input:
                prompt = text_input
            else:
                features_input = request.POST.get('features_input')
                if features_input is not None:
                    prompt = f"{text_input}\n{features_input}"
                else:
                    prompt = text_input
            response = openai.Image.create(prompt=prompt, n=1, size="512x512")
            image_url = response['data'][0]['url']
        context = {'image_url': image_url, 'prompt': prompt}
        return render(request, "generate_img.html", context)
    else:
        context = {}
        return render(request, "generate_img.html", context)
