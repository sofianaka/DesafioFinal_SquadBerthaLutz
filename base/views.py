from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Postagens
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Postagens.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'base/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Postagens, pk=pk)
    return render(request, 'base/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'base/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Postagens, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'base/post_edit.html', {'form': form})