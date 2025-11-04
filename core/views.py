from django.shortcuts import redirect, render
from core.models import*

# Create your views here.


def tcp(request):
    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        email=data.get("email")
        contact=data.get("contact")
        massage=data.get("massage")
        image=request.FILES.get("image")

        print(name)
        print(massage)
        print(email)
        print(contact)
        print(image)


        h.objects.create(
            name=name,
            email=email,
            contact=contact,
            message=massage,
            image=image
        )
    queryset=h.objects.all()
    context={'tcp':queryset}
    return render(request,'index.html',context)

def delete(request,id):
    queryset=h.objects.get(id = id)
    queryset.delete()
    return redirect('/tcp')
    
def update(request,id):
    queryset=h.objects.get(id = id)

    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        email=data.get("email")
        contact=data.get("contact")
        massage=data.get("massage")
        image=request.FILES.get("image")

        queryset.name=name
        queryset.email=email
        queryset.contact=contact
        queryset.message=massage

        if image:
            queryset.image=image
        
        queryset.save()    
        return redirect('/tcp/')
    context={'tcp':[queryset]}
    return render(request,'index.html',context) 
    
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(first_name)
        print(last_name)
        print(username)
       
        if first_name and last_name and username and password:
            if User.objects.filter(username=username).exists():
                context = {"error": "Username already taken."}
                return render(request,'register.html', context)

            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            user.save()

            return redirect('/register/')  # Or redirect to login or homepage
        else:
            context = {"error": "All fields are required."}
            return render(request, 'login.html', context)

    return render(request, 'register.html') 

from django.contrib.auth.hashers import check_password


def login(request):
    if request.session.get('user'):
        return redirect('/get')
    if request.method == "POST":  
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user:
            pwd=check_password(password,user.password)

            if pwd:
                request.session['user']=user.username
                return redirect('/login')
            else:
                return render(request,'login.html',{'errorMsg':'Invalid Password'})
        else:
            return render(request,'login.html',{'errorMsg':'Invalid User'})
    return render(request,'login.html')


from django.shortcuts import render
from .models import m   # make sure this import is correct

# contact page

def con(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        contact = data.get("contact")
        password =data.get("password")

        # Save data to database
        m.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact=contact,
            password=password
        )

        return redirect('/about')

    queryset = m.objects.all()
    context = {'con':queryset}
    return render(request, "contact.html", context)


def abot(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        contact = data.get("contact")
        password =data.get("password")

        # Save data to database
        m.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact=contact,
            password=password
        )

    queryset = m.objects.all()
    context = {'abot':queryset}
    return render(request, "about.html", context)

def session(request):
    request.session['user'] ='tcp'
    return render(request,'session.html')

def get(request):
    if request.session.get('user'):
     return render(request,'get.html')
    else:
        return redirect('/login')

def logout(request):
    request.session.flush()
    return redirect('/login')


def header1(request):
    return render(request,"header1.html")

def prohome(request):
    return render(request,"prohome.html")

def proabout(request):
    return render(request,'proabout.html')  

def prolatestnews(request):
    return render(request,'prolatestnews.html')

def procategary(request):
    return render(request,'procategary.html')

def procontact(request):
    if request.method == "POST":
        data = request.POST
        message = data.get("message")
        name = data.get("name")
        email = data.get("email")
        subject = data.get("subject")

        # Save data to database
        Contact.objects.create(
            message=message,
            name=name,
            email=email,
            subject=subject,
        )

    queryset = Contact.objects.all()
    context = {'cont':queryset}
    return render(request,'procontact.html',context)






# def contact(request):
#     return render(request, contact.html')



    











