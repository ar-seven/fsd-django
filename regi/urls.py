from django.contrib import admin
from django.urls import path,include
from regi import views

urlpatterns =[
    path("new/",views.register,name="r"),
    path("registration/",views.registration,name="r"),
    path("hobbies/",views.hobbies,name="r"),
    path("marks/",views.marks,name="r"),
    path("data/",views.data),
    path("todo/",views.todo),
    path("todo_list/",views.todo_list),
    path("edit/",views.edit)
]