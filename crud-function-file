from django.shortcuts import render, redirect
from . models import Student

# Create your views here.
def home(request):
    std=Student.objects.all()
    return render(request,"home.html", {'std':std})
def add(request):
    if request.method=="POST":
        names=request.POST.get("std_name")
        rolls=request.POST.get("std_roll")
        emails=request.POST.get("std_email")
        phones=request.POST.get("std_phone")
        addresss=request.POST.get("std_address")

        s=Student()
        s.name=names
        s.roll=rolls
        s.phone=phones
        s.address=addresss
        s.emeil=emails

        s.save()
        return redirect('/home')
    return render(request,"add.html")
def delete(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect('/home')

def update(request,roll):
     std=Student.objects.get(pk=roll)
     return render(request,'update.html' ,{'std':std})


def doupdate(request,roll):
    std_roll=request.POST.get('std_roll')
    std_name=request.POST.get('std_name')
    std_email=request.POST.get('std_email')
    std_phone=request.POST.get('std_phone')
    std_address=request.POST.get('std_address')
    std=Student.objects.get(pk=roll)

    std.roll=std_roll
    std.name=std_name
    std.emeil=std_email
    std.address=std_address
    std.phone=std_phone
    std.save()
    return redirect('/home')
