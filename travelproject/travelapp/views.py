from django.shortcuts import HttpResponse
from django.shortcuts import render

from . models import Place,Team
def website(request):
    fields= Place.objects.all()
    data = Team.objects.all()
    return render(request,"index.html",{'obj':fields,'founders':data})



