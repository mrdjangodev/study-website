from django.shortcuts import render, redirect
from django.http import JsonResponse

from config.context import get_ads
# Create your views here.
def mark_read_all(request):
    user = request.user

    my_ads = get_ads(request)['my_ads']
    for my_ad in my_ads:
        if user not in my_ad.ad_seen_by_users.all():
            my_ad.ad_seen_by_users.add(user)
    
    return redirect('dashboard_index')

def notification_view(request):
    
    return render(request, "dashboard_templates/notification.html")  