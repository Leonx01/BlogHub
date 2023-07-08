from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():#进行约束性检验
            new_user=form.save()#创建user对象
            authenticated_user = authenticate(username=new_user.username, 
                                              password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form}
    return render(request,'users/register.html',context)
