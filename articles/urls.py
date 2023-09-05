from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(),
         name='article_update'),
    path('<int:pk>/detail/', views.ArticleDetailView.as_view(),
         name='article_detail'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(),
         name='article_delete'),
    path('new/', views.ArticleCreateView.as_view(), name='article_create'),
]
