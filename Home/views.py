from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post
from .forms import PostForm


class SampleEditorView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'sampleeditor.html'
    # fields = '__all__'
    # fields = ('title', 'body', 'link', 'image')


class DeleteSampleView(DeleteView):
    model = Post
    template_name = 'deletesample.html'
    success_url = reverse_lazy('sampleviewer')


class SampleUploderView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'sampleuploder.html'
    # fields = '__all__'
    # fields = ('title', 'body')


class SampleViewerView(ListView):
    model = Post
    template_name = 'sampleviewer.html'
    ordering = ['-id']


class SampleDetailView(DetailView):
    model = Post
    template_name = 'sampledetails.html'


def home(request):
    return render(request, 'home.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('sampleuploder')
        else:
            messages.error(request, ("There was an error, please try again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.error(request, ("You hane been logged out"))
    return redirect('login')
