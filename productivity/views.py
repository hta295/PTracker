from django.contrib.auth import authenticate
from django.contrib.auth import login as lin
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    if 'username' not in request.POST or 'password' not in request.POST:
        return HttpResponseBadRequest('"username" and "password" must be supplied in login request')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        lin(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(reverse('collector:index'))
    else:
        response = HttpResponse(status=401)
        return response
