from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Question(models.Model):

	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('data publicada')


	def __str__(self):
		return self.question_text


	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days = 1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.booleanl = 'True'
	was_published_recently.short_description = 'Publicado Recentemente?'


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)


	def __str__(self):

		return self.choice_text