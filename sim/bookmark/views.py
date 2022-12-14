from django.shortcuts import render
from django.views.generic import *
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
# Create your views here.
class BookmarkLV(ListView):
    model =Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model =Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner = self.request.user)


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model =Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

#작성자만 삭제 할수 있도록
class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model =Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')