from django.contrib.auth.models import User

from django.db import models

from socialproject.common.abstract_models import AbstractClass


class Profile(AbstractClass):
    MALE = 'male'
    FEMALE = 'female'
    TRANSGENDER = 'transgender'
    OTHERS = 'others'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (TRANSGENDER, 'Transgender'),
        (OTHERS, 'Others'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio ...", max_length=300)

    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True)
    image = models.ImageField(upload_to='avatar', default="avatar/default.png")
    friends = models.ManyToManyField(User, related_name='friends')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.first_name


class Relationship(AbstractClass):
    SENT = 'sent'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS = [
        (SENT, 'Sent'),
        (ACCEPTED, 'Accepted'),
        (REJECTED,'Rejected')

    ]
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=10, choices=STATUS, null=True)

    class Meta:
        unique_together = [('sender', 'receiver')]
