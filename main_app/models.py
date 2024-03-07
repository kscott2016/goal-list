from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
  ('F', 'Family'),
  ('H', 'Health'),
  ('M', 'Financial'),
  ('S', 'Social'),
  ('E', 'Education'),
  ('C', 'Career'),
  ('G', 'Character Growth'),
)

class Goal(models.Model):
  name= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  # category = models.TextField(max_length=50)
  category= models.CharField(
    max_length=1,
    choices=CATEGORIES,
    default=CATEGORIES[0][0])
  completed = models.BooleanField(
    default = False
  )

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('goal-detail', kwargs={'goal_id': self.id})