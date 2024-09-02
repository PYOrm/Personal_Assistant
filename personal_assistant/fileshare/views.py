from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import File
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required
from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth, UploadFileAttributes, UploadFileAttributesParentField
import os 
import uuid

def create_client():
    token=os.getenv('FILESHARE_API_KEY')
    auth: BoxDeveloperTokenAuth = BoxDeveloperTokenAuth(token=token)
    client: BoxClient = BoxClient(auth=auth)
    return client 

@login_required
def index(request):
    category = request.GET.get('category')
    if category:
        files = File.objects.filter(category=category, user=request.user)
    else:
        files = File.objects.filter(user=request.user)
    return render(request, 'files.html', {'files': files, 'selected_category': category})

  
@login_required
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file=request.FILES['file']
            client=create_client()
            upload_response=client.uploads.upload_file(
                UploadFileAttributes(name=str(uuid.uuid4()), parent=UploadFileAttributesParentField(id='0')),
                file=file)
            for item in client.folders.get_folder_items('0').entries:
                print(item.name)
            File.objects.create(
                file_name=file.name,
                box_file_id=str(upload_response.entries[0].id),
                user=request.user, 
                category=request.POST.get('category'))
            return redirect('fileshare:index')
    else:
        form = FileUploadForm()
    return render(request, 'files.html', {'form': form})
  
  
@login_required
def download(request, box_file_id):
    file = get_object_or_404(File, box_file_id=box_file_id)
    client=create_client()
    file_content=client.downloads.download_file(file_id=file.box_file_id)
    response = HttpResponse(file_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.file_name}"'
    return response
  
  
@login_required
def delete(request, box_file_id):
    file = get_object_or_404(File, box_file_id=box_file_id)
    client=create_client()
    client.files.delete_file_by_id(file.box_file_id)
    file.delete()
    return redirect('fileshare:index')

# remove this endpoint on production
# it is a hack to update box dev token in a quick way
def update_dev_token(request):
    os.environ['FILESHARE_API_KEY'] = request.GET.get('token')
