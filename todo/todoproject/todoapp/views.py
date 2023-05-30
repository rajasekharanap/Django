from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Todo
from .forms import Taskform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class Lstview(ListView):
    model=Todo
    template_name='homepage.html'
    context_object_name='taskdet'

class Detailview(DetailView):
    model=Todo
    template_name = 'taskdetails.html'
    context_object_name = 'detview'

class Updateview(UpdateView):
    model=Todo
    template_name = 'cbvupdate.html'
    context_object_name = 'detview'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class Deleteview(DeleteView):
    model=Todo
    template_name = 'deletetask.html'
    success_url = reverse_lazy('taskpage')



def task(request):
    tskdet = Todo.objects.all()
    if request.method=='POST':
        nam=request.POST.get('ta','')
        pri=request.POST.get('pr','')
        dat=request.POST.get('da','')
        taskvar=Todo(name=nam,priority=pri,date=dat)
        taskvar.save()
    return render(request,'homepage.html',{'taskdet':tskdet})


# def taskdetail(request):
#     return render(request,"taskdetails.html",)

def delete(request,delid):
    deleteid=Todo.objects.get(id=delid)
    if request.method=='POST':
        deleteid.delete()
        return redirect('/')
    return render(request,"deletetask.html")

def update(request,updid):
    updateid =Todo.objects.get(id=updid)
    taskupd=Taskform(request.POST or None,instance=updateid)
    if taskupd.is_valid():
        taskupd.save()
        return redirect('/')
    return render(request,"update.html",{'tskup':taskupd,'upid':updateid})


