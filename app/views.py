from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':444,'b':44,}
    return render(request,'condition.html', context=d)