from django.contrib import admin
from .models import Post

# register the model to make it visible on the admin page
admin.site.register(Post)
