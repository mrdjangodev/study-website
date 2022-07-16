from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from .models import Test, Question, Answer, StudentResult
from courses.models import CourseModel, CourseSection
# Create your views here.\
@login_required(login_url='register_login_page')
def test_view(request, pk_id):

    test = Test.objects.get(id=pk_id)
    print('Test:' , test)
    questions = test.get_questions()
    # questions = Question.objects.filter(test_id=pk).order_by('?')
    time = test.duration
    time_for_default_template = time*60-1
    
    # if request.POST:
    #     qws = request.POST.getlist('answer')
    #     print("Answers: ", qws)
    
    context = {
        'test': test,
        'time_for_default_template': time_for_default_template,
        'questions': questions,
    }
    return render(request, 'dashboard_templates/test.html', context)



def check_user_is_finished_course(request, id):
    course = CourseModel.objects.get(id=id)
    print(f"users: {course.finished_users.all()}")
    if request.user not in course.finished_users.all():
        sections = CourseSection.objects.filter(course_id=course)

        requored_step = len(sections)
        step = 0
        for section in sections:
            if request.user in section.fn_cs_users.all():
                step += 1
        if step == requored_step:
            course.finished_users.add(request.user)
        print('Usr checked for finihsed courses')
    else:
        print('User wasnt checked for finihsed courses')
    
@login_required(login_url='register_login_page')
def save_test_view(request, pk):
    
    test = Test.objects.get(id=pk)
    check_user_is_finished_course(request, test.course_id.id)
    
    course_section = CourseSection.objects.get(id=test.section_id.id)
    student = request.user
    if request.POST:
        print('POST recieved')
        data = request.POST
        data_ = dict(data)
        data_.pop('csrfmiddlewaretoken')
        number_of_correct_answers = 0
        is_passed = False
        score_by_percents = 0
        for k in data_.keys():
            selected_answer = request.POST.get(f'{k}')
            question = Question.objects.get(id=k)
        
            for answer in question.get_answers():
                if selected_answer !=None and selected_answer == answer.text:
                    if answer.is_correct:
                        number_of_correct_answers += 1
                        
        final_score = test.max_grade * (number_of_correct_answers/test.number_of_active_questions)
        score_by_percents = (number_of_correct_answers/test.number_of_active_questions)*100
        if score_by_percents >= test.score_to_pass:
            is_passed=True
        course = CourseModel.objects.get(id=test.course_id.id)
        section = CourseSection.objects.get(id=test.section_id.id)    
        required_data = [student.email, test, course, section, is_passed,\
            final_score, score_by_percents]
        try:
            StudentResult.objects.create(student=student, course=course,\
                section=section, test=test, is_passed=is_passed, result=score_by_percents)
        except:
            pass
        if score_by_percents >= test.score_to_pass and request.user not in course_section.fn_cs_users.all():
            course_section.fn_cs_users.add(request.user)
    else:
        print("Post doen't exist")
    return redirect('score_page', pk)


@login_required(login_url='register_login_page')
def score_view(request, pk):
    test = Test.objects.get(id=pk)
    # check_user_is_finished_course(request, test.course_id.id)
    results = StudentResult.objects.filter(test=test, student=request.user).order_by('-created_at')
    list_results = []
    for result in results:
        correct_answers = (result.result/100)*test.number_of_active_questions
        incorrect_answers = test.number_of_active_questions - correct_answers
        dict_result = {
            'extra_result':  {
                'correct_answers': correct_answers,
                'incorrect_answers': incorrect_answers,
                'result': result.result, 
                'created_at': result.created_at,
                'is_passed': result.is_passed,
            }
        }
        list_results.append(dict_result)
    context = {
        'test': test,
        'results': results,
        'list_results': list_results,
    }
    return render(request, 'dashboard_templates/score.html', context) 