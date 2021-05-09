from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import stickers
from .forms import NewPost
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



def homepage(request):
    return render(request, 'main/index.html')


def search(request):
    if request.method == 'POST':
        searched = request.POST['site_search']
        search_results = stickers.objects.filter(keywords__contains=searched.lower())
        return render(request, 'main/search_res.html', {'searched':searched,
                                                        'search_results':search_results})
    else:
        return render(request, 'main/search_res.html', {})


class Show(ListView):
    model = stickers
    template_name = 'main/shop.html'
    context_object_name = 'post'
    paginate_by = 9 # Пагинация

    # Передача контеста в шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class ProductDetail(DetailView):
    model = stickers
    template_name = 'main/detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = stickers.title
        return context

def CategoryView(request, cats):
    category_posts = stickers.objects.filter(cat=cats)
    return render(request, 'main/categ.html', {'cats':cats, 'category_posts':category_posts})


@login_required
def CreatePost(request):
    submitted = False
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('shop'))
    else:
        form = NewPost
        if 'suubmitted' in request.GET:
            submitted = True

    return render(request, 'main/create_post.html', {'form':form, 'submitted':submitted})