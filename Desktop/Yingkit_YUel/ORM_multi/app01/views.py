from django.shortcuts import render,HttpResponse
from app01.models import *

# Create your views here.

def index(req):
    return render(req, 'index.html')

def addbook(req):
    #方法一
    # Book.objects.create(name='Linux运维', price=77, pub_time='2019-10-16', publish_id=2)

    #方法二
    publish_obj = Publish.objects.filter(name='人民出版社')[0]
    Book.objects.create(name='GO', price=23, pub_time='2019-10-15', publish=publish_obj)
    return HttpResponse('添加成功！')
def update(req):pass
def delete(req):pass
def select(req):
    ret = Book.objects.filter(publish__name='人民出版社').values('name', 'price')
    print(ret)

    return HttpResponse('查询成功！')