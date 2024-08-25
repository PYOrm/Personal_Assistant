from django.urls import path

from .views import AddNoteView, NotesView, AddTagView

app_name = "notes"

urlpatterns = [
    path('', NotesView.as_view(), name='notes'),
    path('create_tag/', AddTagView.as_view(), name='create_tag'),
    path('create_note/', AddNoteView.as_view(), name='create_note')
    
]