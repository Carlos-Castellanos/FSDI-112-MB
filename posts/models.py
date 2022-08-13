# from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.  (DataBases)
class Post(models.Model): #inheritance
    title = models.CharField(max_length=256)   # composition
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # send "title" to 127/admin when show the database posts
        return self.title

    def get_absolute_url(self):  ## is executed when a form is used, resolves the error after the POST
        return reverse("post_detail",args=[self.id])