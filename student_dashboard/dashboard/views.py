from django.shortcuts import render
from .models import Student

def dashboard(request):
    student_data = None
    lookup_id = request.GET.get('student_id') or request.POST.get('student_id')  # ✅ unified lookup

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student, created = Student.objects.get_or_create(student_id=student_id)
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.parent_name = request.POST.get('parent_name')
        student.parent_phone = request.POST.get('parent_phone')
        student.academic_records = request.POST.get('academic_records')
        student.save()
        student_data = student
        return render(request, 'dashboard.html', {
            'student': student_data,
            'lookup_id': student_id  # ✅ include this to avoid template crash
        })

    elif request.method == 'GET' and 'student_id' in request.GET:
        try:
            student_data = Student.objects.get(student_id=lookup_id)
        except Student.DoesNotExist:
            student_data = None
        return render(request, 'dashboard.html', {
            'student': student_data,
            'lookup_id': lookup_id  # ✅ include even if student doesn't exist
        })

    # For plain GET without student_id param
    return render(request, 'dashboard.html', {'lookup_id': lookup_id})
