from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course, Desc, Comment


def index(request):
    context = {
        'all_courses' : Course.objects.all(),
        'all_desc' : Desc.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    new_course = Course.objects.create(name = request.POST['name_input'])
    new_desc = Desc.objects.create(course=new_course, desc = request.POST['desc_input'])
    return redirect('/')

def destroy_yn(request, course_id):
    context = {
        'this_course' : Course.objects.get(id=course_id)
    }
    return render(request, 'destroy.html', context)

def destroy(request, course_id):
    if request.method == 'POST':
        delete_course = Course.objects.filter(id=course_id)
        delete_course.delete()
        return redirect('/')
    return redirect('/')

def comments(request, course_id):
    
    context = {
        'this_course' : Course.objects.get(id=course_id),
        'all_comments' : Comment.objects.filter(course=Course.objects.get(id=course_id)),
    }
    return render(request, 'comments.html', context)

def comment_create(request, course_id):
    
    if request.method == 'POST':
        new_comment = Comment.objects.create(course=Course.objects.get(id=course_id), comment=request.POST['comment_input'])
    return redirect(f'/comments/{course_id}')

def comment_destroy(request, course_id, comment_id):
    if request.method == 'POST':
        delete_comment = Comment.objects.get(id=comment_id)
        delete_comment.delete()
    return redirect(f'/comments/{course_id}')
