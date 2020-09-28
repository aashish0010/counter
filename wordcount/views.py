from django.http import HttpResponse
from django.shortcuts import render

# def wordcount(request):
#     return HttpResponse('Hello')

def wordcount(request):
    return render(request,'home.html')

    

def count(request):
    full=request.GET['fulltext']

    wordlist= full.split()

    return render(request,'count.html',{'full':full,'count':len(wordlist)})





def about(request):
    return render(request,'about.html')