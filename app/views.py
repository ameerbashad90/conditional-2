from django.shortcuts import render

# Create your views here.
def con_ameer(request):
    d={'a':9, 'b':5,'c':7}
    return render(request,'con_ameer.html',d)
    
