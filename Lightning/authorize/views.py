from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import simplejson


@csrf_exempt
def user_login(request):
    res = {
        'status': 'OK',
        'msg': ''
    }
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            res['status'] = 'FAIL'
            res['msg'] = 'User not exist'
            return JsonResponse(simplejson.dumps(res), safe=False)
        user = authenticate(username=username, password=password)
        if user is None:
            res['status'] = 'FAIL'
            res['msg'] = 'Wrong password'
            return JsonResponse(simplejson.dumps(res), safe=False)
        res['status'] = 'OK'
        res['msg'] = 'SUCCESS'
        detail = {
            'username': username,
            'groups': [level.name for level in user.groups.all()]
        }
        res['detail'] = detail
        login(request, user)
        return JsonResponse(simplejson.dumps(res), safe=False)
    else:
        return HttpResponse(None)


def user_logout(request):
    res = {
        'status': 'OK',
        'msg': 'SUCCESS'
    }
    logout(request)

    return JsonResponse(simplejson.dumps(res), safe=False)


@csrf_exempt
def register(request):
    res = {
        'status': 'OK',
        'msg': 'SUCCESS'
    }

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        try:
            User.objects.get(username=username)
            res['status'] = 'FAIL'
            res['msg'] = ''
        except User.DoesNotExist:
            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()

        return JsonResponse(simplejson.dumps(res), safe=False)


def is_login(request):
    res = {
        'status': '',
        'msg': ''
    }
    try:
        user = User.objects.get(username=request.GET.get('username', ''))
        user.get
        if not user.is_authenticated():
            res['status'] = 'FAIL'
            res['msg'] = 'Not login'
            return JsonResponse(simplejson.dumps(res), safe=False)
    except User.DoesNotExist:
        res['status'] = 'FAIL'
        res['msg'] = 'Not login'
        return JsonResponse(simplejson.dumps(res), safe=False)
    res['status'] = 'OK'
    res['msg'] = 'SUCCESS'
    return JsonResponse(simplejson.dumps(res), safe=False)

@login_required
def hehe(request):
    return HttpResponse('OK')


def you_need_login(request):
    res = {
        'status': 'FAIL',
        'msg': 'You need login'
    }

    return JsonResponse(simplejson.dumps(res), safe=False)
