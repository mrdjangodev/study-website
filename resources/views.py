from django.shortcuts import render, redirect
from django.http import FileResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from .models import Resource
from courses.models import CourseModel
# Create your views here.

@login_required(login_url='register_login_page')
def store_inner_view(request, type):
    my_resources = []
    documents = Resource.objects.filter(document_type=type)
    user = request.user
    
    if user.status == "Student" or user.status == "Teacher_And_Student":
        my_courses = CourseModel.objects.filter(learners=user)
        for document in documents:
            if document.recievers == 'my_students':
                for my_course in my_courses:
                    if document.auther == my_course.teacher:
                        my_resources.append(document)
            else:
                my_resources.append(document)
    if my_resources != '':
        pagination = Paginator(my_resources, 1)
        page = request.GET.get('page')
        paginated_resources2 = pagination.get_page(page)
    context = {
        'my_resources': my_resources,
        'pagination': pagination,
        'paginated_resources2': paginated_resources2,
    }
    return render(request, 'dashboard_templates/store-inner.html', context)



@login_required(login_url='register_login_page')
def store_view(request):

    return render(request, 'dashboard_templates/store.html')


@login_required(login_url='register_login_page')
def download_file(request, pk):
    file = Resource.objects.get(id=pk).file
    # type_file = file.document_type
    response = FileResponse(file)
    
    return response
    