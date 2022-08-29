from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student
from .forms import PersonForm

def index(request):
    return render(request, 'student_register/index.html')

def student_add_update(request):
    form = PersonForm()
    # print(form)                             

    if request.method == 'POST':
        form = PersonForm(request.POST)
        # print(form)  
        if form.is_valid():
            print(form)               
            form.save()
            # return HttpResponse('Your task was created')
            return redirect('list')

    context = {
        'form' : form,
    }

    return render(request, 'student_register/student_form.html', context)



def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students,
    }

    return render(request, 'student_register/student_list.html', context)

def student_delete(request):
    pass