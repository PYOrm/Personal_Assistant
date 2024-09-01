from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import File
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required
from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth, UploadFileAttributes, UploadFileAttributesParentField
import os 
import uuid

token:str=os.getenv('FILESHARE_API_KEY')
auth: BoxDeveloperTokenAuth = BoxDeveloperTokenAuth(token=token)
client: BoxClient = BoxClient(auth=auth)

@login_required
def index(request):
    category = request.GET.get('category')
    if category:
        files = File.objects.filter(category=category, user=request.user)
    else:
        files = File.objects.filter(user=request.user)

    return render(request, 'fileshare.html', {'files': files, 'selected_category': category})

  
@login_required
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file=request.FILES['file']
            box_file_name=str(uuid.uuid4())
            client.uploads.upload_file(
                UploadFileAttributes(name=box_file_name, parent=UploadFileAttributesParentField(id='0')),
                file=file)
            for item in client.folders.get_folder_items('0').entries:
                print(item.name)
            File.objects.create(
                file_name=file.name,
                box_file_name=box_file_name, 
                user=request.user, 
                category=request.POST.get('category'))
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

