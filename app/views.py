from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Note

# Create your views here.
def home_view(request):
    notes = Note.objects.all()
    return render(request, 'index.html', context ={
        "notes":notes
    })
def about_view(request):
    return render(request, 'about.html')

def save_data_view(request):
    print(request.POST)
    title = request.POST.get("Title","")
    description = request.POST.get("Description","")

    if not title and not description:
        messages.error(request, "Both Title and Description cannot be empty.")
        return redirect('home')

    note = Note(title=title, description=description)
    note.save()
    messages.success(request, "Data saved successfully.")
    return redirect('home')


def delete_view(request , id):
    note = Note.objects.get(id=id)
    note.delete()
    messages.success(request, "Delete success.")
    return redirect('home')