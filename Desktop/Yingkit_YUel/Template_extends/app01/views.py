from django.shortcuts import render

# Create your views here.

def backend(req):
    #return render(req, 'index.html')
    return render(req, 'base.html')

def student(req):
    student_list = ['磊磊', '鹿杨', '水军', '老牛']

    return render(req, 'student2.html',locals())