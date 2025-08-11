from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    paginate_by = 12
    template_name = 'catalog/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        status = self.request.GET.get('status', '')
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(author__icontains=q) |
                Q(description__icontains=q) |
                Q(isbn__icontains=q)
            )
        if status:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q', '')
        ctx['status'] = self.request.GET.get('status', '')
        return ctx

class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'catalog/book_form.html'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'catalog/book_form.html'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'catalog/book_confirm_delete.html'
    success_url = reverse_lazy('catalog:book-list')
