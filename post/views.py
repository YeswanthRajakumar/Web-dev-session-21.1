from django.shortcuts import render
from django.http.response import HttpResponse
from foodDB import foodData

def getPostsList(request):
    foodInfo ={
        "foods" : foodData
    }
    return render(request,template_name='post/post-list.html',context= foodInfo)

def getHome(request):
    cohort ={
         "current_cohort" : "21.2",
         "cohort_name" : "Romans" 
          }

    return render(request , template_name='post/home.html', context= cohort)

