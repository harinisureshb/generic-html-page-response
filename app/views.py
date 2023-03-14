from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'HARINISURESH','father':'d/o : SURESHREDDY'}
    return render(request,'first.html',context=d)
