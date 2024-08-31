from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import File
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    category = request.GET.get('category')
    if category:
        files = File.objects.filter(category=category)
    else:
        files = File.objects.all()

    return render(request, 'fileshare.html', {'files': files})

  
@login_required
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fileshare:index')
    else:
        form = FileUploadForm()
    return render(request, 'fileshare.html', {'form': form})
  
  
@login_required
def download(request, file_id):
    file = get_object_or_404(File, id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response
  
  
@login_required
def delete(request, file_id):
    file = get_object_or_404(File, id=file_id)
    file.delete()
    return redirect('fileshare:index')

@login_required
def file_list(request):
    return render(request, 'file_list.html')

