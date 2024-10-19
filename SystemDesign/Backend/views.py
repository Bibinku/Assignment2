from django.shortcuts import render,redirect
from Backend.models import UserDB,ProductDB

# Create your views here.

#create indexpage function in views
def indexpage(req):
    return render(req,"Index.html")
#We have to add User details
#So, Create Function named as adduser
def adduser(req):
    return render(req,"AddUser.html")

#To save User
def saveuser(req):

    if req.method =="POST":

        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('mobile')

        obj=UserDB(name=a,email=b,mobile=c)
        obj.save()
        redirect(displayuser)

def displayuser(req):
    data = UserDB.objects.all()
    return render(req,"displayuser.html",{'data':data})


def edituser(req,Userid):
    data=UserDB.objects.get(id=Userid)
    return render(req,"edituser.html",{'data':data})

def updateuser(req,Userid):
    if req.method =="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('mobile')

        UserDB.objects.filter(id=Userid).update(name=a,email=b,mobile=c)
        return redirect(displayuser)

def deleteuser(req,Userid):
    data=UserDB.objects.filter(id=Userid)
    data.delete()
    return redirect(displayuser)

def productpage(req):

    return render(req,"addproduct.html")

def saveproduct(req):

    if req.method =="POST":

        a=req.POST.get('name')

        b=req.POST.get('price')

        obj=ProductDB(name=a,price=b,)
        obj.save()
        redirect(displayproduct)

def displayproduct(req):
    cata=ProductDB.objects.all()
    return render(req,"displayproduct.html",{'cata':cata})


def editproduct(req,Proid):
    cata=ProductDB.objects.get(id=Proid)
    return render(req,"editproduct.html",{'cata':cata})


def updateproduct(req,Proid):
    if req.method =="POST":
        a=req.POST.get('name')
        b=req.POST.get('price')


        ProductDB.objects.filter(id=Proid).update(name=a,price=b)
        return redirect(displayproduct)

def deleteproduct(req,Proid):
    cata=ProductDB.objects.filter(id=Proid)
    cata.delete()
    return redirect(displayproduct)
