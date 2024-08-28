from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Note, Tag
from .forms import NoteForm, TagForm, TagFilterForm

class NotesView(ListView):
    model = Note
    template_name = 'notes/notes.html'
    context_object_name = 'notes'
    paginate_by = 6
    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tags__id=tag)
        return queryset.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TagFilterForm(self.request.GET)
        return context

class AddTagView(CreateView):
    model = Tag
    template_name = 'notes/create_tag.html'
    success_url = reverse_lazy('notes:create_tag')
    form_class = TagForm

class AddNoteView(CreateView):
    model = Note
    template_name = 'notes/create_note.html'
    success_url = reverse_lazy('notes:notes')
    form_class = NoteForm

class EditNoteView(UpdateView): 
    model = Note
    template_name = 'notes/edit_note.html'
    success_url = reverse_lazy('notes:notes')
    form_class = NoteForm

class DeleteNoteView(DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('notes:notes')

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/detail_note.html'
    context_object_name = 'note'