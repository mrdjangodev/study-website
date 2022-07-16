from ads.models import Ads
from django.contrib.auth.decorators import login_required

def universal_elements(request):
    user = request.user
    return {'user': user}

def get_ads(request):
    user = request.user
    statuses = ['Student', 'Teacher', 'Teacher_And_Student']
    my_ads = []
    studendt_ads = ''
    teacher_ads = ''
    number_of_new_messages = 0
    if user.is_authenticated:
        if user.status in statuses:
            ads_for_everyone = Ads.objects.filter(speacial_for="everyone")
            if user.status != "Teacher_And_Student":
                if user.status == "Student":
                    studendt_ads = Ads.objects.filter(speacial_for="Student")                  
                elif user.status == "Teacher":
                    teacher_ads = Ads.objects.filter(speacial_for="Teacher")
                    
            else:
                studendt_ads = Ads.objects.filter(speacial_for="Student")
                teacher_ads = Ads.objects.filter(speacial_for="Teacher")

            my_ads.extend(studendt_ads)
            my_ads.extend(teacher_ads)
            my_ads.extend(ads_for_everyone)
            

        for my_ad in my_ads:
            if user not in my_ad.ad_seen_by_users.all():
                number_of_new_messages +=1
       
    context = {
        'my_ads': my_ads,
        'number_of_new_messages': number_of_new_messages,
    }
    return context


