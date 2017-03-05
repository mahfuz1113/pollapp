import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.


class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""was_published_recently() should return False for
		questions whose pub_date is in future."""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_receltly() should return True for questions whose pub_date is within last day.
		"""
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)
