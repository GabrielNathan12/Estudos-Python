from django.urls import path
from blog.views import PostListView,PostDetailView, PageDetailView, CreatedByListView, CategoryListView, TagListView, SearchListView
app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('pages/<slug:slug>/', PageDetailView.as_view(), name='pages'),
    path('created_by/<int:id>/', CreatedByListView.as_view(), name='created_by'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('tag/<slug:slug>/', TagListView.as_view(), name='tag'),
    path('search/', SearchListView.as_view(), name='search'),

]

