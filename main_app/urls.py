from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('goals/', views.goal_index, name='goal-index'),
  path('goals/<int:goal_id>/', views.goal_detail, name='goal-detail'),
   path('goals/create/', views.GoalCreate.as_view(), name='goal-create'),
   path('goals/<int:pk>/update/', views.GoalUpdate.as_view(), name='goal-update'),
  path('goals/<int:pk>/delete/', views.GoalDelete.as_view(), name='goal-delete'),
]