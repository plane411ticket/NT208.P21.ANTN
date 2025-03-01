from django.urls import path
from comics import views

urlpatterns = [
    path('comics/', views.ComicListView.as_view(), name='comic-list'),
    path('comics/<int:pk>/', views.ComicDetailView.as_view(), name='comic-detail'),
    path('audio-comics/', views.AudioComicListView.as_view(), name='audio-comic-list'),
    path('stories/', views.StoryListView.as_view(), name='story-list'),
]