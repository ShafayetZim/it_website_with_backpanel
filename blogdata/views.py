from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import View
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required


@login_required()
class BgBlogList(ListView):
    model = BgBlog
    template_name = 'blog/blog_bg_list.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blog Bg List"
        context["nav_bar"] = "bg_blog"
        context['blog'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
class BgBlogUpdateView(SuccessMessageMixin, UpdateView):
    model = BgBlog
    form_class = BgBlogForm
    success_url = reverse_lazy('blog-bg-list')
    template_name = 'blog/blog_bg_update.html'
    success_message = "Bg was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Bg Information"
        context["nav_bar"] = "bg_blog"
        return context


@login_required()
class BlogList(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blog List"
        context["nav_bar"] = "blog"
        context['blog'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_blog(request):
    template_name = 'blog/blog_new.html'

    if request.method == 'GET':
        print("GET called")
        blog_form = BlogForm(None)

    elif request.method == 'POST':
        print("Post called")
        blog_form = BlogForm(request.POST, request.FILES)

        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.save()

            messages.add_message(request, messages.SUCCESS, 'New Blog Entry Successful')
            return redirect('blog-list')

        else:
            print("Not Valid Create Form")
            print(blog_form.errors)

    return render(request, template_name, {
        'blog_form': blog_form,
        'title': 'New Blog',
        'nav_bar': 'blog',
    })


@login_required()
class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog-list')
    template_name = 'blog/blog_update.html'
    success_message = "Blog was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Blog Information"
        context["nav_bar"] = "blog"
        return context


@login_required()
def blog_delete(request, id):
    if request.method == 'GET':
        instance = Blog.objects.get(id=id)
        Blog.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('blog-list')


@login_required()
class CommentList(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Comment List"
        context["nav_bar"] = "comment"
        context['comment'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_comment(request):
    template_name = 'blog/comment_new.html'

    if request.method == 'GET':
        print("GET called")
        comment_form = CommentForm(None)

    elif request.method == 'POST':
        print("Post called")
        comment_form = CommentForm(request.POST, request.FILES)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()

            messages.add_message(request, messages.SUCCESS, 'New Comment Entry Successful')
            return redirect('comment-list')

        else:
            print("Not Valid Create Form")
            print(comment_form.errors)

    return render(request, template_name, {
        'comment_form': comment_form,
        'title': 'New Comment',
        'nav_bar': 'comment',
    })


@login_required()
class CommentUpdateView(SuccessMessageMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comment-list')
    template_name = 'blog/comment_update.html'
    success_message = "Comment was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Comment Information"
        context["nav_bar"] = "comment"
        return context


@login_required()
def comment_delete(request, id):
    if request.method == 'GET':
        instance = Comment.objects.get(id=id)
        Comment.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('comment-list')
