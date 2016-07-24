
# import other pieces of files
from django.db import models
from django.utils import timezone

# create an object called "post"
# models.Model tells Django that Post is a Django model, so it should be stored in the database
class Post(models.Model):
    # now we define the properties of the object
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # define a method that belongs to Post, called publish
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # this will give us a text tring with a Post title
    def __str__(self):
        return self.title
