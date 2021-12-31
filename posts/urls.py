from django.urls import path


from .views import PostListView, MyPosts, AddLike, AddDislike,AddRestLike

urlpatterns = [
    path('timeline', PostListView.as_view(), name="timeline"),
    path('post/<int:pk>/like',AddLike.as_view(), name='like'),

    path('post/<int:pk>/dislike',AddDislike.as_view(), name='dislike'),
    path('myposts',MyPosts.as_view(), name="myposts"),
    path('post/like/<int:pk>',AddRestLike.as_view(),name="restlike")


]
