from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    return render(request, 'index.html')
def about_view(request):
    return render(request, 'about.html')

def save_data_view(request):
    print(request.POST)
    title = request.POST.get("Title","")
    description = request.POST.get("Description","")

    return HttpResponse(f"data save Title = {title} Description = {description}")