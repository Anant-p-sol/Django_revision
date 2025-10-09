from django.shortcuts import render, redirect, get_object_or_404
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
    title = request.POST.get("Title","").strip()
    description = request.POST.get("Description","").strip()

    if not title and not description:
        messages.error(request, "Both Title and Description cannot be empty.")
        return redirect('home')

    note = Note(title=title, description=description)
    note.save()
    messages.success(request, "Data saved successfully.")
    return redirect('home')

def delete_view(request , id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    messages.success(request, "Delete success.")
    return redirect('home')
    
def updateview(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        title = request.POST.get("Title","").strip()
        description = request.POST.get("Description","").strip()

        if not title and not description:
            messages.error(request, "Both Title and Description cannot be empty.")
            return redirect('updateview_data', id=id)

        note.title = title
        note.description = description
        note.save()
        messages.success(request, "Note updated successfully.")
        return redirect('home')

    # GET -> render edit form with current note
    return render(request, 'component/edit_page.html', {"note": note})