from django.db import models
from django.urls import reverse

class Goal(models.Model):
  name= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  category = models.TextField(max_length=50)
  priority = models.BooleanField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('goal-detail', kwargs={'goal_id': self.id})