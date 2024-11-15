from django.shortcuts import render,HttpResponse

from regi.forms import RegiForm
from .models import Person,Hobbies,Marks,Todo
# Create your views here.
def register(request):
    return HttpResponse("<html><body>HI, this is a response</body></html>")



def registration(request):
    if request.method == "POST":
        name=request.POST['username']
        email = request.POST['email']
        print(name)
        ins=Person(username=name,email=email)
        ins.save()
        print("Success")
    context = {"website":"Amrita","course":"Full stack development"}
    return render(request,'register.html',context)

def hobbies(request):
    if request.method == "POST":
        username=request.POST['username']
        hobbies = request.POST['hobbies']
        ins=Hobbies(username=username,hobbies=hobbies)
        ins.save()
        print("Success")
    context = {"website":"Amrita","course":"Full stack development"}    
    return render(request,'hobbies.html',context)

def marks(request):
    if request.method == "POST":
        username=request.POST['username']
        marks = request.POST['marks']
        ins=Marks(username=username,marks=marks)
        ins.save()
        print("Success")
    context = {"website":"Amrita","course":"Full stack development"}       
    return render(request,'marks.html',context)

def todo(request):
    if request.method == "POST":
        task=request.POST['task']
        description = request.POST['description']
        ins=Todo(task=task,description=description)
        ins.save()
        print("Success")    
    context = {"website":"Amrita","course":"Full stack development"}    
    return render(request,'todo_form.html',context)

def todo_list(request):
    todo = Todo.objects.all()  
    context = {
        'lists': todo
    } 
    return render(request,'todo.html',context)


def data(request):
    persons = Person.objects.all()  
    context = {
        'persons': persons
    }
    return render(request, 'data.html', context)

# def edit(request):
#     reg=RegiForm()
#     return render(request,"edit.html",{"regi1":reg})

def email_data(request):
    persons = Person.objects.all()  
    context = {
        'persons': persons
    }
    return render(request, 'data.html', context)



def edit(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        try:
            person = Person.objects.get(username=username)
            person.email = email  # Update the email or any other fields as needed
            person.save()
            print("Update Success")
        except Person.DoesNotExist:
            print("Person not found")
    reg = RegiForm()
    return render(request, "edit.html", {"regi1": reg})

def edit_email(request,username):
    row_to_edit = Person.objects.get(username=username)
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        try:
            person = Person.objects.get(username=username)
            person.email = email  # Update the email or any other fields as needed
            person.save()
            print("Update Success")
        except Person.DoesNotExist:
            print("Person not found")

    reg = RegiForm(instance=row_to_edit)
    return render(request, "edit.html", {"regi1": reg})

def delete_email(request, username):
    try:
        person = Person.objects.get(username=username)
        person.delete()  # Delete the person object
        print("Delete Success")
    except Person.DoesNotExist:
        print("Person not found")

    persons = Person.objects.all()  
    context = {
        'persons': persons
    }
    return render(request, 'data.html', context)