from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Note, Tag
from .forms import NoteForm, TagForm, TagFilterForm
from django.contrib.auth.mixins import LoginRequiredMixin

class NotesView(LoginRequiredMixin, ListView):
    login_url = "/users/login/"
    model = Note
    template_name = 'notes/notes.html'
    context_object_name = 'notes'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        search_query = self.request.GET.get('search')
        user = self.request.user
        
        # Фільтрація за користувачем
        queryset = queryset.filter(user=user)
        
        if tag:
            queryset = queryset.filter(tags__id=tag)
        
        if search_query:
            queryset = queryset.filter(body__icontains=search_query)
        
        return queryset.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TagFilterForm(self.request.GET)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class AddTagView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Tag
    template_name = 'notes/create_tag.html'
    success_url = reverse_lazy('notes:create_tag')
    form_class = TagForm

class AddNoteView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Note
    template_name = 'notes/create_note.html'
    success_url = reverse_lazy('notes:notes')
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditNoteView(LoginRequiredMixin, UpdateView):
    login_url = "/users/login/"
    model = Note
    template_name = 'notes/edit_note.html'
    success_url = reverse_lazy('notes:notes')
    form_class = NoteForm

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class DeleteNoteView(LoginRequiredMixin, DeleteView):
    login_url = "/users/login/"
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('notes:notes')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteDetailView(LoginRequiredMixin, DetailView):
    login_url = "/users/login/"
    model = Note
    template_name = 'notes/detail_note.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)