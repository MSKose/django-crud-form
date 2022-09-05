from django.shortcuts import render, redirect
from .models import Student
from .forms import PersonForm

# def home(request):
#     return render(request, 'student_register/base.html')



def student_add_update(request, id = -7): # equating id to -7 and then checking with an if-else whether student_add_update should do an update or create. If id is not equal to -7 it means it is an update
    if id != -7:
        todo = Student.objects.get(id=id)
        form = PersonForm(instance=todo)

        if request.method == "POST":
            form = PersonForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                return redirect("list")

        context = {
            'todo': todo,
            'form' : form,
        }
        return render(request, 'student_register/student_form.html', context)

    else:
        form = PersonForm()

        if request.method == 'POST':
            form = PersonForm(request.POST)
            if form.is_valid():
                form.save()
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

def student_delete(request, id):
    student = Student.objects.get(id=id)
    print(request.method)
    
    if request.method == "POST":
        student.delete()
        return redirect("list")

    context = {
        'student': student,
    }

    return render(request, "student_register/student_delete.html", context) 