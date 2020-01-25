from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, reverse

from .forms import RegisterForm, LoginForm

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout

# Create your views here.

def my_register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form = form.clean()
			username = form.get("username")
			email = form.get("email")
			password = form.get("password")
			remember_me = form.get("remember_me")

			newUser = User(username=username, email=email)
			newUser.set_password(password)
			newUser.save()

			login(request, newUser)
			messages.success(request,"Uğurla qeydiyyatdan keçdiniz.")
			if not remember_me:
				request.session.set_expiry(0)
			return redirect("index")
		else:
			return render(request, 'register.html', {'form': form})
	form = RegisterForm()
	return render(request, 'register.html', {'form': form})
  
def my_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.clean()
			username = data["username"]
			password = data["password"]
			remember_me = data["remember_me"]
			user1 = None
			if '@' in username:
				user1 = authenticate(request, email=username, password=password)
			else:
				user1 = authenticate(request, username=username, password=password)
			if user1 is not None:
				messages.success(request,"Daxil olma uğurla başa çatdı")
				login(request,user1)
				if not remember_me:
					request.session.set_expiry(0)
				return redirect('index')
			else:
				messages.info(request,"Isdifadəçi adı və ya Parol səhvdir")
				return render(request,"login.html", {'form': form})
	form = LoginForm()
	return render(request,"login.html", {'form': form})

def logoutUser(request):
    logout(request)
    messages.success(request,"Çıxış edildi")
    return redirect("login")

	
	      