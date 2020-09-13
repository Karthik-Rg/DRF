from django.urls import path, include
from django_filters.views import FilterView

from .filters import PostFilter
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, \
    AnnouncementListView, AnnouncementCreateView, AnnouncementDeleteView, AnnouncementUpdateView, QueryCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('api/posts/', include("blog.api.urls"), name='blog-api'),
    path('announcement/', AnnouncementListView.as_view(), name='announcements-list'),
    path('announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcements-delete'),
    path('announcement/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcements-update'),
    path('announcement/new/', AnnouncementCreateView.as_view(), name='announcements-create'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', QueryCreateView.as_view(), name='blog-about'),
    path('search/', FilterView.as_view(filterset_class=PostFilter), name='searcher'),

]
