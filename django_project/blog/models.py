from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_edited = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg', upload_to='post_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            print(self.image.path)
            img.save(self.image.path)

    @property
    def check_if_edited(self):
        result = self.date_edited - self.date_posted
        return result.seconds # returns seconds from difference of dates


class AnnouncementsQuerySet(models.QuerySet):
    def query_by_author(self, super_author):
        return self.filter(super_author=super_author)

class AnnouncementsManager(models.Manager):
    def get_queryset(self):
        return AnnouncementsQuerySet(self.model, using=self._db)

    def query_by_author(self, super_author):
        return self.get_queryset.queries(super_author)


class Announcements(models.Model):
    # should be always short and sweet
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_announced = models.DateTimeField(default=timezone.now)
    super_author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = AnnouncementsQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('announcements-list')



class Query(models.Model):
    # to get queries from users
    subject = models.CharField(max_length=100)
    content = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)




    def get_absolute_url(self):
        return reverse('blog-about')
