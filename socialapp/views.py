from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, ListView

from posts.models import Post, Comment
from .forms import RegisterForm, LoginForm, ProfileForm

from .models import Profile, Relationship


class SignUp(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'SignUp.html'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            profile, created = Profile.objects.get_or_create(user=user)

        return redirect('/socialapp/signin')


class UserLogin(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'SignIn.html', context)

    def post(self, request):
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/posts/timeline')
        else:
            return render(request, 'SignIn.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/socialapp/signin')


class ProfileDetailView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile.html'
    success_url = '/posts/timeline'


class ProfileView(DetailView):
    model = Profile
    template_name = 'profileview.html'


class ListFriends(ListView):
    model = Profile
    template_name = 'friends.html'
    context_object_name = 'users'

    def get_queryset(self):
        return Profile.objects.exclude(user=self.request.user)


class SendRequest(View):
    def get(self, request, id, *args, **kwargs):
        sender = self.request.user.profile
        receiver = Profile.objects.get(id=id)
        friend_request, created = Relationship.objects.get_or_create(sender=sender, receiver=receiver, status='sent')

        return HttpResponse('friend request sent')

        return render(request, 'friends.html')


# def accept_friend_request(request):
#     friend_request = Relationship.objects.get(receiver=request.user.profile)
#     if friend_request.receiver == request.user:
#         friend_request.receiver.friends.add(friend_request.sender)
#         friend_request.sender.friends.add(friend_request.receiver)
#         friend_request.delete()
#         return HttpResponse('Friend request accepted')
#     else:
#         return HttpResponse('friend request not accepted')
#
#     return render(request, 'requests.html')

class ListRequests(ListView):
    model = Relationship
    template_name = 'requests.html'
    context_object_name = 'friend_requests'

    def get_queryset(self):
        return Relationship.objects.filter(receiver=self.request.user.profile)


class AcceptRequest(View):
    def get(self, request, id, *args, **kwargs):
        friend_request = Relationship.objects.get(id=id)
        friend_request.sender.user.friends.add(friend_request.receiver)
        friend_request.receiver.user.friends.add(friend_request.sender)
        if friend_request.status == 'sent':
            friend_request.status = 'accepted'
            friend_request.delete()
            return HttpResponse('friend request accepted')

        return render(request, 'requests.html')


class FriendList(ListView):
    model = Profile

    def get(self, request, id, *args, **kwargs):
        profile = Profile.objects.get(id=id)
        friends = profile.friends.all()
        context = {
            'friends': friends
        }

        return render(request, 'friendslist.html', context)

class Comments(CreateView):
    model=Comment
    def post(self, request, *args, **kwargs):
        comment=request.POST.get("comment")
        pid=kwargs.get("id")
        comments=self.model(user=self.request.user.profile,
                            post_id=pid,
                            comment=comment
                            )
        comments.save()


        return redirect("timeline")


