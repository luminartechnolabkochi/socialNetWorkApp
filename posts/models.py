from django.db import models

from socialproject.common.abstract_models import AbstractClass
from socialapp.models import Profile


class Post(AbstractClass):
    content = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(Profile, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='dislikes')

    class Meta:
        ordering = ['-created']

    def __str(self):
        return self.author


class Comment(AbstractClass):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    # parent=models.ForeignKey('self',on_delete=models.CASCADE)


