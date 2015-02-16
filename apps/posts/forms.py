from django import forms
from .models import Post
from profiles.models import User


class LikePostForm(forms.Form):
    post_id = forms.CharField()
    user_id = forms.CharField()

    def clean_post_id(self):
        post_id = self.cleaned_data.get('post_id')
        return Post.objects.filter(id=post_id).exists()

    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        return User.objects.filter(id=user_id).exists()
