
from django.urls import path


from .views import (PostCreateAPIView, PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView)
urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
]