from django.shortcuts import render
from accounts.models import Tweet
from accounts.test_code.testing import test
from accounts.test_code.fetch_tweets import mine
from django.views.generic import TemplateView

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == "POST":
        
        t_user = request.POST['t_user']
        
        get_tweets = []
        get_tweets = mine(t_user)
        
        sentiments = []
        for t in get_tweets:
            sentiments.append(test(t))
       
        f = 0
        not_f = 0
        for s in sentiments:
            if s == 1:
                f += 1
            else:
                not_f +=1    
                
        obj_display = Tweet(username=t_user, found=f, not_found=not_f)
        
        caption = "For Twitter User - " + t_user
        res = "Analysis shows "+ str(f) + " depressed tweets and "+str(not_f)+" non-depressed tweets"
        obj_name = Tweet(username=caption, found=res)

        obj_display
        obj_display.save()
        #print("Data saved")
        latest = Tweet.objects.all()
       
        context = {'Tweet': latest, 'UserTweet': obj_display, 'name': obj_name}

        return render(request, 'accounts/index.html', context)
    else:
        latest = Tweet.objects.all()
        context = {'Tweet': latest}
        return render(request, 'accounts/index.html', context) 
    #return render(request,'accounts/index.html')

@login_required
def logout(request):
    logout(request)
    return render(request,'accounts/index.html')

def sign_up(request):
    context = {}
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'accounts/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)


