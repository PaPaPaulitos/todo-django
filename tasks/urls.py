from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld,name='hello-world'),
    path('yourname/<str:name>',views.yourName,name='your-name'),
    path('', views.tasksList,name='tasks-list'),
    path('task/<int:id>',views.taskView,name="task-view"),
    path('changestatus/<int:id>',views.changeStatus,name="change-status"),
    path('newtask/',views.newTask,name="new-task"),
    path('edit/<int:id>',views.editTask,name='edit-task'),
    path('delete/<int:id>',views.deleteTask,name='delete-task')
]
