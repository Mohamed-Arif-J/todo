from ast import Delete
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from . models import Todo

# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        a= request.POST.get('username')
        b= request.POST.get('password')
        c= authenticate(username=a,password=b)
        if c:
            login(request, c)
            print("Login successful")
            return redirect('dashboard')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        d= request.POST.get('username')
        e= request.POST.get('password')
        User.objects.create_user(username=d, password=e)
        return redirect('login')
    return render(request, 'register.html')
    
def dashboard(request):
    c=Todo.objects.filter(user=request.user) 
    if request.method == 'POST' and request.POST.get('todo_id'):
        todo = get_object_or_404(Todo, id=request.POST.get('todo_id'), user=request.user)
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return redirect('dashboard')
    if request.method == 'POST':  
        a = request.POST.get('task')
        b = request.POST.get('date')
        Todo.objects.create(user=request.user,task = a , date = b)
        return redirect('dashboard')
    return render(request,'dashboard.html', {'c': c})
def logout_view(request):
    logout(request)
    print('logout successful')
    return redirect('login')
def delete_task(request,id):
    todo=Todo.objects.filter(id=id)
    todo.delete()
    return redirect('dashboard')
def update_task(request,id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        a = request.POST.get('task')
        b = request.POST.get('date')
        todo.task = a
        todo.date = b
        todo.save()
        return redirect('dashboard')
    return render(request,'update.html',{'todo': todo})


