from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': "Say something..."}))

    class Meta:
        model = Post
        fields = ('content', 'image')


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}))

    class Meta:
        model = Comment
        fields = ('comment',)
        widget = {
            'text': forms.TextInput(attrs={
                'id': 'post-text',
                'required': True,
                'placeholder': 'Say something...'
            }),
        }
