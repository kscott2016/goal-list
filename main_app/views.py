from django.shortcuts import render

class Goal:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, category):
    self.name = name
    self.description = description
    self.category = category


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def goal_index(request):
  return render(request, 'goals/index.html', { 'goals': goals })