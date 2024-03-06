from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Goal 

# class Goal:
#   def __init__(self, name, description, category):
#     self.name = name
#     self.description = description
#     self.category = category

# def home(request):
#   return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def goal_index(request):
  goals= Goal.objects.all()
  return render(request, 'goals/index.html', { 'goals': goals })

def goal_detail(request, goal_id):
  goal = Goal.objects.get(id=goal_id)
  return render(request, 'goals/detail.html', { 'goal': goal })

class GoalCreate(CreateView):
  model = Goal
  fields = '__all__'
  success_url='/goals/'

class GoalUpdate(UpdateView):
  model = Goal
  fields = ['name', 'description', 'category','priority']

class GoalDelete(DeleteView):
  model = Goal
  success_url = '/goals/'

class Home(LoginView):
  template_name = 'home.html'