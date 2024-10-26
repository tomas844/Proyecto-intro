from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def hola_mundo(request):
 #   return HttpResponse("Nos echamos intro")

from django.shortcuts import render

def mi_app(request):
    return render(request, 'mi_app/index.html')