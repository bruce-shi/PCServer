from django.shortcuts import render
from PCWebService.models import UserRecords
from django.http import JsonResponse
# Create your views here.


def add_history(request):
    if request.user.is_authenticated():
        url = request.POST.get("url", "")
        duration = request.POST.get("active", 0)
        user = request.user
        record = UserRecords(url=url, duration=duration, user=user)
        record.save()
        return JsonResponse({'status':True})
    else:
        return  JsonResponse({'status':False, 'error':403})