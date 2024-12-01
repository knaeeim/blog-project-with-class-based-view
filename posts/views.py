from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                messages.success(request, "Post added successfully")
                return redirect('home')
        else:
            form = PostForm()
        return render(request, "add_post.html", {'form': form})
    
# Add Post Class Based View Version
@method_decorator(login_required, name="dispatch")
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post added successfully")
        return super().form_valid(form)
    

@login_required
def edit_post(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=id)
        # print(post)
        form = PostForm(instance=post)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                messages.success(request, "Post updated successfully")
                return redirect('home')
        return render(request, "edit_post.html", {'form': form})
    
# Edit Post Class Based View Version
@method_decorator(login_required, name="dispatch")
class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "edit_post.html"
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully")
        return super().form_valid(form)




@login_required
def delete_post(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=id)
        # print(post)
        messages.success(request, "Post deleted successfully")
        post.delete()
        return redirect('home')
    
# Delete Post Class Based View Version
@method_decorator(login_required, name="dispatch")
class DeletePost(DeleteView):
    model = Post
    # form_class = PostForm
    template_name = "delete.html"
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Post deleted successfully")
        return super().form_valid(form)
    
class DetailsPostView(DetailView):
    model = Post
    template_name = "post_details.html"
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        form = CommentForm(self.request.POST)
        post = self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post # Assign the post to the comment
            new_comment.save()
            messages.success(self.request, "Comment added successfully")
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        form = CommentForm()
        context['comments'] = comments
        context['form'] = form
        return context