"""GIT REPOSITORY LINK
     https://github.com/dhwani911/caninsure/pull/new/master

     webpage = caninsure.pythonanywhere.com
"""

from django.shortcuts import render,redirect,HttpResponse
from app_insure.models import Products,Services,Client
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    """Home screen"""
    return render(request,'./home.html')

# AUTHENTICATION APIs
def handleSignup(request):
    """Signup page"""

    if request.method == "POST":
        # Get the Post Parameters
        fullname = request.POST['name']
        dob = request.POST['dob']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        # Validation for user creation
        # check for length of username characters
        if len(phone) < 10:                             # The phone is not less than 10 digits long.
            print(len(phone))
            messages.error(request, "Your phone number must be under 10 characters")
            return redirect("/")
        if len(password) >= 8:
            if not password.isalnum():                  # The password is not less than 8 characters with at least 1 digit.
                messages.error(request, "Username characters must be letters and alpha")
                return redirect("/")

        # Create the user with username is "email" to login
        myuser = User.objects.create_user(email, email,password,fullname,dob,address)
        messages.success(request, "Your user has been created successfully")
        return redirect('home')
    else:
        return HttpResponse("404- Not Found")


def handleLogin(request):
    """Login function"""
    if request.method == "POST":
        # Get the Post Parameters
        loginusername = request.POST['loginusername']               # Fetching loginusername and loginpassword
        loginpassword = request.POST['loginpassword']

        # firstly, authenticate user details into our database as below
        user = authenticate(username=loginusername,
                            password=loginpassword)

        if user is not None:  # if user is not none...that means if user has value...it would allow to login
            login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect("/")
        else:
            messages.success(request, "Invalid credentials! please try again")
            return redirect('home')

    return HttpResponse('404- Not Found')


def handleLogout(request):
    """Logout function"""
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('/')

def productList(request):
    products = Products.objects.all()
    services = Services.objects.all()
    context = {'products':products,'services':services}
    return render(request,'app_insure/products.html',context)