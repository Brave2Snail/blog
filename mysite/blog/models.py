from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class BlogArticles(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User, related_name='blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


