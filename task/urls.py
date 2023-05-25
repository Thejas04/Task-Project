from django.urls import path
from .import views
from .views import login

app_task = "task"

urlpatterns = [
    path('',views.login, name='login'),
    path('taskdetails/',views.taskdetails, name='taskdetails'),
]
