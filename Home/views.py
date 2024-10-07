from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Post, PostImage
from .forms import PostForm


class SampleEditorView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "sampleeditor.html"
    success_url = reverse_lazy("sampleviewer")

    def form_valid(self, form):
        # Save the Post object first
        post = form.save()

        # Handle new files if any are uploaded
        files = self.request.FILES.getlist("images")
        for file in files:
            PostImage.objects.create(post=post, image=file)

        # Redirect after updating
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        # Add the post's existing images to the context for display in the template
        context = super().get_context_data(**kwargs)
        context["images"] = PostImage.objects.filter(post=self.object)
        return context


class ImageDeleteView(DeleteView):
    model = PostImage
    success_url = reverse_lazy("sampleviewer")  # Default redirect

    def get(self, request, *args, **kwargs):
        # Fetch the image to be deleted using its primary key (pk)
        self.object = get_object_or_404(PostImage, pk=self.kwargs["pk"])

        # Get the associated post to redirect to the post's edit page after deletion
        post = self.object.post

        # Delete the image and redirect to the post editor
        self.object.delete()
        return redirect("sampleeditor", pk=post.pk)


class DeleteSampleView(DeleteView):
    model = Post
    template_name = "deletesample.html"
    success_url = reverse_lazy("sampleviewer")


class SampleUploderView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "sampleuploder.html"
    success_url = reverse_lazy("sampleviewer")

    def form_valid(self, form):
        # Save the Post object first
        post = form.save()

        # Retrieve the files from the request
        files = self.request.FILES.getlist(
            "images"
        )  # 'images' is the form field for the files

        # Loop through the files and create PostImage for each
        for file in files:
            PostImage.objects.create(post=post, image=file)

        # Redirect after saving all images
        return redirect(self.success_url)


class SampleViewerView(ListView):
    model = Post
    template_name = "sampleviewer.html"
    ordering = ["-id"]


class SampleDetailView(DetailView):
    model = Post
    template_name = "sampledetails.html"


def home(request):
    return render(request, "home.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect("home")
        else:
            messages.error(request, ("There was an error, please try again"))
            return redirect("login")
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.error(request, ("You hane been logged out"))
    return redirect("login")
