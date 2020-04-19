import logging

from django.contrib.auth import authenticate
from django.contrib.auth import login as lin
from django.contrib.auth import logout as lout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse

logger = logging.getLogger(__name__)


def login(request):
    ip = request.META.get('REMOTE_ADDR')
    if request.method == 'GET':
        return render(request, 'authentication/login.html')
    if 'username' not in request.POST or 'password' not in request.POST:
        logger.debug(f"Remote host ({ip}) tried to POST to login without 'username' or 'password'")
        return HttpResponseBadRequest('"username" and "password" must be supplied in login request')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        lin(request, user)
        logger.debug(f"User ({username}) successfully logged in from remote host ({ip})")
        # Redirect to a success page.
        return HttpResponseRedirect(reverse('collector:index'))
    else:
        logger.debug(f"User ({username}) failed to log in from remote host ({ip}) using invalid credentials")
        response = HttpResponse(status=401)
        return response


def logout(request):
    if not request.user.is_authenticated:
        return render(request, 'authentication/logout.html')
    else:
        lout(request)
        ip = request.META.get('REMOTE_ADDR')
        username = request.user.username
        logger.debug(f"User ({username}) logged out of session from remote host ({ip})")
        return HttpResponseRedirect(reverse('logout'))
