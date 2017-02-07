# -*- coding:utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect


def authenticate_user(request):
    if request.POST:
        if 'email' not in request.POST:
            return JsonResponse({'success': False, "reason": "missing_email"})

        if 'password' not in request.POST:
            return JsonResponse({'success': False, "reason": "missing_password"})

        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, "reason": "username_or_email_used"})

        new_user = User.objects.create_user(email, email, password)
        new_user.save()

        user = authenticate(username=email, password=password)
        login(request, user)

        return JsonResponse({"success": True, 'next_page': '/mainpage'})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

