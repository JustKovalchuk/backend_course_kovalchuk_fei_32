from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


import json


# Create your views here.
def home(request):
    return HttpResponse("authentication page")


def signup(request: HttpRequest):
    if request.method == "POST":
        print(request.POST)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]

        if User.objects.filter(email=email):
            print("error")
            messages.error(request, "Email already exists!")
            return HttpResponse(json.dumps({'result': 'False'}), content_type="application/json")

        username = first_name + " " + last_name
        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone

        user.save()
        return HttpResponse(json.dumps({'result': 'True'}), content_type="application/json")
        # messages.success(request, "Account successfully created!")

    return None


def login_request(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)

        messages.success(request, "Account successfully created!")

    return HttpResponse("login page")


def logout(request):
    return HttpResponse("logout page")
