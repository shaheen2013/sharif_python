from django.http import HttpResponse
from django.shortcuts import redirect




def is_staf_checker(view_func):
    def wrapper_func(request,*args,**kwargs):
        print(request.user)
        if request.user.is_staff:
            return redirect('/create-user')
        else:
            return HttpResponse("You can not create any user")
    return wrapper_func