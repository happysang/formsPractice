from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlogForm

def index(request):
    return render(request, 'formscrud/index.html')

def create(request):
    if request.method == 'POST':
        form = NewBlogForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = NewBlogForm()
        return render(request, 'formscrud/create.html', {'form':form})

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'formscrud/crud.html', {'blogs':blogs})


def update(request,pk):
    blog = get_object_or_404(Blog, pk = pk)
    form = NewBlogForm(request.POST, instance=blog)
    if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'formscrud/create.html', {'form':form})

def delete(request,pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

