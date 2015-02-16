import factory
from .models import Post, Comment
from django.contrib.webdesign import lorem_ipsum
from profiles.models import User

class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    
    image = factory.django.ImageField(
        filename = "example.jpg",
        width = 400,
        height = 400,
        color = 'Blue',
        format = 'JPEG')

    @factory.lazy_attribute
    def user(self):
        return User.objects.get(id=1)

    #@factory.sequence
    #def link_original():
     #   return 'http://{}'.format(lorem_ipsum.words(1, False))

    @factory.post_generation
    def liked_users(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for liked_users in extracted:
                self.liked_users.add(liked_users)


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment




    @factory.lazy_attribute
    def user(self):
        return User.objects.all().order_by('?')[0]

    @factory.lazy_attribute
    def post(self):
        return Post.objects.all().order_by('?')[0]

    @factory.sequence
    def text(self):
        return lorem_ipsum.sentence()