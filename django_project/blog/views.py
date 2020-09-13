from django.shortcuts import render, get_object_or_404
from .models import Post, Announcements, Query

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone
# Create your views here.




class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
    # <app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    # <app>/<model>_<form>.html

    def get_form(self, form_class=None):
        form = super(PostCreateView, self).get_form(form_class)
        form.fields['image'].required = False
        return form


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    # <app>/<model>_<form>.html

    def form_valid(self, form):
        form.instance.date_edited = timezone.now()
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class AnnouncementListView(ListView):
    model = Announcements
    context_object_name = 'announcement'

class AnnouncementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Announcements
    fields = ['title', 'content']
    # <app>/<model>_<form>.html

    def form_valid(self, form):
        form.instance.super_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcements
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.super_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        announcement_post = self.get_object()
        return self.request.user == announcement_post.super_author


class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcements
    success_url = '/announcement/'

    def test_func(self):
        announcement_post = self.get_object()
        return self.request.user == announcement_post.super_author


class QueryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Query
    fields = ['subject', 'content']
    template_name = 'blog/about.html'
    success_message = f'Query has been submitted!'
    # <app>/<model>_<form>.html

    def form_valid(self, form):
        # mail_admins(form.instance.subject, form.instance.content)
        form.instance.sent_by = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})


