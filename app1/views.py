from django.shortcuts import render

# Create your views here.
def usd(request):
    d={'data':'HAI kalyani'}
    return render(request,'usd.html',d)
