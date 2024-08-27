from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import File

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'fileshare/upload_file.html', {'form': form})

@login_required
def file_list(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'fileshare/file_list.html', {'files': files})
