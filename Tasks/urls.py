from django.contrib import admin
from django.urls import path, include
from todo import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.TodoView.as_view(), name="todo"),
    path('todoall/', views.TodoAllView.as_view(), name='todoall'),
]
