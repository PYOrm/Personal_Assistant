from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import NoteForm, TagForm

from .models import Note, Tag

class NotesView(ListView):
    model = Note
    template_name = 'notes/notes.html'
    context_object_name = 'notes'

class AddTagView(CreateView):
    model = Tag
    template_name = 'notes/create_tag.html'
    success_url = reverse_lazy('notes')
    form_class = TagForm

class AddNoteView(CreateView):
    model = Note
    template_name = 'notes/create_note.html'
    success_url = reverse_lazy('notes')
    form_class = NoteForm

    

# Create your views here.