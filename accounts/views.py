from django.shortcuts import render,redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    decorators,
	)
from .forms import UserLoginForm,UserRegisterForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def login_view(request):
	print(request.user.is_authenticated())
	title = "login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated())
		return redirect("/uploads/list/")

	return render(request,"loginform.html",{"form":form,"title":title})

def register_view(request):
	form = UserRegisterForm(request.POST or None)
	title = "Register"
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username,password=password)
		login(request,new_user)
		return redirect("/uploads/list/")

	context = {
	"form":form,
	"title":title
	}
	return render(request,"loginform.html",context)

def logout_view(request):
	logout(request)
	return redirect("/login/")