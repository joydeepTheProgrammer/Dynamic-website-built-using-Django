from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from app.models import Contact
# Create your views here.

def home(req):
    return render(req, "home.html")




def signup(req):

    if req.method == 'POST':
        username=req.POST['username']
        email=req.POST['email']
        fname=req.POST['fname']
        lname=req.POST['lname']
        pass1=req.POST['pass1']
        pass2=req.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(req, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(req, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(req, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success=(req, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")
        



def handleLogin(req):
    if req.method=="POST":
        # Get the post parameters
        loginusername=req.POST['loginusername']
        loginpassword=req.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(req, user)
            messages.success(req, "Successfully Logged In")
            return render(req, "user_profile.html")
        else:
            messages.error(req, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
    



def handleLogout(req):
    logout(req)
    messages.success(req, "Successfully logged out")
    return redirect('home')
   



def services(req):
    return render(req, 'services.html')




def contact(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        address = req.POST['address']
        city = req.POST['city']
        state = req.POST['state']
        zip = req.POST['zip']
        message = req.POST['message']
        contact = Contact(name=name, email=email, address=address, city=city, state=state, zip=zip, message=message)
        contact.save()
        messages.success(req, 'Form submitted successfully!')
    return render(req, 'contact.html')





