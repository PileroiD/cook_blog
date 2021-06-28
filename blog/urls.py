from django.urls import path

from . import views

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
]