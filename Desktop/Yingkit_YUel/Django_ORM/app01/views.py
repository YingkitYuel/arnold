from django.shortcuts import render,HttpResponse
from app01.models import Book, publisher
# Create your views here.
def index(req):
    return render(req, 'index.html')

def addbook(req):
    # b = Book(name='python基础', price=99, author='秦磊', pub_time='2019-10-15')
    # b.save()

    #Book.objects.create(name='python基础', price=99, author='秦磊', pub_time='2019-10-15')
    #Book.objects.create(**dic)

    #一对多：book_obj.publish-------一定是一个对象
    # book_obj = Book.objects.get(name='python')
    # print(book_obj.name)
    # print(book_obj.pub_time)
    b = Book(name='python基础', price=99, author='秦磊', pub_time='2019-10-15')
    b.save()

    publisher.objects.create(id=None, publish='人民出版社', city='北京')
    publisher.objects.create(id=None, publish='山东出版社', city='山东')
    publisher.objects.create(id=None, publish='江苏出版社', city='江苏')
    publisher.objects.create(id=None, publish='浙江出版社', city='浙江')
    publisher.objects.create(id=None, publish='浙江出版社', city='浙江')

    return HttpResponse('添加成功')


def update(req):
    #可以改多个
    #Book.objects.filter(author='秦磊').update(price=999)

    #只能改一个
    b = Book.objects.get(author='秦磊')
    b.price = 120
    b.save()

    return HttpResponse('修改成功!')

def delete(req):
    Book.objects.filter(author='秦磊').delete()

    return HttpResponse('删除成功！')

def select(req):
    booklist = Book.objects.all()
    print(booklist)
    print(booklist[0])
    return render(req, 'index.html', {'booklist':booklist})