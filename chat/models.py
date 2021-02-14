from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Message(models.Model):
	author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
	context = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.author.username

	def last_15_messages(self):
		return Message.objects.order_by('-timestamp').all()[:15]
		
