from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/todo/', include('todo.urls')),
    path('api/v1/reminder/', include('reminder.urls')),
]
