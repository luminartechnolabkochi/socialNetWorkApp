from django.contrib.auth.models import User
from django.core.serializers import json
from django.http import request, HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, FormView, DetailView, TemplateView

from socialapp.models import Profile
from .models import Post, Comment
from .forms import PostForm, CommentForm

# rest imports
from rest_framework .views import APIView
from rest_framework .response import Response


class PostListView(TemplateView):
    model = Post

    def get(self, request, *args, **kwargs):
        friends_list=list(self.request.user.profile.friends.all().values_list("profile__id",flat=True))

        posts = Post.objects.filter(author_id__in=friends_list)

        form = PostForm()
        context = {
            'posts': posts,
            'form': form
        }
        return render(request, 'timeline.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all()

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user.profile
            new_post.save()

        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'timeline.html', context)







class MyPosts(ListView):
    model = Post
    template_name = 'postdetail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.profile)


class AddLike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        # is_dislike = False
        #
        # for dislike in post.dislikes.all():
        #     if dislike == request.user.profile:
        #         is_dislike = True
        #         break
        #
        # if is_dislike:
        #     post.dislikes.remove(request.user.profile)

        # is_like = False
        is_like=True

        for like in post.likes.all():
            if like == request.user.profile:
                is_like = False
                break

        if  is_like:
            post.likes.add(request.user.profile)

        if not is_like:
            post.likes.remove(request.user.profile)

        next = request.POST.get('next', '/')
        post_like_count=post.likes.all().count()
        print(post_like_count)
        return HttpResponseRedirect(next)


class AddDislike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user.profile:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user.profile)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user.profile:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user.profile)

        if is_dislike:
            post.dislikes.remove(request.user.profile)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class AddRestLike(APIView):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user.profile:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user.profile)

        is_like = False

        for like in post.likes.all():
            if like == request.user.profile:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user.profile)

        if is_like:
            post.likes.remove(request.user.profile)

        next = request.POST.get('next', '/')
        print(post.likes.all().count())
        return Response({"message":"hello"})
