from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def login(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            check_user = User.objects.get(email=email)
            if check_user.password == password:
                request.session['email'] = email
                request.session['type'] = check_user.account_type
                print('successful' , request.session['type'])
                return redirect('account')
            else:
                context['error'] = "error"
        except Exception as e:
            print(e)
            context['error'] = "error"
    return render(request, 'login.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        acc_type = request.POST.get('type')
        try:
            new_user = User.objects.create(email=email, name = name, password = password, account_type = acc_type)
            #print(email, name, password, acc_type)
            return redirect('login')
        except Exception as e:
            print(e)
            context = {"error": "error"}
    return render(request, 'register.html', context)

def logout(request):
    try:
        if request.session['email']:
            del request.session['email']
            del request.session['type']
    except Exception as e:
        print(e)
    return redirect('index')