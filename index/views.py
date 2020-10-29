from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
	return  render(request, "index.html")

def about(request):
	return  render(request, "about.html")

#for user register
def register(request):
	if request.method == 'POST':
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')
		
		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		# from django.shortcuts import redirect
		return redirect('index')
	return render(request, 'index/register.html')

def login(request):
	if request.method == "POST":
		username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "index/login.html", {
                "message": "Invalide credentials"
            })
	return render(request, 'index/login.html')