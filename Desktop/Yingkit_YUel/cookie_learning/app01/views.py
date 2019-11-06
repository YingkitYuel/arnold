from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        pwd = req.POST['password']
        if username == 'abc' and pwd == '123':
            req.session['is_login'] = 'True'
            req.session['username'] = 'abc'

            return redirect('/backend/')
    return render(req, 'login.html')


def backend(req):
    is_login = req.session.get('is_login', False)

    if is_login:
        cookie_content = req.COOKIES
        session_content = req.session
        username = req.session['username']
        return render(req, 'backend.html', {
            'cookie_content':cookie_content,
            'session_content':session_content,
            'username':username
        })
    else:
        return redirect('/login/')

def logout(req):
    try:
        del req.session['is_login']
    except KeyError:
        pass
    return redirect('/login/')