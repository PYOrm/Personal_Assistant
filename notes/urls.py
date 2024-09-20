from django.urls import path

from .views import AddNoteView, NoteDetailView, NotesView, AddTagView, EditNoteView, DeleteNoteView

app_name = "notes"

urlpatterns = [
    path('', NotesView.as_view(), name='notes'),
    path('create_tag/', AddTagView.as_view(), name='create_tag'),
    path('create_note/', AddNoteView.as_view(), name='create_note'),
    path('edit_note/<int:pk>/', EditNoteView.as_view(), name='edit_note'),
    path('delete_note/<int:pk>/', DeleteNoteView.as_view(), name='delete_note'),
    path('detail_note/<int:pk>/', NoteDetailView.as_view(), name='detail_note'),
    
]