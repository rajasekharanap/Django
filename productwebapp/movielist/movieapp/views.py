from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Movies
from .forms import Movieform

def index(request):
    data=Movies.objects.all()
    context={'moviekey':data}
    return render(request,'index.html',context)

def mid(request,mov):
    movie=Movies.objects.get(id=mov)
    return render(request,"aboutmovie.html",{'about':movie})

def upload(request):
    if request.method=='POST':
        n=request.POST.get('nm')
        d = request.POST.get('ds')
        y = request.POST.get('yr')
        i = request.FILES['im']
        uploaddb=Movies(name=n,desc=d,year=y,img=i)
        uploaddb.save()
    return render(request,"upload.html")

def update(request,objid):
    table=Movies.objects.get(id=objid)
    model=Movieform(request.POST or None,request.FILES,instance=table)
    if model.is_valid():
        model.save()
        return redirect('/')
    return render(request,"update.html",{'table':table,'model':model})

def delete(request,delid):
    if request.method=="POST":
        item=Movies.objects.get(id=delid)
        item.delete()
        return redirect('/')
    return render(request,'delete.html')

