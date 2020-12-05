from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import  Booksp,bookreport

def home(request):
    allbooks =Booksp.objects.all()

    context= {'allbooks':allbooks}
    return render(request, 'home.html',context)


def singup(request):
    return render(request, 'loginsignup.html', )


def login(request):
    return render(request, 'login.html', )


def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['repassword']

        if len(username) > 10:
            messages.error(request, "please enter less than 10 character")
            return redirect('home')


        if pass1 != pass2:
            messages.error(request, "both passwords must be same")
            return redirect('home')

        user = User.objects.create_user(username=username, password=pass1, email=email, first_name=fname,
                                        last_name=lname)
        user.save()
        messages.success(request, "your Inobooks account is created")
        return redirect("home")

    else:
        return HttpResponse("404 Error Not Found")


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect("home")
        else:
            messages.error(request, 'Please Check your credentials')
            return redirect("home")


def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

def upload(request):
    return render(request,"upload.html")

def handleupload(request):
    if request.method == 'POST':
        name = request.POST['name']
        author= request.POST['author']
        description= request.POST['description']
        bookpdf = request.FILES['selectbook']
        thumbinal=request.FILES['thumbinal']

        book =Booksp(user=request.user,name=name,author=author,Description=description,pdf=bookpdf,img=thumbinal)
        book.save()
        messages.success(request," Sucessfully Uploaded")

        return redirect('home')

    else:
        messages.danger(request,"Please fill detail Correct")
        return render(request,"upload.html")

def donate(request):
    return render(request,"donate.html")


def search(request):
    query = request.GET['query']
    print(query)
    if len(query) > 150:
        messages.error(request, 'no search resluts found')

    else:
        allsearch = Booksp.objects.filter(name__icontains=query)
        params = {'allsearch': allsearch}

    return render(request, 'search.html', params)

def pay(request):
    return render(request,'pay.html')

def bookreport(request):
    if request.method=='POST':
        comment = request.POST.get("comment")
        user = R=request.user

        post = request.POST.get("post")
        print(comment)

        report = bookreport(comment=comment,user=user, post=post)
        report.save()
        messages.success(request,"Sucessfully Reported")
        return redirect('/')
    else:
        return render(request,'home')

def aboutus(request):
    return render(request,"aboutus.html")
