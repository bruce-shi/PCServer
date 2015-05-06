from django.shortcuts import render
from PCWebService.models import UserRecords
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
import datetime
from PCServer import settings
import hashlib
from PCWebService.models import Member
import datetime
from PCWebService.forms import RegisterForm
from django.contrib.auth.models import User
import  uuid
# Create your views here.


def add_history(request):
    secret = request.get_signed_cookie(settings.CHROME_EXT_COOKIE_NAME)
    if secret is not None:
        url = request.POST.get("url", "")
        duration = request.POST.get("active", 0)
        user = request.user
        record = UserRecords(url=url, duration=duration, user=user)
        record.save()
        return JsonResponse({'status':True})
    else:
        return JsonResponse({'status':False, 'error':403})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)

        if user is not None:

            member = Member.objects.get(user=user)
            login(request,user)

            secret = hashlib.sha1(username+password).hexdigest()
            member.cookie_secret = secret
            member.last_login = datetime.datetime.now()
            member.save()
            response = JsonResponse({'status': True})
            set_cookie(response,settings.CHROME_EXT_COOKIE_NAME,secret,365*5)
            return response
        else:
            return JsonResponse({'status':False})
    else:
        return JsonResponse({'status':False})

def user_register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            user = User.objects.create_user(username=username,password=password,email=email)
            member = Member()
            member.user = user
            member.email = email
            member.UUID = ""
            member.save()
            if user:
                return JsonResponse({'status':True})
            else:
                return JsonResponse({'status':False})
        else:
            return JsonResponse({'status':False, 'errors': [(k, v[0]) for k, v in register_form.errors.items()] })
    else:
        return JsonResponse({'status':False})

def mobile_login(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        device_id = request.POST.get('UUID', None)
        user = authenticate(username=username, password=password)

        if user is not None and device_id is not None:
            member = Member.objects.get(user=user)
            member.UUID = device_id

            app_key = uuid.uuid4().hex
            member.app_key = app_key

            member.last_login = datetime.datetime.now()
            member.save()
            return JsonResponse({'status':True,'appkey':app_key})
        else:
            return JsonResponse({'status':False,'error':"Wrong username or password"})
    else:
        return JsonResponse({'status':False})


def mobile_test_news(request):
    device_id = request.POST.get("uuid")
    app_key = request.POST.get("app_key")
    user = Member.objects.filter(UUID=device_id, app_key=app_key)
    if user.exists():
        news = [
            {
                'title':"Fake news 1 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'description':"This is the demo description of fake news",
                'content':"content of the news is not important",
                'img_url':"https://www.apple.com/v/home/bq/images/og.jpg?201504300657"

            }
            , {
                'title':"Fake news 2 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'description':"This is the demo description of fake news",
                'content':"content of the news is not important",
                'img_url':"https://www.apple.com/v/home/bq/images/og.jpg?201504300657"

            }
            , {
                'title':"Fake news 3 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'description':"This is the demo description of fake news",
                'content':"content of the news is not important",
                'img_url':"https://www.apple.com/v/home/bq/images/og.jpg?201504300657"
            }
        ]

        return JsonResponse({"status":True,"resullt":news})
    else:
        return JsonResponse({'status':False,'error':403})


def set_cookie(response, key, value, days_expire = 7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60
        expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_signed_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN)