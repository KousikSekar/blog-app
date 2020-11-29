from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.urls import reverse

=======
>>>>>>> f99a36e29daf09a57d73702899369a4393f9a6a1


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


=======
>>>>>>> f99a36e29daf09a57d73702899369a4393f9a6a1
