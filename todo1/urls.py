from . import views
from django.urls import path

urlpatterns = [
    #add task
    path('addTask/',views.addTask,name='addTask'),
    #Mark as done
    path('mark_as_done/<int:pk>',views.mark_as_done,name='mark_as_done'),

    #EDIT Feature
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),

     #delete task
     path('delete_task/<int:pk>',views.delete_task,name='delete_task'),

]