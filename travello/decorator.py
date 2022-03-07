from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseNotFound  


def above18(function):
    def inner(request, *args, **kwargs):
        u = User.objects.get(username=request.user)
        if(u.account.age>21):
            return function(request, *args, **kwargs) 
        else:
            return HttpResponseNotFound('<h1>No Page Here</h1>')  
    return inner
