from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("This is homepage")
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def booking(request):

    return render(request,'booking.html')
def room(request):
    return render(request,'room.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')
def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

def users(request):
    return render(request,'user.html')