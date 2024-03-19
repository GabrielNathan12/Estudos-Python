from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from blog.models import Post, Page
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView

PAGES = 9

class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    ordering = '-pk',
    paginate_by = PAGES

    queryset = Post.objects.get_published()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Home - '
        })

        return context
     

class CreatedByListView(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__temp_context: dict[str, Any] = {}
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        user = self.__temp_context['user']
        user_full_name = user.username

        if user.first_name:
            user_full_name = f'{user.first_name} {user.last_name}'
        
        page_title = 'Posts de ' + user_full_name + ' - '
        
        context.update({
            'page_title': page_title
        })

        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = qs.filter(created_by__pk=self.__temp_context['user'].pk)

        return qs
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        id = self.kwargs.get('id')
        user = User.objects.filter(pk=id).first()
        
        if user is None:
            return redirect('blog:index')
        
        self.__temp_context.update({
            'id': id,
            'user': user
        })

        return super().get(request, *args, **kwargs)
    

class CategoryListView(PostListView):
    allow_empty = False
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(category__slug=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        page_title = f'{self.object_list[0].category.name} - Categoria -'
        context.update({
            'page_title': page_title
        })
        return context
    
class TagListView(PostListView):
    allow_empty = False
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(tags__slug=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        page_title = f'{self.object_list[0].tags.first().name} - Tags -'
        context.update({
            'page_title': page_title
        })
        return context

class SearchListView(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__search_value = ''
    
    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self.__search_value = request.GET.get('search','').strip()
        return super().setup(request, *args, **kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        posts = (
            Post.objects.get_published()
            .filter(
                Q(title__icontains=self.__search_value) |
                Q(excerpt__icontains=self.__search_value) |
                Q(content__icontains=self.__search_value)
            )[:PAGES]
        )
        
        return super().get_queryset()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context.update({
            'page_title': f'{self.__search_value[:30]} - Search -',
            'search_value': self.__search_value
            })
        
        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.__search_value == '':
            return redirect('blog:index')
        return super().get(request, *args, **kwargs)

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/pages/page.html'
    slug_field = 'slug'
    context_object_name = 'page'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        page = self.get_object()
        page_title = f'{page.title} - Página - '

        context.update({
            'page_title': page_title
        })

        return context
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/pages/post.html'
    slug_field = 'slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        page_title = f'{post.title} - Post - '

        context.update({
            'page_title': page_title
        })

        return context
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)

