from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('list/', views.ToDoViewSet.as_view()),
    path('add/', csrf_exempt(views.ToDoViewSet.as_view())),
    path('delete/', csrf_exempt(views.ToDoViewSet.as_view())),
    path('task/list/', views.TaskViewSet.as_view()),
    path('task/add/', csrf_exempt(views.TaskViewSet.as_view())),
    path('task/delete/', csrf_exempt(views.TaskViewSet.as_view())),
    path('task/complete/', csrf_exempt(views.TaskComplete.as_view())),
]
