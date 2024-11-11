from django.shortcuts import render,HttpResponse
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