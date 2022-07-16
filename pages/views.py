from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from courses.models import SpecializeModel, CourseModel
from exams.models import Test, Question
# Create your views here.



def home(request):
    
    specializes = SpecializeModel.objects.all()
    courses = CourseModel.objects.all()
    context = {
        'specializes': specializes, 
        'courses': courses,
    }
    return render(request, 'index.html', context)




def dashboard_about(request):
    
    context = {
        
    }
    return render(request, 'dashboard_templates/about.html', context)


# def dashboar_article(request):
    
#     return render(request, 'dashboard_templates/article.html')


def dashboard_sertificate(request):
    
    return render(request, 'dashboard_templates/certificates.html')



def dashboard(request):
    
    return render(request, 'dashboard_templates/dashboard.html')



def documents(request):
    
    return render(request, 'dashboard_templates/documents.html')


def help_handbook(request):
    
    return render(request, 'dashboard_templates/help-handbook.html')





def help_security_view(request):
    return render(request, 'dashboard_templates/help-security.html')


def help_terms_view(request):
    return render(request, "dashboard_templates/help-terms.html")


def help_view(request):
    return render(request, 'dashboard_templates/help.html')





def media_view(request):
    return render(request, 'dashboard_templates/media.html')



def poisk_view(request):
    return render(request, "dashboard_templates/poisk.html")


def search_view(request):
    return render(request, 'dashboard_templates/search.html')




# def videos_error_view(request):
#     return render(request, 'dashboard_templates/videos-error.html')


# def videos_view(request):
#     return render(request, 'dashboard_templates/videos.html')


# def test_quiz_view   