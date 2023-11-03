from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('yourname/<str:name>',views.yourName ),
    path('', views.tasksList,name='tasks-list'),
    path('task/<int:id>',views.taskView,name="task-view"),
    path('newtask/',views.newTask,name="new-task"),
    path('edit/<int:id>',views.editTask,name='edit-task'),
    path('delete/<int:id>',views.deleteTask,name='delete-task')
]
