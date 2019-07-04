from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import RIG,Lecturer,Publication,ResearchGrant,Performance
from mysite import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template import Template, Context

def Home(request):
	all_rigs = list(RIG.objects.all())
	context = {'all_rigs': all_rigs}
	return render(request, 'webapp/home.html', context)


def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                messages.warning(request, 'Error! Invalid Username or Password')
        else:
            messages.warning(request, 'Error! Invalid Username or Password')

    return render(request, "webapp/login.html", {'redirect_to': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)	

@login_required
def Home(request):
    return render(request, "webapp/home.html", {})

def About(request):
    return render(request, "webapp/about.html", {})

def per2018(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    return render(request, "webapp/2018.html", context)

def Grant(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    return render(request, "webapp/grant.html", context)

def Test(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    return render(request, "webapp/test.html", context)

def Performance1(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    return render(request, "webapp/performance1.html", context)

def Indexedjournal(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    return render(request, "webapp/indexedjournal.html", context)

def Nonindexedjournal(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    return render(request, "webapp/nonindexedjournal.html", context)

def Otherpublication(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    return render(request, "webapp/otherpublication.html", context)

def Nationalgrant(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    return render(request, "webapp/nationalgrant.html", context)

def NationalgrantRM(request):
    rig = RIG.objects.all()
    lect = Lecturer.objects.all()
    pub = Publication.objects.all()
    res = ResearchGrant.objects.all()
    per = Performance.objects.all()
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,

    }
    context = {
                "rig": rig,
                "lect": lect,
                "pub": pub,
                "res": res,
                "per": per,
    }
    return render(request, "webapp/nationalgrantRM.html", context)