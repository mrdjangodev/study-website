from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# my models
from .models import SpecializeModel, CourseSection, LessonModel, CourseModel
from exams.models import Test

# Create your views here.
def actual_view(request):
    return render(request, 'test_login.html')


@login_required(login_url='register_login_page')
def info_view(request, pk):
    user = request.user
    statuses = ['Student', 'Teacher', 'Teacher_And_Student']
    if user.status not in statuses:
        user.status = "Student"
        user.save()
    course = CourseModel.objects.get(id=pk)
    if request.user not in course.learners.all():
        course.learners.add(request.user)
    course_sections = CourseSection.objects.filter(course_id=pk)
    
    context ={
        'course': course,
        'course_sections': course_sections,
    }
    return render(request, "dashboard_templates/info.html", context)

@login_required(login_url='register_login_page')
def lesson_main_view(request, pk):
    """
        This view created for first time view when we enter inside of course section
        and 
        in this view I take the last lesson as current lesson
    """
    lessons = LessonModel.objects.filter(section_id=pk)
    test = Test.objects.get(section_id=pk)
    if lessons:
        last_lesson = LessonModel.objects.filter(section_id=pk, fn_l_users=request.user).last() # this variable for identifying my last time finished lesson bases on one section
        test_is_open = False
        if lessons.last() == last_lesson:
            test_is_open = True
        if not last_lesson:
            last_lesson = lessons.first()
        next_lesson = last_lesson.next_lesson()
    
        context = {
            'lessons': lessons,
            'current_lesson': last_lesson, # When I enter this page firts time I wont to see my last time entered page as current lesson
            'next_lesson': next_lesson,
            'test_is_open': test_is_open,
            'test': test,
        }
    else:
        context = {
            'test': test,
        }
    return render(request, 'dashboard_templates/lesson_main.html', context)

@login_required(login_url='register_login_page')
def lesson_view(request, course_section_id, pk):
    section = CourseSection.objects.get(id=course_section_id)
    test = Test.objects.get(section_id=section)
    
    lessons = LessonModel.objects.filter(section_id=course_section_id)
    current_lesson = LessonModel.objects.get(section_id=course_section_id, id=pk) # this variable for identifying my last time finished lesson bases on one section
    test_is_open = False
    if lessons.last() == current_lesson:
        test_is_open = True
    next_lesson = current_lesson.next_lesson()
    user = request.user
    
    if user not in current_lesson.fn_l_users.all():
        current_lesson.fn_l_users.add(user)
 
    context = {
        'lessons': lessons,
        'current_lesson': current_lesson, # When I enter this page firts time I wont to see my last time entered page as current lesson
        'next_lesson': next_lesson,
        'test_is_open': test_is_open,
        'test': test,
    }
    return render(request, 'dashboard_templates/lesson_main.html', context)

@login_required(login_url='register_login_page')
def dashboard_index_view(request):
    user = request.user
    active_courses = CourseModel.objects.filter(learners=user)
    complated_courses = CourseModel.objects.filter(finished_users=user)
    
    context = {
        'active_courses': active_courses,
        'complated_courses': complated_courses,
    }
    return render(request, 'dashboard_templates/index.html', context)



def home3_view(request):
    user=request.user
    my_courses = CourseModel.objects.filter(learners=request.user)
    context = {
        'my_courses': my_courses,
    }
    return render(request, "dashboard_templates/index3.html", context)


