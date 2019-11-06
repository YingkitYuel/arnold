from django.shortcuts import render,HttpResponse
import time

# Create your views here.
def showtime(req):
    #return HttpResponse('hello')
    t = time.ctime()

    #return render(req, 'index1.html', locals())
    return render(req, 'index1.html', {'time':t})

# def article_year(req,year,month):
#     return HttpResponse('year:%s, month:%s' %(year, month))

def article_year_month(req,year, month):
    return HttpResponse('year:%s, month:%s' %(year, month))

def register(req):
    #return HttpResponse('ok')
    print(req.GET)
    print(req.GET.get('user'))

    return render(req, 'register.html')