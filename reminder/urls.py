from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('list/', views.ListReminders.as_view()),
    path('add/', csrf_exempt(views.ListReminders.as_view())),
    path('delete/', csrf_exempt(views.ListReminders.as_view()))
]
