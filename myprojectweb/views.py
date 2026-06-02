from django.shortcuts import render, redirect
from .models import Register

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = Register.objects.get(username=username, password=password)
            return redirect('welcome')
        except:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        data = Register(
            name=request.POST['name'],
            gender=request.POST['gender'],
            qualification=request.POST['qualification'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        data.save()
        return redirect('login')
    return render(request, 'register.html')

def welcome(request):
    return render(request, 'welcome.html')
