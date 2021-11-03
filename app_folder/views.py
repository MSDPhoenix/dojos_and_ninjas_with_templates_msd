from django.shortcuts import render,redirect
from .models import *
def index(request):
    context = {
        "dojos":Dojo.objects.all()
    }
    return render(request,'main_page.html',context)

def index2(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')

def index3(request):
    if len(Dojo.objects.all()) ==0:
        context = {
        "message":"Please create a dojo first!",
        }
        return render(request,'main_page.html',context)
    else:
        Ninja.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dojo=Dojo.objects.get(id=request.POST['dojo']),
        )
        return redirect('/')

def index4(request):
    Dojo.objects.all().delete()
    return redirect('/')

def delete_dojo(request,dojo_id):
    Dojo.objects.get(id=dojo_id).delete()
    return redirect('/')

