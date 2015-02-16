from django.db import models

from sorl.thumbnail import ImageField
from django.conf import settings

class Post(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("profiles.user", related_name='posts')
    liked_users = models.ManyToManyField("profiles.user", related_name='Liked_posts')
    geolocation = models.CharField(max_length=150, blank=True)
    link_original = models.URLField(name="link original")
    attached = models.BooleanField(default=False)
    image = ImageField('image', upload_to=settings.MEDIA_ROOT, null=True, blank=True)

    def like_trigger(self, user):
        if user in self.liked_users.all():
            return self.liked_users.remove(user)
        return self.liked_users.add()

    def unlike(self, user):
        return self.liked_users.remove(user)

    @property 
    def likes(self):
        return self.liked_users.count()


class Comment(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("profiles.user", related_name='comments')
    post = models.ForeignKey(Post, related_name='comments')
    text = models.TextField("text")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"