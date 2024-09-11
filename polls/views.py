from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReceipesForm
from .models import Receipes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student
from django.core.paginator import Paginator

@login_required(login_url='/login/')

def index(request):
    peoples = [
        {'name': 'Kishore', 'age': 22},
        {'name': 'Ramya', 'age': 28},
        {'name': 'Saif', 'age': 32},
        {'name': 'Karthik', 'age': 24},
        {'name': 'Sagar', 'age': 23},
    ]
    fruits = ['Mango', 'banana', 'cherry', 'strawberry']
    return render(request, 'polls/index.html', context={'peoples': peoples, 'fruits': fruits})

def success(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")

def about(request):
    context = {'page': 'Django 2024 tutorial'}
    return render(request, 'polls/about.html', context)

def contact(request):
    context = {'page': 'Django 2024 tutorial'}
    return render(request, 'polls/contact.html', context)

def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipes.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

        return redirect('/receipes/')

    queryset = Receipes.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))

    # Check if the user is authenticated
    if request.user.is_authenticated:
        current_username = request.user.username
    else:
        current_username = None  # Or set a default value
    return render(request, 'polls/receipes.html', context={'receipes': queryset, 'current_username': current_username})

def delete_receipe(request, id):
    queryset = Receipes.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

def update_receipe(request, id):
    queryset = Receipes.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')
    return render(request, 'polls/update_receipes.html', context={'receipe': queryset,})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/receipes/')
    return render(request, 'polls/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully you are logged in now')
        return redirect('/register/')


    return render(request,'polls/register.html')

def student_data(request):
    return render(request, 'student.html')

def get_students(request):
    queryset = Student.objects.all()
    paginator = Paginator(queryset, 20)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    print(page_obj.object_list)
    return render(request, 'report/students.html',{'queryset':page_obj})
