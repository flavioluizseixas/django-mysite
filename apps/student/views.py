from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Student
from .forms import StudentForm

@login_required
def students_list(request):
    termo_busca = request.GET.get('q', None)

    if termo_busca:
        students = Student.objects.filter(
            Q(registration__icontains=termo_busca) | Q(user__username__icontains=termo_busca)
        )
    else:
        students = Student.objects.all()

    return render(request, 'student_list.html', {'students': students, 'termo_busca': termo_busca})


@login_required
def student_new(request):
    form = StudentForm(request.POST or None, request.FILES or None)

    if 'cancel' in request.POST:
        return redirect('index')

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'student_form.html', {'form': form})


@login_required
def student_update(request, id):
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)

    if 'cancel' in request.POST:
        return redirect('index')

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'student_form.html', {'form': form})


@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            student.delete()

        return redirect('index')

    return render(request, 'student_delete_confirm.html', {'student': student})
