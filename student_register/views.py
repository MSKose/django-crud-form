from django.shortcuts import render, redirect
from .models import Student
from .forms import PersonForm

# def home(request):
#     return render(request, 'student_register/base.html')



def student_add_update(request, pk = -7):
    if pk != -7:
        todo = Student.objects.get(id=pk)
        form = PersonForm(instance=todo)

        context = {
            'form' : form,
        }
        return render(request, 'student_register/student_form.html', context)

    else:
        form = PersonForm()

        if request.method == 'POST':
            form = PersonForm(request.POST)
            # print(form)  
            if form.is_valid():
                print(form)               
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

def student_delete(request):
    pass