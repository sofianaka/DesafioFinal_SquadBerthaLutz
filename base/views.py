from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Postagens


# Create your views here.
def post_list(request):
    posts = Postagens.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'base/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Postagens, pk=pk)
    return render(request, 'base/post_detail.html', {'post': post})