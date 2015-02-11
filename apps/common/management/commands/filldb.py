import sys
import random

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from profiles.factories import AdminFactory, UserFactory
from posts.factories import PostFactory
from posts.factories import CommentFactory

class Command(BaseCommand):
    help = 'Fill the database with test fixtures'

    def handle(self, *args, **options):
        sys.stdout.write('Starting fill db\r\n')

        site = Site.objects.get(pk=1)
        site.domain = site.name = settings.DOMAIN
        site.save()

        AdminFactory()
        users = UserFactory.create_batch(50)
        posts = PostFactory.create_batch(20)
        for post in posts:
            likes = random.randint(1, 50)
            post.liked_users.add(*users[:likes])
        CommentFactory.create_batch(150)

        sys.stdout.write('Completed fill db\r\n')
