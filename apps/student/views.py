from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm


@login_required
def students_list(request):
    termo_busca = request.GET.get('pesquisa', None)

    if termo_busca:
        students = Student.objects.filter(registration__icontains=termo_busca)
    else:
        students = Student.objects.all()

    return render(request, 'student_list.html', {'students': students})


@login_required
def student_new(request):
    form = StudentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'student_form.html', {'form': form})


@login_required
def student_update(request, id):
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'student_form.html', {'form': form})


@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student_delete_confirm.html', {'student': student})
