from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

@login_required
def goal_index(request):
  goals = Goal.objects.filter(user=request.user)
  return render(request, 'goals/index.html', { 'goals': goals })

@login_required
def goal_detail(request, goal_id):
  goal = Goal.objects.get(id=goal_id)
  return render(request, 'goals/detail.html', { 'goal': goal })


class GoalCreate(LoginRequiredMixin, CreateView):
  model = Goal
  fields = ['name', 'description', 'category']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url='/goals/'

class GoalUpdate(LoginRequiredMixin, UpdateView):
  model = Goal
  fields = ['name', 'description', 'category','completed']

class GoalDelete(LoginRequiredMixin, DeleteView):
  model = Goal
  success_url = '/goals/'

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('goal-index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  