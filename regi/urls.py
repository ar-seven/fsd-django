from django.contrib import admin
from django.urls import path,include
from regi import views

urlpatterns =[
    path("new/",views.register,name="r"),
    path("registration/",views.registration,name="registration"),
    path("hobbies/",views.hobbies,name="r"),
    path("marks/",views.marks,name="r"),
    path("data/",views.data),
    path("todo/",views.todo),
    path("todo_list/",views.todo_list),
    path("edit/",views.edit),
    #new 
    path("view/",views.email_data),
    path("edit_email/<str:username>",views.edit_email,name='edit_email'),
    path("delete_email/<str:username>",views.delete_email,name='delete_email'),
    # path("edit_email/",views.edit,name='delete_email')
    
]