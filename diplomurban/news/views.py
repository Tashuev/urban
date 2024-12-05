from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required

@login_required
def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'update.html'
    form_class = ArticlesForm
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма неверна'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', data)