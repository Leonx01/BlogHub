from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    audited = models.BooleanField(default=False)
    def __str__(self):
        if len(self.text)<50:
            return self.text
        else:
            return self.text[:50]+"..."