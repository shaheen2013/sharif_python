from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .decorators import is_staf_checker
# from django.contrib.auth import get_user_model
# User = get_user_model()


@login_required(login_url='/admin-login')
def DashBoardView(request):
    return render(request, 'admin-pages/index.html')


class LoginView(generic.View):

    def get(self,request):
        return render(request, 'admin-pages/login.html')

    def post(self,request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/admin-login')


def logoutView(request):
    logout(request)
    return redirect('/admin-login')


class CreateUser(generic.View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'admin-pages/user-creation-page.html',{"form":form})


    def post(self,request):
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # con_pass = request.POST.get('confirm_password')
        # if password == con_pass:
        #     user = CustomUser(email=email,password=password)
        #     user.set_password(password)
        #     user.save()
        #     return redirect('/')
        # else:
        #     return redirect('/create-user')
        user = CustomUserCreationForm(request.POST)
        print(user.is_valid())
        if user.is_valid():
            user.save()
            return redirect('/')
        else:
            return redirect('/create-user')