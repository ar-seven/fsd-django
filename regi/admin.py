from django.contrib import admin

from regi.models import Person,Marks,Hobbies,Todo

# Register your models here.
admin.site.register(Person)
admin.site.register(Marks)
admin.site.register(Hobbies)
admin.site.register(Todo)